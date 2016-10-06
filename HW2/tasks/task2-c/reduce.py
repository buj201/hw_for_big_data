#!/usr/bin/python

import sys

current_count = 0
current_key = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t',1)
    vale = int(value)

    if current_key == key:
        #Same key as previous line from sys.stdin
        current_count += 1

    if (current_key != key and current_key):
        #Different key than previous, but there was a previous line read
        #Should join and flush
         print '%s\t%d' % (current_key,current_count)
         current_key = key
         current_count = 1

    if not current_key:
        #First line read in from sys.stdin, so current_key = None
        current_key = key
        current_count = 1

#Flush after last line:
print '%s\t%d' % (current_key,current_count)
