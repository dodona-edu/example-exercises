#!/usr/bin/env bash

if [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Age: $1"
else
    echo "invalid age" >&2
    exit 1
fi
