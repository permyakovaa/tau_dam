#!/bin/bash

cd /code

# Read the environment variables file line by line
while IFS= read -r line; do
  # Check if the line is empty or starts with #
  if [[ -n "$line" && ! "$line" =~ ^#.* ]]; then
    # Split the line into variable name and value
    var_name="${line%%=*}"
    var_value="${line#*=}"
    # Set the environment variable
    export "$var_name"="$var_value"
  fi
done < env_list.txt

# Execute the desired command
python3 manage.py compress_previews 100