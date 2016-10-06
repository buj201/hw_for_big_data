#!/usr/bin/python

import sys

current_medallion = None
current_license = None

for line in sys.stdin:

    line = line.strip()
    license, medallion = line.split('\t',1)

    if current_license == license and current_medallion != medallion:
        #same driver, different car. Note num_meds must have already
        #been initialized to have current_license == license.
        num_meds += 1

    if current_license != license and current_license:
        #New driver, but not first line
        print '%s\t%d' % (current_license, num_meds)
        current_license = license
        current_medallion = medallion
        num_meds = 1

    if not current_license:
        #First line
        current_license = license
        current_medallion = medallion
        num_meds = 1

#Flush after last line:
print '%s\t%d' % (current_license, num_meds)
