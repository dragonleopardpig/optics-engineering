from __future__ import annotations

import argparse
import copy
import json
import math
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

from svg_math_labels import latex_for_label


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "docs/source/_static"
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
TEXT_PATTERN = re.compile(r"<text\b[^>]*>.*?</text>", re.DOTALL)
MATH_PATTERN = re.compile(
    r"[=√∫∑∞≤≥≈≃∝λπθφσνδαβγΔρτξωμ²₀₁₂]"
    r"|[A-Za-z]\^|[A-Za-z]_[A-Za-z]|\b\w+/\w+\b"
    r"|^[A-Za-z](?:['′]|\d)?$"
)
POINT_TO_PIXEL = 72 / 72.27


def normalize(text: str) -> str:
    return " ".join(text.split())


def declarations(value: str) -> dict[str, str]:
    return {
        name.strip(): setting.strip()
        for name, setting in re.findall(r"([\w-]+)\s*:\s*([^;]+)", value)
    }


@lru_cache(maxsize=512)
def document_style(source: str) -> tuple[dict, list]:
    result = {"font-size": "12", "fill": "#111827", "text-anchor": "start"}
    root_markup = re.search(r"<svg\b[^>]*>", source).group()
    root = ET.fromstring(root_markup[:-1] + "/>")
    result.update(root.attrib)
    result.update(declarations(root.get("style", "")))
    rules = []
    for stylesheet in re.findall(r"<style\b[^>]*>(.*?)</style>", source, re.DOTALL):
        rules.extend(re.findall(r"([^{}]+)\{([^{}]+)\}", stylesheet))
    return result, rules


def text_style(source: str, node: ET.Element) -> dict[str, str]:
    defaults, rules = document_style(source)
    result = defaults.copy()
    for selector, body in rules:
        selectors = {value.strip() for value in selector.split(",")}
        if "text" in selectors or selectors.intersection("." + name for name in node.get("class", "").split()):
            result.update(declarations(body))
    result.update(node.attrib)
    result.update(declarations(node.get("style", "")))
    if "font" in result:
        size = re.search(r"([\d.]+)px", result["font"])
        if size:
            result["font-size"] = size.group(1)
    return result


def restored_source(source: str) -> str:
    pattern = re.compile(r'<g\b[^>]*\bdata-original-text="[^"]*"[^>]*>')
    group_tags = re.compile(r"</?g\b[^>]*>")
    replacements = []
    for match in pattern.finditer(source):
        depth = 1
        end = match.end()
        for tag in group_tags.finditer(source, end):
            if tag.group().startswith("</"):
                depth -= 1
            elif not tag.group().endswith("/>"):
                depth += 1
            if depth == 0:
                end = tag.end()
                break
        original = ET.fromstring(match.group()[:-1] + "/>").get("data-original-text")
        replacements.append((match.start(), end, original))
    for start, end, original in reversed(replacements):
        source = source[:start] + original + source[end:]
    return source


def segments(source: str, markup: str) -> list[ET.Element]:
    node = ET.fromstring(markup)
    if "Matplotlib" in source and list(node):
        return []
    children = list(node)
    if children and not (node.text or "").strip() and all(
        child.get("x") is not None and child.get("y") is not None
        for child in children
    ):
        result = []
        for child in children:
            line = ET.Element("text", {**node.attrib, **child.attrib})
            line.text = "".join(child.itertext())
            result.append(line)
        return result
    return [node]


def is_math(node: ET.Element, label: str) -> bool:
    classes = node.get("class", "").split()
    return bool(
        MATH_PATTERN.search(label)
        or set(classes).intersection({"eq", "result", "matrix", "var", "smallvar", "icontext"})
        or any(child.get("baseline-shift") for child in node)
    )


def multiply(left: tuple, right: tuple) -> tuple:
    return tuple(
        sum(left[row * 3 + index] * right[index * 3 + column] for index in range(3))
        for row in range(3) for column in range(3)
    )


def transform_matrix(value: str) -> tuple:
    result = (1, 0, 0, 0, 1, 0, 0, 0, 1)
    for name, arguments in re.findall(r"([A-Za-z]+)\(([^)]*)\)", value):
        numbers = [
            float(number)
            for number in re.findall(r"[-+]?(?:\d*\.)?\d+(?:[eE][-+]?\d+)?", arguments)
        ]
        if name == "translate":
            operation = (1, 0, numbers[0], 0, 1, numbers[1] if len(numbers) > 1 else 0, 0, 0, 1)
        elif name == "scale":
            operation = (numbers[0], 0, 0, 0, numbers[1] if len(numbers) > 1 else numbers[0], 0, 0, 0, 1)
        elif name == "rotate":
            cosine = math.cos(math.radians(numbers[0]))
            sine = math.sin(math.radians(numbers[0]))
            operation = (cosine, -sine, 0, sine, cosine, 0, 0, 0, 1)
            if len(numbers) > 1:
                operation = multiply(
                    (1, 0, numbers[1], 0, 1, numbers[2], 0, 0, 1),
                    multiply(operation, (1, 0, -numbers[1], 0, 1, -numbers[2], 0, 0, 1)),
                )
        elif name == "matrix":
            first, second, third, fourth, fifth, sixth = numbers
            operation = (first, third, fifth, second, fourth, sixth, 0, 0, 1)
        else:
            raise ValueError(f"Unsupported transform: {name}")
        result = multiply(result, operation)
    return result


