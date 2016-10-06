#!/usr/bin/python

import sys

for line in sys.stdin:
    key, val = line.split('\t',1)
    val = val.strip().split(',')
    passenger_count = val[3] #Index of passenger count in natural join of fares and trips
    print '%d\t1' %(int(passenger_count))
