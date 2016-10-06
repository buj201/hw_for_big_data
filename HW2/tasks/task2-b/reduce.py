#!/usr/bin/python

import sys

current_count = 0

for line in sys.stdin:

    key = int(line.strip())

    current_count += key

#Flush after last line:
print current_count
