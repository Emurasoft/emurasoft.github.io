#!/usr/bin/env bash
pids=()
PROJECT='en' sphinx-build . _build/en & pids+=($!)
PROJECT='ja' sphinx-build . _build/ja & pids+=($!)
PROJECT='ko' sphinx-build . _build/ko & pids+=($!)
PROJECT='zh-cn' sphinx-build . _build/zh-cn & pids+=($!)
PROJECT='zh-tw' sphinx-build . _build/zh-tw & pids+=($!)

error=false
for pid in ${pids[*]}; do
    if ! wait $pid; then
        error=true
    fi
done

if error; then
    echo "Error occurred"
    exit 1
fi