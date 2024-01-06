#!/bin/bash
# Send a GET request to the URL and displays the body of the response
curl -sL -X GET -w "%{http_code}" "$1" | grep -z '.*200$' | rev | cut -z -c 4- | rev
