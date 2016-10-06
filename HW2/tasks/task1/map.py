#!/usr/bin/python

import sys

for line in sys.stdin:
    # If line has 11 features, fares data
    # medallion = 0 , hack_license = 1, vendor_id = 2, pickup_datetime = 3

    # If line has 14 features, trips data
    # medallion = 0 , hack_license = 1, vendor_id = 2, pickup_datetime = 5

    line = line.strip()
    line =  line.split(',')
    if len(line) == 11:
        key = line[0:4]
        value = ['Fare'] + line[4:]

    if len(line) == 14:
        key = [line[0], line[1], line[2], line[5]]
        value = ['Trip'] + line[3:5] + line[6:]

    if key != ['medallion', 'hack_license', 'vendor_id', 'pickup_datetime']:
        print ','.join(key) + '\t' + ','.join(value)
