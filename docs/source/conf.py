import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "Optics Engineering"
author = "Optics Engineering contributors"
copyright = "2026, Optics Engineering contributors"

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "jupyterlite_sphinx",
    "worked_solution_toggle",
    "formula_plotter",
]
exclude_patterns = [
    "_contents/**",
    "worked_exercises/photonics_essentials/notebooks/*.ipynb",
]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "sticky_navigation": False,
    "titles_only": True,
    "version_selector": False,
    "language_selector": False,
    "logo_only": False,
}
html_logo = "_static/logo.svg"
html_favicon = "_static/logo.svg"
html_title = project
html_short_title = project
templates_path = ["_templates"]
html_context = {
    "docs_description": (
        "Optical engineering references, worked textbook solutions, "
        "and interactive tools for understanding and designing optical systems."
    ),
}
html_show_sphinx = False
pygments_style = "friendly"
html_baseurl = "https://optics.engineering/"
html_static_path = ["_static"]
html_css_files = [
    "modern.css",
    "knowledge_base/worked_exercises/photonics_essentials/photodiode_lab.css",
    "custom.css",
]
html_js_files = [
    ("theme-ui.js", {"defer": "defer"}),
    "knowledge_base/worked_exercises/photonics_essentials/photodiode_lab.js"
]

jupyterlite_contents = [
    "_notebook_support/photodiode.py",
    (
        "worked_exercises/photonics_essentials/"
        "notebooks/*.ipynb"
    ),
]
jupyterlite_new_tab_button_text = "Open the live Python notebook"
notebooklite_new_tab_button_text = "Open the live Python notebook"
