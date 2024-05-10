#!/bin/bash
# Get size of content
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
