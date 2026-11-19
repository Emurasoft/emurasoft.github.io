# EmEditor Help

Sphinx project for [https://help.emeditor.com/](https://help.emeditor.com/).

# Build instructions

1. Install Python, then clone this repo.
2. `cd` to your local folder of the repo.
3. Optionally, create and activate a new virtual environment (venv).
4. Run `pip install -r requirements.txt` to get all dependencies.
5. Set the `PROJECT` variable to the language to build, then build the pages with `sphinx-build`. In PowerShell, the command is:

```
$env:PROJECT='en'
sphinx-build . _build/en
```

Use `buildEnglish.ps1` (English) or `buildAll.sh` (all languages) for a complete build. They run `sphinx-build` and then two post-build scripts: `strip_unused_markup.py` removes unused attributes and wrapper markup, and `build_sidebar_nav.py` moves the expanded sidebar branch out of every page into `_build/<language>/_static/nav.js`. A bare `sphinx-build` skips both, and because `nav.js` is generated rather than checked in, its pages would load no expanded sidebar branch.

Both scripts take an optional Sphinx builder name and use `html` when none is given. The `servedhtml` builder (registered by `served_html.py`) writes the URLs the deployed site serves, so index pages end with `/` and other pages have no extension. Use it only for the Workers deploy: the local Help archives, the PDFs and the automation test use `html`, whose `.html` links work when the files are opened from disk.

# Deployment

The help site is deployed to Cloudflare Workers as static assets by `.github/workflows/deploy-workers.yml`. The workflow builds all languages with the `servedhtml` builder, assembles `help_pages/` from `_build/` with `_add_to_build/` copied over it, removes the Sphinx `.doctrees` directories, and runs `wrangler deploy` using `wrangler.jsonc`.

`check_served_urls.py help_pages` runs after the built tree is moved to `help_pages/` and before `_add_to_build/` is copied in. It fails the deploy if a page or the sitemap still points at a `.html` URL, which would only reach the visitor through the Worker's redirect.

The deploy requires the repository secrets `CLOUDFLARE_API_TOKEN` (Workers Scripts: Edit, Workers Routes: Edit, and Account Settings: Read) and `CLOUDFLARE_ACCOUNT_ID`.

The workflow runs on pushes to `main`, on tags other than `0.0.0`, and on manual dispatch. Pushes to other branches do not deploy; use `workflow_dispatch` to deploy on demand. The `version` file is written from the ref that triggered the deploy.

The Worker attaches `help.emeditor.com` as a Custom Domain through the `routes` entry in `wrangler.jsonc`, so the site is served at that hostname and at https://emeditor-help.makoto-679.workers.dev. Cloudflare manages the DNS record and certificate for the hostname. A Custom Domain cannot be created while a CNAME exists for the hostname, so if the domain is ever re-pointed, delete the existing DNS record first.

`https://help.emeditor.com/mcp` is served by the separate `emeditor-help-mcp` Worker ([repository](https://github.com/Emurasoft/emeditor-help-mcp)) through its `help.emeditor.com/mcp*` route. Worker routes take precedence over Custom Domains, so `/mcp` never reaches the site Worker and no MCP code is needed here.

GitHub Pages is no longer used for this site. The repository still has a Pages site, which organization sites cannot deactivate, but its custom domain was removed and its deploy job is gone, so it is not updated. The custom domain entry must stay removed so GitHub does not claim `help.emeditor.com`.
