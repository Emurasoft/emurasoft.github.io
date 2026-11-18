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

# Deployment

The help site is also deployed to Cloudflare Workers as static assets by `.github/workflows/deploy-workers.yml`. The workflow builds all languages, assembles `help_pages/` from `_build/` with `_add_to_build/` copied over it, removes the Sphinx `.doctrees` directories, and runs `wrangler deploy` using `wrangler.jsonc`.

The deploy requires the repository secrets `CLOUDFLARE_API_TOKEN` (Workers Scripts: Edit and Account Settings: Read) and `CLOUDFLARE_ACCOUNT_ID`.

Every push except tag `0.0.0` deploys, so a branch push can be used to test the deploy. Until the domain moves, the Worker is served at https://emeditor-help.makoto-679.workers.dev and https://help.emeditor.com/ still serves the GitHub Pages deployment.
