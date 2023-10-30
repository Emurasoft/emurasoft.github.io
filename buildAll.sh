#!/usr/bin/env bash
parallel --verbose 'PROJECT={} sphinx-build -v --jobs auto -W --keep-going -n . _build/{}' ::: en ja ko zh-cn zh-tw