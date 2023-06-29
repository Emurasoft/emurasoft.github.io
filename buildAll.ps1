$env:PROJECT='en'
sphinx-build . _build/en
$env:PROJECT='ja'
sphinx-build . _build/ja
$env:PROJECT='ko'
sphinx-build . _build/ko
$env:PROJECT='zh-cn'
sphinx-build . _build/zh-cn
$env:PROJECT='zh-tw'
sphinx-build . _build/zh-tw