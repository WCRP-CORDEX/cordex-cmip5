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
  # jf: dirty trick for directory tree with INST-MODEL vs just MODEL
  # Uncomment one at a time
  #localpath=$(ls -d ${localpath//p1\//p1\/\*-} 2> /dev/null || continue)
  #localpath=$(ls -d ${localpath//p0\//p0\/\*-} 2> /dev/null || continue)
  if test -d "${localpath}"
  then
    echo "${dataset} -> found at ${localpath}"
  fi
done
