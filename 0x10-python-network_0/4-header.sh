#!/bin/bash
# sends a get request with a header variable  
curl -sX GET -H "X-School-User-Id: 98" "$1"
