#!/bin/bash
# Send a GET request to the URL and displays the body of the response
curl -s -w "%{http_code}" -X GET "$1" | grep '.*200' | rev | cut -c 4- | rev
