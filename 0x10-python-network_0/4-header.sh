#!/bin/bash
# Takes in a URL as an argument, send a GET request to URL and displays the body of the response
curl -H "X-School-User-Id: 98" -s "$1"