def validate_bounds(path: Path) -> list[str]:
    root = ET.parse(path).getroot()
    minimum_x, minimum_y, width, height = map(float, root.get("viewBox").split())
    issues = []
    def visit(node: ET.Element, parent: tuple) -> None:
        matrix = multiply(parent, transform_matrix(node.get("transform", "")))
        if node.get("data-latex"):
            image = node.find("{" + SVG_NAMESPACE + "}svg")
            left, top, box_width, box_height = (
                float(image.get(name)) for name in ("x", "y", "width", "height")
            )
            points = [
                (
                    matrix[0] * horizontal + matrix[1] * vertical + matrix[2],
                    matrix[3] * horizontal + matrix[4] * vertical + matrix[5],
                )
                for horizontal, vertical in (
                    (left, top), (left + box_width, top),
                    (left, top + box_height), (left + box_width, top + box_height),
                )
            ]
            excess = max(
                minimum_x - min(point[0] for point in points),
                minimum_y - min(point[1] for point in points),
                max(point[0] for point in points) - minimum_x - width,
                max(point[1] for point in points) - minimum_y - height,
            )
            if excess > 2:
                issues.append(f"{path.name}: {node.get('aria-label')} ({excess:.1f}px outside canvas)")
            return
        for child in node:
            visit(child, matrix)
    visit(root, (1, 0, 0, 0, 1, 0, 0, 0, 1))
    return issues


def inventory(paths: list[Path], restore: bool = True) -> dict[str, list[str]]:
    labels: dict[str, list[str]] = {}
    for path in paths:
        source = path.read_text()
        if restore:
            source = restored_source(source)
        for match in TEXT_PATTERN.finditer(source):
            for node in segments(source, match.group()):
                label = normalize("".join(node.itertext()))
                if is_math(node, label):
                    labels.setdefault(label, []).append(str(path.relative_to(STATIC)))
    return labels


def run(command: list[str], directory: Path) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, cwd=directory, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(" ".join(command) + "\n" + result.stdout[-5000:] + result.stderr[-2000:])
    return result


