#!/usr/bin/env bash
parallel --verbose 'PROJECT={} sphinx-build -vvv --jobs auto . _build/{}' ::: en ja ko zh-cn zh-tw