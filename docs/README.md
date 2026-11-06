# Optics Engineering documentation sources

Build and publishing instructions are in the [project README](../README.md).

- `source/conf.py`: Sphinx configuration and site title.
- `source/index.rst`: landing page and navigation.
- `source/knowledge_base/`: references, interactive tools, and worked exercises.
- `source/_static/`: logo, illustrations, CSS, JavaScript, and vendored libraries.
- `source/_templates/`: modern Read the Docs layout, optics homepage, and logo markup.
- `source/_static/modern.css`: shared light/dark design and responsive navigation.
- `source/_static/custom.css`: optics branding, equations, and interactive component styling.
- `source/_static/theme-ui.js`: appearance controls, mobile menu, search shortcut, and code copying.
- `source/_ext/`: worked-solution and formula-plotter Sphinx extensions.
- `source/_notebook_support/photodiode.py`: module bundled with JupyterLite.
- `source/knowledge_base/worked_exercises/photonics_essentials/notebooks/`:
  browser-based Python lab.

The checked-in figures and RST pages are sufficient for a normal Sphinx build.
Local figure generators, numerical models, and simulator design notes outside
`source/` are excluded from the publication repository. They are not needed
to build or publish the site.

Mathematical labels in the illustrations are rendered from LaTeX to embedded
SVG paths. Their fractions, roots, matrices, and subscripts do not depend on
browser fonts or JavaScript. The ordinary Sphinx build uses the checked-in
assets and does not need a TeX installation.

To regenerate the labels, install LaTeX with `amsmath`, `amssymb`, and `preview`,
plus `dvisvgm`, then run from the repository root:

```bash
python tools/typeset_svg_math.py --output-dir docs/source/_static
python tools/typeset_svg_math.py --check
```

Formula transcriptions are maintained in `tools/svg_math_labels.py`. Each
generated label retains its original text for accessibility and regeneration.
The check audits all SVG illustrations for unformatted math and clipped labels;
it does not need LaTeX and runs in the deployment workflow.

The modern layout is adapted from the Aster Sphinx starter. Its MIT notice is
retained in `source/_static/THEME-LICENSE.txt`. Self-hosted DM Sans and JetBrains
Mono retain their SIL Open Font Licenses in `source/_static/fonts/`.
The project continues to use the license in `../LICENSE.txt`.
