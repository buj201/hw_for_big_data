#!/usr/bin/python

import sys

fares = []
trips = []
current_key = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t',1)

    if current_key == key:
        #Same key as previous line from sys.stdin
        if value[0:4] == 'Fare':
            fares.append(value[5:])
        elif value[0:4] == 'Trip':
            trips.append(value[5:])

    if (current_key != key and current_key):
        #Different key than previous, but there was a previous line read
        #Should join and flush fares/trips
        if (len(fares)>0 and len(trips) > 0):
            #Might have misentered data, so no matches by key
            for trip in trips:
                for fare in fares:
                    print current_key + '\t' + trip + ',' + fare

        #Now reset fares/trips/current_key
        if value[0:4] == 'Fare':
            fares = [value[5:]]
            trips = []
        elif value[0:4] == 'Trip':
            trips = [value[5:]]
            fares = []
        current_key = key

    if not current_key:
        #First line read in from sys.stdin, so current_key = None
        if value[0:4] == 'Fare':
            fares = [value[5:]]
        elif value[0:4] == 'Trip':
            trips = [value[5:]]
        current_key = key

#Flush last line:

if (len(fares)>0 and len(trips) > 0):
    #Might have misentered data, so no matches by key
    for trip in trips:
        for fare in fares:
            print current_key + '\t' + trip + ',' + fare
