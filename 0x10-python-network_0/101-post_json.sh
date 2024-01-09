#!/bin/bash
# Script that sends a JSON POST request to a URL  and displays the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
