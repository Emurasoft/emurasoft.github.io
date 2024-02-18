#!/usr/bin/env bash

# Build all projects in parallel. Ignore error.
exit_code=0
(parallel --verbose 'PROJECT={} sphinx-build -v --jobs auto -W --keep-going -n . _build/{}' ::: en ja ko zh-cn zh-tw | tee output.txt) || exit_code=$?

# Output error messages
cat output.txt | grep 'WARNING:\|ERROR:'

# Exit with exit code from build
exit "$exit_code"