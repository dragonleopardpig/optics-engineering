# Optics Engineering

A standalone Sphinx documentation site with a Knowledge Base, Worked Exercise
Solutions, interactive tools, and an optics development roadmap.
The Manual and Tutorials sections and their image collections are omitted.
The site builds independently and does not link to the private source repository.

The SVG logo shows two lenses, ray paths, and plane and spherical wavefronts.

## Build and preview

Use Python 3.12 or later. From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/requirements.txt
python -m sphinx -W --keep-going -b html -d docs/build/doctrees docs/source docs/build/html
python -m http.server 8000 --directory docs/build/html
```

Open <http://localhost:8000>. Alternatively, run `make -C docs html` after
installing the dependencies. On Windows, use `.venv\Scripts\activate` and
`docs\make.bat html`.

The JupyterLite notebook runs Python entirely in the browser. Its photodiode
module is included in `docs/source/_contents/photodiode.py`, so building this
site does not require the original simulator checkout or its dependencies.
The first build needs internet access for the JupyterLite runtime assets;
the notebook also needs internet access to load its Pyodide kernel/packages.

## Publish on GitHub Pages

1. Create a GitHub repository and push this folder to its `main` or `master` branch.
2. In the repository, open **Settings → Pages → Build and deployment** and
   select **GitHub Actions** as the source.
3. Open **Actions → Build and deploy documentation** and run the workflow,
   or push another commit to trigger it.

The workflow builds the site and deploys `docs/build/html`. Pull requests
build the documentation without deploying. The published URL appears in
the deployment and the repository's Pages settings. Project sites under a
repository path are supported; no hard-coded domain or repository name is
needed. Sphinx generates `.nojekyll` to preserve underscore-prefixed assets.

See [GitHub's custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
for Pages configuration.

## Editing and provenance

Edit the site title and build settings in `docs/source/conf.py`, the landing
page/navigation in `docs/source/index.rst`, and the logo in
`docs/source/_static/logo.svg`. Content and existing illustrations remain in
`docs/source/knowledge_base`, `docs/source/future_plan`, and `docs/source/_static`.

Adapted from the local KrakenOS documentation on 2026-10-18. The original
contributor attribution and GPL-3.0 license are retained in the site and
`LICENSE.txt`. Software names in code examples retain their original spelling.
