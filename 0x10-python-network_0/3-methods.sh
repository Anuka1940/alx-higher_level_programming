#!/bin/bash
#takes in a URL and display all the HTTP methods that the server will accept
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
