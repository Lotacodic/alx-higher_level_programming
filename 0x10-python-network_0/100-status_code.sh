#!/bin/bash
# displays only the status code of the response. no pipe
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
