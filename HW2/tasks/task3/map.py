#!/usr/bin/python

import sys
import StringIO
import csv

for line in sys.stdin:
    # If line has 16 features, license data
    # medallion = 0

    # If line has 20 features (noting tab sep between key/val), joined data
    # medallion = 0


    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file, quotechar='"')
    for record in csv_reader:
        if len(record) == 16:
            key = record[0]
            value = ['license'] + record[1:]

        if len(record) == 20:
            key = record[0]
            value = ['joindat']
            for field in record[1:]:
                value.extend(field.split('\t'))

        if key != 'medallion':
            string_for_value = StringIO.StringIO()
            value_string = csv.writer(string_for_value, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            value_string.writerow(value)
            value = string_for_value.getvalue().strip('\r\n')
            print '%s\t%s' % (key, value)
