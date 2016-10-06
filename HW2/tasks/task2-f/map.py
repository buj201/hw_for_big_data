#!/usr/bin/python

import sys

for line in sys.stdin:
    key, val = line.split('\t',1)
    key = key.strip().split(',')
    medallion = key[0] #Index of medallion in natural join
    license = key[1] #Index of license in natural join

    print '%s\t%s' % (license, medallion)
