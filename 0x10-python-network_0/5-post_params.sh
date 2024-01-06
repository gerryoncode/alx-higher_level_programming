#!/bin/bash
#Sends a post request passed url and displays the body of a response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
