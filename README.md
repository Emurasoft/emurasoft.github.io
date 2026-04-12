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
