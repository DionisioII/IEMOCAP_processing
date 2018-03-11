#!/bin/bash
FILES=averaged_output_NaN_Removed/*
for f in $FILES
do
  python3 unify_csv.py $f
    
done