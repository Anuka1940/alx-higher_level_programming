#!/bin/bash
# Send a request to URL and display only the status code response
curl -o /dev/null -s -w "%{http_code}" "$1"
