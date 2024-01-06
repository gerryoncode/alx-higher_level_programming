#!/bin/bash
#Send a POST request with contents of a file
curl -sX POST "$1" -H "Content-Type: application/json" -d "$(cat "$2")"
