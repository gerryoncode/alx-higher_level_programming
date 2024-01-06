#!/bin/bash
#Sends a request to a URL passed as an argument
curl -sI "$1" | grep "HTTP/1.1" | cut -d' ' -f2
