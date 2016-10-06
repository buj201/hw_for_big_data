#!/usr/bin/python

import sys

current_date = None

for line in sys.stdin:

    line = line.strip()
    date, value = line.split('\t',1)
    total, tolls_amount = value.split(',',1)

    if current_date == date:
        #Same date as previous line from sys.stdin
        current_tolls += float(tolls_amount)
        current_total += float(total)

    if (current_date != date and current_date):
        #Different date than previous, but there was a previous line read
        #Should join and flush
        print '%s\t%.2f,%.2f' % (current_date, current_total, current_tolls)
        current_date = date
        current_tolls = float(tolls_amount)
        current_total = float(total)

    if not current_date:
        #First line read in from sys.stdin, so current_date = None
        current_date = date
        current_tolls = float(tolls_amount)
        current_total = float(total)

#Flush after last line:
print '%s\t%.2f,%.2f' % (current_date, current_total, current_tolls)
