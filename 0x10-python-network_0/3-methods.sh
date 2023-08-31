#!/bin/bash
#takes in a URL and display all the HTTP methods that the server will accept
curl -X OPTIONS -i -s "$1" | awk '/Allow:/ {print $2}'
