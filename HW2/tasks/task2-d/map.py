#!/usr/bin/python

import sys

for line in sys.stdin:
    key, val = line.split('\t', 1)
    key = key.strip().split(',')
    val = val.strip().split(',')
    fare_amount = val[11] #Index of fare_amount in natural join
    surcharge = val[12] #Index of surcharge in natural join of fares and trips
    tip_amount = val[14] #Index of tip_amount in natural join of fares and trips
    total = float(fare_amount)+float(surcharge)+float(tip_amount)

    tolls_amount = float(val[15]) #Index of tolls_amount in natural join of fares and trips
    date = key[3].split(' ')[0]

    print '%s\t%s,%.2f' % (date, total, tolls_amount)
