#!/bin/bash

basepath=$1

cat Missing_CORDEX_Data.txt | while read dataset
do
  localpath=${basepath}/${dataset//./\/}
#  echo ${localpath}
  if test -d "${localpath}"
  then
    echo "${dataset} -> found at ${localpath}"
  fi
done
