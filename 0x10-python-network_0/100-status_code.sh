#!/bin/bash
# Script that sends request to a URL the response status code
curl -so /dev/null -w "%{http_code}" "$1"
