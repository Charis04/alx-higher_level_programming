#!/bin/bash
# Get size of content
echo "$(curl -s "$1" -o /dev/null | wc -c)"
