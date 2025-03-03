#!/bin/bash
# Removes 1st and last line from all .json files in current directory.

sed -i '1d' *.json
sed -i '$d' *.json
echo "done"
