#!/bin/bash
# Takes in a URL, sends a POST request to passed URL, and display the body of response
curl -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -s "$1"