def render_formulas(formulas: list[tuple[str, float]], directory: Path) -> dict:
    preamble = [
        r"\documentclass{article}",
        r"\usepackage{amsmath,amssymb}",
        r"\usepackage[active,tightpage]{preview}",
        r"\setlength\PreviewBorder{0pt}",
        r"\newsavebox{\formulabox}",
        r"\begin{document}",
    ]
    for index, (formula, size) in enumerate(formulas):
        point_size = size / POINT_TO_PIXEL
        preamble.extend([
            r"\begin{preview}",
            rf"\sbox{{\formulabox}}{{\fontsize{{{point_size:.5f}}}{{{point_size * 1.2:.5f}}}\selectfont $\displaystyle {formula}$}}",
            rf"\typeout{{LABEL-{index}:\the\ht\formulabox;\the\dp\formulabox;\the\wd\formulabox}}",
            r"\usebox{\formulabox}",
            r"\end{preview}",
        ])
    preamble.append(r"\end{document}")
    (directory / "labels.tex").write_text("\n".join(preamble))
    compiled = run(["latex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "labels.tex"], directory)
    metrics = {
        int(index): (float(height), float(depth), float(width))
        for index, height, depth, width in re.findall(
            r"LABEL-(\d+):([\d.]+)pt;([\d.]+)pt;([\d.]+)pt", compiled.stdout
        )
    }
    run([
        "dvisvgm", "--page=1-", "--no-fonts", "--bbox=preview",
        "--output=label-%p.svg", "labels.dvi",
    ], directory)
    pages = {int(path.stem.split("-")[-1]): path for path in directory.glob("label-*.svg")}
    result = {}
    for index, key in enumerate(formulas):
        rendered = ET.parse(pages[index + 1]).getroot()
        height, depth, width = metrics[index]
        result[key] = (rendered, height * POINT_TO_PIXEL, depth * POINT_TO_PIXEL, width * POINT_TO_PIXEL)
    return result


def replacement(source: str, node: ET.Element, formula: str, rendered: tuple, identifier: str) -> str:
    image, height, depth, width = rendered
    style = text_style(source, node)
    x_position = float(node.get("x", "0"))
    y_position = float(node.get("y", "0"))
    anchor = style.get("text-anchor", "start")
    if anchor == "middle":
        x_position -= width / 2
    elif anchor == "end":
        x_position -= width
    baseline = style.get("dominant-baseline", "alphabetic")
    if baseline in {"middle", "central"}:
        y_position += (height - depth) / 2
    attributes = {
        name: value for name, value in node.attrib.items()
        if name not in {"x", "y", "dx", "dy", "text-anchor", "dominant-baseline"}
    }
    attributes.update({"data-latex": formula, "role": "img", "aria-label": normalize("".join(node.itertext()))})
    attributes["data-original-text"] = ET.tostring(node, encoding="unicode")
    group = ET.Element("g", attributes)
    group.set("style", group.get("style", "") + ";color:" + style.get("fill", "#111827"))
    ET.SubElement(group, "title").text = normalize("".join(node.itertext()))
    nested = ET.SubElement(group, "svg", {
        "x": f"{x_position:.5f}", "y": f"{y_position - height:.5f}",
        "width": f"{width:.5f}", "height": f"{height + depth:.5f}",
        "viewBox": image.get("viewBox", ""), "overflow": "visible",
    })
    for child in image:
        nested.append(copy.deepcopy(child))
    markup = ET.tostring(group, encoding="unicode")
    markup = re.sub(r'\s+xmlns:ns\d+="[^"]+"', "", markup)
    markup = re.sub(r"ns\d+:", "", markup)
    markup = re.sub(r"\bid=['\"]([^'\"]+)['\"]", lambda match: 'id="' + identifier + "-" + match.group(1) + '"', markup)
    markup = re.sub(r"\bhref=['\"]#([^'\"]+)['\"]", lambda match: 'href="#' + identifier + "-" + match.group(1) + '"', markup)
    return markup


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--only", nargs="*")
    arguments = parser.parse_args()
    paths = sorted(STATIC.rglob("*.svg"))
    if arguments.only:
        paths = [path for path in paths if any(value in str(path.relative_to(STATIC)) for value in arguments.only)]
    labels = inventory(paths, restore=not arguments.check)
    if arguments.inventory:
        print(json.dumps(labels, indent=2, ensure_ascii=False))
        return
    manifest = {label: latex_for_label(label) for label in labels}
    if arguments.check:
        pending = [label for label, formula in manifest.items() if formula is not None]
        if pending:
            raise SystemExit("Unformatted math labels:\n" + "\n".join(pending))
        clipping = [issue for path in paths for issue in validate_bounds(path)]
        if clipping:
            raise SystemExit("Clipped math labels:\n" + "\n".join(clipping))
        print(f"Checked {len(paths)} SVG illustrations; mathematical labels are typeset.")
        return
    requests = {}
    for path in paths:
        source = restored_source(path.read_text())
        for match in TEXT_PATTERN.finditer(source):
            for node in segments(source, match.group()):
                label = normalize("".join(node.itertext()))
                if label in manifest and manifest[label] is not None:
                    size = float(re.match(r"[\d.]+", text_style(source, node)["font-size"]).group())
                    requests.setdefault((manifest[label], size), None)
    if not arguments.output_dir:
        raise SystemExit("Provide --output-dir to write converted SVG files.")
    with tempfile.TemporaryDirectory(prefix="optics-latex-") as temporary:
        rendered = render_formulas(list(requests), Path(temporary))
        changed = 0
        label_count = 0
        for path in paths:
            source = restored_source(path.read_text())
            sequence = 0
            def convert(match: re.Match) -> str:
                nonlocal sequence, label_count
                nodes = segments(source, match.group())
                if not nodes:
                    return match.group()
                if not any(normalize("".join(node.itertext())) in manifest and manifest[normalize("".join(node.itertext()))] is not None for node in nodes):
                    return match.group()
                output = []
                for node in nodes:
                    label = normalize("".join(node.itertext()))
                    formula = manifest.get(label)
                    if formula is None:
                        output.append(ET.tostring(node, encoding="unicode"))
                        continue
                    size = float(re.match(r"[\d.]+", text_style(source, node)["font-size"]).group())
                    sequence += 1
                    label_count += 1
                    output.append(replacement(source, node, formula, rendered[(formula, size)], f"math-{sequence}"))
                return "\n".join(output)
            revised = TEXT_PATTERN.sub(convert, source)
            if revised != source:
                destination = arguments.output_dir / path.relative_to(STATIC)
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(revised)
                ET.fromstring(revised)
                changed += 1
        print(f"Typeset {label_count} labels in {changed} SVG illustrations.")


if __name__ == "__main__":
    main()
