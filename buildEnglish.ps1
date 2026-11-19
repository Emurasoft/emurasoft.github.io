$env:PROJECT='en'
sphinx-build --jobs auto -W --keep-going -n . _build/en
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -I strip_unused_markup.py _build/en
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -I build_sidebar_nav.py _build/en
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
