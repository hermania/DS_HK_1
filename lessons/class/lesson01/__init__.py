from __future__ import division
import sys

filename = "nytimes.csv"
file = open(filename,"r")

age = 0
impressions = 0
clicks = 0

lines = sys.stdin.readlines()
lines.pop(0)
x = len(lines)
 
for line in lines:

  new_line = line.strip().split(',')
  age = age + int(new_line[0])

  impressions = impressions + int(new_line[2])
  clicks = clicks + int(new_line[3])

  if age > int(oldest_person[0]):
  	oldest_person = c_line


print 'Total Unique Visitors: ', x
print 'Total Impressions: ', impressions
print 'Average Age: ', age/x
print 'Average Clicks per Impression: ', clicks/impressions