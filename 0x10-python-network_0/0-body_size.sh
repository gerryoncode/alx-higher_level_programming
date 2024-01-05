#!/bin/bash
# Takes in a url, seneds a request to that uRL and displays the size
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2

