#!/bin/bash
url=$1
header="X-HolbertonSchool-User-Id: 98"
response=$(curl -s -H "$header" "$url")
echo "$response"
