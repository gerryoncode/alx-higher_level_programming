#!/bin/bash
#Sends a json post requestto a URL passed as the first argument
curl -X POST "$1" -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 33}'
