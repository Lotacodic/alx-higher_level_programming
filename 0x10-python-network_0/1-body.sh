#!/bin/bash
# Display only body of a 200 status code response
VAR=$(curl -so /dev/null -I -w "%{http_code}" "$1");

if [ "$VAR" == 200 ]; then
    curl -sL "$1"
fi
