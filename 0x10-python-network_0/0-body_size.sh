#!/bin/bash
# use curl to send a request to a url and get the size of the response in bytes
[ $# -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; url="$1"; echo "$(curl -s "$url" | wc -c)"
