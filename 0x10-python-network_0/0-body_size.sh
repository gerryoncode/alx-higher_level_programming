#!/usr/bin/bash
# Prints the content length in bytes
curl -Is "$1" | grep "Content-Length" | cut -f2 -d" "

