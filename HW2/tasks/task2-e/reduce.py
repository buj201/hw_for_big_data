#!/usr/bin/python

import sys

current_medallion = None
current_date = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t',1)
    medallion, date = key.split(',',1)

    if current_date == date and current_medallion == medallion:
        #Same date and medallion as previous line from sys.stdin
        num_trips += 1

    elif current_medallion == medallion and current_date != date:
        #Same taxi but new date
        current_date = date
        num_trips += 1
        num_days += 1.0

    elif not current_medallion and not current_date:
        #First line read in from sys.stdin, so current_date = None
        current_date = date
        current_medallion = medallion
        num_days = 1.0
        num_trips = 1

    elif current_medallion != medallion and current_date:
        #First time seeing new taxi, so flush
        avg_trips_day = num_trips / num_days
        print '%s\t%d,%.2f' % (current_medallion, num_trips, avg_trips_day)
        current_date = date
        current_medallion = medallion
        num_days = 1.0
        num_trips = 1

#Flush after last line:
avg_trips_day = num_trips / num_days
print '%s\t%d,%.2f' % (current_medallion, num_trips, avg_trips_day)
