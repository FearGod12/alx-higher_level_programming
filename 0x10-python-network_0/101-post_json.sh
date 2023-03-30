#!/bin/bash
#takes in a URL and posts a json data in a json fikle
curl -sX POST -d @"$2" -H "Content-Type: application/json" "$1"
