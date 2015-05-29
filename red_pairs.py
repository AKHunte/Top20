#!/usr/bin/env python

#Author: Aisha Hunte
#Date: March 22, 2015

from operator import itemgetter
import sys

current_pair = None
current_count = 0
pair = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    pair, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_pair == pair:
        current_count += count
    else:
        if current_pair:
            # write result to STDOUT
            	print current_pair, current_count
        current_count = count
        current_pair = pair

# do not forget to output the last pair if needed!
if current_pair == pair:
       print current_pair,current_count
