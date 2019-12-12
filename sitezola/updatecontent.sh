#!/bin/bash
cd content

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for f in *
do
  echo "$f"
  echo -e "+++
title = \"${f%%.*}\"
date = 2019-12-12
+++

$(tail -n +2 ${f})" > $f
done
IFS=$SAVEIFS

cd -