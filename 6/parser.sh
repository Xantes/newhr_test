#!usr/bin/bash

declare -a values
file=$1

while read -r line; do
    key="$(echo $line | awk -F ',' '{print $1}')"
    ((values[$key]++))
done <$file

echo "${#values[@]}"
