#!/usr/bin/python

import sys

for line in sys.stdin:
    old_key, val = line.split('\t',1)
    val = val.strip().split(',')
    fare = float(val[11]) #Index of fare in natural join of fares and trips
    by_four = int(fare/4.0)
    if fare <= 4.00:
        key = str("0,4")
    elif fare <= 48 and fare % 4 != 0.0:
        key = str(4.0*by_four+0.01) + ',' + str(4*by_four+4)
    elif fare <= 48 and fare % 4 == 0.0:
        key = str(4.0*(by_four-1)+0.01) + ',' + str(4*(by_four-1)+4)
    elif fare >= 48.01:
        key = str(48.01) + ',infinite'

    print '%s\t%d' % (key, 1)
