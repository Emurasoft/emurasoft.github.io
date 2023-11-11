# EmEditor Help

Sphinx project for [https://www.emeditor.org/](https://www.emeditor.org/).

# Build instructions

1. Install Python, then clone this repo.
2. `cd` to your local folder of the repo, and run `pip install -r requirements.txt` to get all dependencies.
3. Set the `PROJECT` variable to the language to build, then build the pages with `sphinx-build`. In PowerShell, the command is:

```
$env:PROJECT='en'
sphinx-build . _build/en
```