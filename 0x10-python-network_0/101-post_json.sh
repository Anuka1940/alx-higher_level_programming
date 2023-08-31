#!/bin/bash
# Send a POST request with the content of a file passed with the filename as the second argument of the scrip
$(curl -X POST -H "Content-Type: application/json" -d "$2" -s "$1")
