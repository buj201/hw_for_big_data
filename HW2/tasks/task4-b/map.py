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
    csv_reader = csv.reader(csv_file, delimiter=',')
    for record in csv_reader:
        agent_name =  record[-6] #Index of agent_name
        fare_amount = record[14] #Index of fare_amount
        surcharge = record[15] #Index of surcharge
        tip_amount = record[17] #Index of tip_amount
        total = float(fare_amount) + float(surcharge) + float(tip_amount)

        print '%s\t%.2f' % (agent_name,total)
