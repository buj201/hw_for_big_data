#!/usr/bin/python

import sys
import csv
import StringIO
import re

for line in sys.stdin:
    # If line has 16 features, license data
    # medallion = 0

    # If line has 21 features, joined data
    # medallion = 0

    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file, delimiter=',') ##ignore tab
    for record in csv_reader:
        vehicle_type =  record[25] #Vehicle type
        fare_amount = record[14] #Index of fare_amount
        surcharge = record[15] #Index of surcharge
        tip_amount = float(record[17]) #Index of tip_amount
        total = float(fare_amount) + float(surcharge) + float(tip_amount)

        print '%s\t%.2f,%.2f' % (vehicle_type,total, tip_amount)
