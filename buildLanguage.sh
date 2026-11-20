#!/usr/bin/env sh
# Build one language, or all of them with "all": Sphinx then the two post-build passes.
# Usage: buildLanguage.sh <language|all> [builder]
set -e

if [ $# -lt 1 ]; then
    echo "usage: $0 <language|all> [builder]" >&2
    exit 2
fi

LANGUAGE="$1"
BUILDER="${2:-html}"

if [ "$LANGUAGE" = "all" ]; then
    parallel --verbose sh "$0" {} "$BUILDER" ::: en ja ko zh-cn zh-tw
    exit
fi

PROJECT="$LANGUAGE" sphinx-build -b "$BUILDER" --jobs auto -W --keep-going -n . "_build/$LANGUAGE"
python -I strip_unused_markup.py "_build/$LANGUAGE"
python -I build_sidebar_nav.py "_build/$LANGUAGE"
