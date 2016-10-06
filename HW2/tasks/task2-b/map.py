#!/usr/bin/python

import sys

for line in sys.stdin:

    key, val = line.strip().split('\t',1)
    val = val.split(',')
    fare = float(val[-1]) #Index of total in natural join of fares and trips
    if fare <= 10:
        print '1'
