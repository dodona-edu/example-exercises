#!/bin/sh
# Every language copy of tested/input-output must keep the evaluation/ directory of the Python original.
status=0

for copy in tested/*/input-output/evaluation; do
    [ -d "$copy" ] || continue
    if ! diff -r tested/input-output/evaluation "$copy"; then
        echo "::error::$copy differs from tested/input-output/evaluation"
        status=1
    fi
done

exit $status
