# Optics Engineering documentation sources

Build and publishing instructions are in the [project README](../README.md).

- `source/conf.py`: Sphinx configuration and site title.
- `source/index.rst`: landing page and navigation.
- `source/knowledge_base/`: references, interactive tools, and worked exercises.
- `source/future_plan/`: retained optics development roadmap.
- `source/_static/`: logo, illustrations, CSS, JavaScript, and vendored libraries.
- `source/_ext/`: worked-solution and formula-plotter Sphinx extensions.
- `source/_contents/photodiode.py`: standalone module bundled with JupyterLite.
- `source/knowledge_base/worked_exercises/photonics_essentials/notebooks/`:
  browser-based Python lab.

The checked-in figures and RST pages are sufficient for a normal Sphinx build.
Local figure generators, numerical models, and simulator design notes outside
`source/` are excluded from the publication repository. They are not needed
to build or publish the site.
