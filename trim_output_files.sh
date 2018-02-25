#!/bin/bash
FILES=output/*
for f in $FILES
do
  python3 trim_csv_output.py $f
    
done
