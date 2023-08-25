#!/usr/bin/env bash
parallel --verbose 'PROJECT={} sphinx-build -v --jobs auto . _build/{}' ::: en ja ko zh-cn zh-tw