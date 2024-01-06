#!/bin/bash
#Senda get request with a header variable
curl -sLH 'X-School-User-Id:98' "$1"
