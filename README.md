# emeditor-help

Sphinx project for [https://www.emeditor.org/](https://www.emeditor.org/).

# Build instructions

1. Requires Python. Install dependencies with `pip install -r requirements.txt`.
2. Set the `PROJECT` variable to the language to build, then build the pages with `sphinx-build`. In PowerShell, the command is:

```
$env:PROJECT='en'
sphinx-build . _build/en
```