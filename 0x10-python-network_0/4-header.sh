#!/bin/bash
#Senda get request with a header variable
curl -sLX GET -H 'X-School-User-Id: 98' "$1"
