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

The deploy requires the repository secrets `CLOUDFLARE_API_TOKEN` (Workers Scripts: Edit, Workers Routes: Edit, and Account Settings: Read) and `CLOUDFLARE_ACCOUNT_ID`.

Every push except tag `0.0.0` deploys, so a branch push can be used to test the deploy. The Worker attaches `help.emeditor.com` as a Custom Domain through the `routes` entry in `wrangler.jsonc`, so the site is served at that hostname and at https://emeditor-help.makoto-679.workers.dev.

Before the first deploy that attaches the custom domain, delete the existing `help.emeditor.com` CNAME record (which points to `emurasoft.github.io`) in the `emeditor.com` zone. Cloudflare refuses to create a Custom Domain while a CNAME exists for the hostname; it creates the DNS record and certificate itself.
