#!/usr/bin/env bash
parallel --verbose 'PROJECT={} sphinx-build -v --jobs auto -W --keep-going -n . _build/{} && python -I strip_reference_classes.py _build/{} && python -I build_sidebar_nav.py _build/{}' ::: en ja ko zh-cn zh-tw
