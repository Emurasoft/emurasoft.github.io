#!/usr/bin/env bash
parallel --verbose 'PROJECT={} sphinx-build . _build/{}' ::: en ja ko zh-cn zh-tw