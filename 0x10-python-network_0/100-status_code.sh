#!/bin/bash
#takes in a URL and displays only the response code
curl -o /dev/null -sw "%{http_code}" "$1"
