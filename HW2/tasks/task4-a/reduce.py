#!/usr/bin/python

import sys

current_total = 0.0
sum_tip_percents = 0.0
current_trips_num = 0
current_key = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t',1)
    total, tip_amount = value.split(',',1)
    total = float(total)
    tip_amount = float(tip_amount)

    if current_key == key:
        #Same vehicle_type as previous line from sys.stdin
        current_total += total
        if total > 0.0:
            sum_tip_percents += tip_amount / total
        current_trips_num += 1

    if (current_key != key and current_key):
        #Different vehicle_type than previous, but there was a previous line read
        if current_total > 0.0:
            tip_percent = sum_tip_percents/current_trips_num*100.0
        else:
            tip_percent = 0.0
        print '%s\t%d,%.2f,%.2f' % (current_key, current_trips_num, current_total, tip_percent)

        #Now reset current_total/sum_tip_percents/current_key
        if total > 0.0:
            sum_tip_percents = tip_amount / total
        else:
            sum_tip_percents = 0
        current_total = total
        current_trips_num = 1
        current_key = key

    if not current_key:
        if total > 0.0:
            sum_tip_percents = tip_amount / total
        else:
            sum_tip_percents = 0
        current_total = total
        current_trips_num = 1
        current_key = key

#Flush last line:
if current_total > 0.0:
    tip_percent = sum_tip_percents/current_trips_num*100.0
else:
    tip_percent = 0.0
print '%s\t%d,%.2f,%.2f' % (current_key, current_trips_num, current_total, tip_percent)
