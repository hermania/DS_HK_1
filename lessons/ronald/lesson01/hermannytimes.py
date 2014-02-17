#!/usr/bin/python
# Import required libraries

from __future__ import division
import sys
"""

"""


# Start a counter and store the textfile in memory
age = 0
impressions = 0
clicks = 0

lines = sys.stdin.readlines()
lines.pop(0)
oldest_person = [0]
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
	clean_line = line.strip().split(',')
	age = int(clean_line[0])

if int(clean_line[0])>80:
  	impressions = impressions + int(clean_line[2])
  	clean_line = clean_line + int(clean_line[3])
if age = int[oldestPerson[0]):
	oldest person = clean_line
print 'Total Unique visitors: ', n
print 'Total Impressions: ', Impressions
print 'Average age: ', age/n
print 'Average Clicks per Impression: ' clicks/impressions
print oldest_person