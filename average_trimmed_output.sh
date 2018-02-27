#!/bin/bash
FILES=trimmed_output/*
for f in $FILES
do
  python3 average_trimmed_output.py $f
    
done
