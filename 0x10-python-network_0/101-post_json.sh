#!/bin/bash
#Send a POST request with contents of a file
curl -X POST "$1" -H "Content-Type: application/json" -d "@$2"
