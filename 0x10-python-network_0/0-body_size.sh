#!/bin/bash
# use curl to send a request to a url and get the size of the response in bytes

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
url="$1"
response=$(curl -s "$url")
content_length=$(echo -n "$response" | wc -c)

if [ -n "$content_length" ]; then
	echo "$content_length"
else
	echo "Unable to retrieve content length"
fi
