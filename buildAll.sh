#!/usr/bin/env bash
PROJECT='en' sphinx-build . _build/en
PROJECT='ja' sphinx-build . _build/ja
PROJECT='ko' sphinx-build . _build/ko
PROJECT='zh-cn' sphinx-build . _build/zh-cn
PROJECT='zh-tw' sphinx-build . _build/zh-tw