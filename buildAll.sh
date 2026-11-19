#!/usr/bin/env bash
BUILDER="${1:-html}"
parallel --verbose "PROJECT={} sphinx-build -b $BUILDER --jobs auto -W --keep-going -n . _build/{} && python -I strip_unused_markup.py _build/{} && python -I build_sidebar_nav.py _build/{}" ::: en ja ko zh-cn zh-tw
