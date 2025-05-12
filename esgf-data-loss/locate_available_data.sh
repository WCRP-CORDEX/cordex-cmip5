#!/bin/bash

basepath="$1"
missing_data_url="https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip5/refs/heads/main/esgf-data-loss/Missing_CORDEX_Data.txt"

if [ -z "$basepath" ]; then
  echo "Usage: $0 /path/to/local/cordex/data"
  exit 1
fi

curl -fsSL "$missing_data_url" | while read dataset
do
  localpath=${basepath}/${dataset//./\/}
  if test -d "${localpath}"
  then
    echo "${dataset} -> found at ${localpath}"
  fi
done
