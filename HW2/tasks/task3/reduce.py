#!/usr/bin/python

import sys

licenses = []
joined_recs = []
current_key = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t',1)
    relation = value[0:7]
    other_features = value[8:].split(',')

    if current_key == key:
        #Same key as previous line from sys.stdin
        if relation == 'license':
            licenses.append(other_features)
        elif relation == 'joindat':
            joined_recs.append(other_features)

    if (current_key != key and current_key):
        #Different key than previous, but there was a previous line read
        #Should join and flush licenses/joined_recs
        if (len(licenses)>0 and len(joined_recs) > 0):
            #Might have misentered data, so no matches by key
            for joined_rec in joined_recs:
                for license in licenses:
                    print current_key + '\t' + ','.join(joined_rec) + ',' + ','.join(license)

        #Now reset licenses/joined_recs/current_key
        joined_recs = []
        licenses = []
        current_key = key
        if relation == 'license':
            licenses.append(other_features)
        elif relation == 'joindat':
            joined_recs.append(other_features)

    if not current_key:
        #First line read in from sys.stdin, so current_key = None
        if relation == 'license':
            licenses = [other_features]
        elif relation == 'joindat':
            joined_recs = [other_features]
        current_key = key

#Flush last line:

if (len(licenses)>0 and len(joined_recs) > 0):
    #Might have misentered data, so no matches by key
    for joined_rec in joined_recs:
        for license in licenses:
            print current_key + '\t' + ','.join(joined_rec) + ',' + ','.join(license)
