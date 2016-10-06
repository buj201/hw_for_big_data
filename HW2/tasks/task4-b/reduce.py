#!/usr/bin/python

import sys

current_total = 0.0
current_key = None
agents_and_revs = {}

for line in sys.stdin:

    line = line.strip()
    key, total = line.split('\t',1)
    total = float(total)

    if current_key == key:
        #Same agent_name as previous line from sys.stdin
        current_total += total

    if (current_key != key and current_key):
        #Different agent_name than previous, but there was a previous line read
        agents_and_revs[current_key] = current_total

        #Now reset current_total/current_tips/current_key
        current_total = total
        current_key = key

    if not current_key:
        current_total = total
        current_key = key

#Flush last line:
agents_and_revs[current_key] = current_total

#Get order:
ranked_agents_and_revs = sorted(agents_and_revs.items(), key=lambda x:x[1], reverse=True)

for i in range(20):
    if i < len(ranked_agents_and_revs):
        print '%s\t%.2f' % (ranked_agents_and_revs[i][0], ranked_agents_and_revs[i][1])
