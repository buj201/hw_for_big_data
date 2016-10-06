#!/usr/bin/python

import sys

for line in sys.stdin:
    key, val = line.split('\t',1)
    val = val.strip().split(',')
    key = key.strip().split(',')
    medallion = key[0] #Index of medallion in natural join
    date = key[3].split(' ')[0] #Index of datetime, taking only date

    print '%s,%s\t1' % (medallion, date)
