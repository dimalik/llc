#!/usr/bin/env python
import os
import sys
import csv

story = "/Users/andrewcaines/Corpora/DundeeCorpus/tx01wrdp.dat"
=[]
ages=[]
with open('data.csv','r') as f:
    next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')
    for name,age in reader:
        names.append(name)
        ages.append(age) 


for line in story:
    
