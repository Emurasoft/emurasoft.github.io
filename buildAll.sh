#!/usr/bin/env bash
parallel 'PROJECT={} sphinx-build . _build/{}' ::: en ja ko zh-cn zh-tw