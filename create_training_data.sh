#!/bin/bash
FILES=mocapfiles/*
for f in $FILES
do
  python3 training-generator.py $f
    
done
