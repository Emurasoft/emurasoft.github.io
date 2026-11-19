#!/usr/bin/env sh
# Build one language: Sphinx then the two post-build passes.
# Usage: buildLanguage.sh <language> [builder]
set -e

if [ $# -lt 1 ]; then
    echo "usage: $0 <language> [builder]" >&2
    exit 2
fi

LANGUAGE="$1"
BUILDER="${2:-html}"

PROJECT="$LANGUAGE" sphinx-build -b "$BUILDER" --jobs auto -W --keep-going -n . "_build/$LANGUAGE"
python -I strip_unused_markup.py "_build/$LANGUAGE"
python -I build_sidebar_nav.py "_build/$LANGUAGE"
