$env:PROJECT='en'
sphinx-build --jobs auto -W --keep-going -n . _build/en
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -I strip_reference_classes.py _build/en
