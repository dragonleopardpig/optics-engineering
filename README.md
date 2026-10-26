# Optics Engineering

A standalone Sphinx documentation site with a Knowledge Base, Worked Exercise
Solutions, and interactive tools.
The Manual and Tutorials sections and their image collections are omitted.
The site builds independently and does not link to the private source repository.

The SVG logo shows a converging lens and a diverging lens with ray paths
and plane and spherical wavefronts.

Published site: <https://optics.engineering/>.
Source repository: <https://github.com/dragonleopardpig/optics-engineering>.

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
module is included in `docs/source/_notebook_support/photodiode.py`, so building this
site does not require the original simulator checkout or its dependencies.
The first build needs internet access for the JupyterLite runtime assets;
the notebook also needs internet access to load its Pyodide kernel/packages.

## Publish on GitHub Pages

GitHub Pages is configured for this repository with **GitHub Actions** as
the publishing source. Push changes to `main` or `master` to deploy, or run
**Actions → Build and deploy documentation** manually.

The workflow builds the site and deploys `docs/build/html`. Pull requests
do not trigger this workflow, so fork contributions do not automatically
execute on the self-hosted machine. Review their changes before merging.
The published URL appears in
the deployment and the repository's Pages settings. Project sites under a
repository path are supported; no hard-coded domain or repository name is
needed. Sphinx generates `.nojekyll` to preserve underscore-prefixed assets.
The canonical site URL is set by `html_baseurl` in `docs/source/conf.py`.

See [GitHub's custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
for Pages configuration.

### Local runner and pre-push checks

Both build and deployment jobs require a self-hosted Linux x64 runner with
the `thinky-local` label; neither job falls back to a GitHub-hosted runner.
On the development workstation, start the existing rootless Ubuntu runner
before pushing:

```bash
gh-runner start optics-engineering
python -m sphinx -W --keep-going -b html -d docs/build/doctrees docs/source docs/build/html
python tools/typeset_svg_math.py --check
git push origin main
```

Activate the documentation virtual environment first, as in the build
instructions. After a source-directory move, add `-E` to the Sphinx command
once to discard cached document paths. The runner runs in an isolated,
one-job container and is replaced between build and deployment. Keep the
workstation awake and the runner online until both jobs finish; otherwise
the workflow waits for a matching runner. Check it with `gh-runner status`
and stop it when no jobs are running with `gh-runner stop optics-engineering`.

## Custom domain

The repository's **Settings → Pages → Custom domain** is `optics.engineering`.
The domain's DNS already contains the following GitHub Pages records:

| Type | Name | Value |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `dragonleopardpig.github.io` |

Keep these records at your DNS provider. The `www` record points to the
account's GitHub Pages hostname, without a repository path. GitHub handles
the redirect between the `www` hostname and the apex domain. Enable
**Enforce HTTPS** in the repository's Pages settings after the certificate
is available. DNS changes and certificate issuance can take up to 24 hours.

To verify domain ownership, open your GitHub account's **Settings → Pages**,
add `optics.engineering`, and add the TXT record GitHub supplies to your DNS.
The TXT record name is `_github-pages-challenge-dragonleopardpig`; keep the
record after verification.

See [GitHub's custom domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## Editing and provenance

Edit the site title and build settings in `docs/source/conf.py`, the landing
page/navigation in `docs/source/index.rst`, and the logo in
`docs/source/_static/logo.svg`. Content and existing illustrations remain in
`docs/source/knowledge_base` and `docs/source/_static`.

Adapted from existing optics documentation on 2026-10-18. The site credits its
documentation contributors and retains the GPL-3.0 license in `LICENSE.txt`.
Examples use self-contained calculations and the bundled notebook module.
