#!/usr/bin/env bash
# Get size of content

# Get the URL from the first argument
url="$1"

# Use curl to get the response header size
header_size=$(curl -sI "$url" -w "%{size_header}\n" -o /dev/null)

# Use curl to download the response body and get its size
body_size=$(curl -s "$url" -o /dev/null | wc -c)

# Calculate total response size
total_size=$((header_size + body_size))

# Display the total size in bytes
echo "$total_size"
