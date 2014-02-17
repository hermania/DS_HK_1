#!/usr/bin/python
# Import required libraries

from __future__ import division
import sys
"""

"""


# Start a counter and store the textfile in memory
age = 0
impressions = 0
count = 0
clicks = 0
oldest_person = [0]


lines = sys.stdin.readlines()
lines.pop(0)

n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
	c_line = line.strip().split(',')
	age=int(c_line[0])
    count = count + int(line.strip().split(',')[2])
	if age == int(oldest_person[0]):
		oldest_person = c_line
		print oldest_person