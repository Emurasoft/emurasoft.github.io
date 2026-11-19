#!/usr/bin/env bash
BUILDER="${1:-html}"
export BUILDER
parallel --verbose 'sh ./buildLanguage.sh {} "$BUILDER"' ::: en ja ko zh-cn zh-tw
