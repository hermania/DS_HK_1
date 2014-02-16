from __future__ import division
import sys

filename = "nytimes.csv"
file = open(filename,"r")

age = 0
impressions = 0
clicks = 0
signed_in = 0
impressions = 0

lines = sys.stdin.readlines()
lines.pop(0)
x = len(lines)
 
for line in lines:

  new_line = line.strip().split(',')
  age = age + int(new_line[0])

  impressions = impressions + int(new_line[2])
  clicks = clicks + int(new_line[3])

  signed_in = signed_in + int(new_line[4])

  if clicks > int(max_clicks[0]):
  	max_clicks = c_line


  if impressions > int(max_impressions)[0]):
  	max_impressions = c_line
 
>>> 
print 'Total Unique Visitors: ', x
print 'Average Impressions: ', impressions/signed_in
print 'Average Clicks: ', clicks/signed_in
print 'Average Clicks per Impression: ', clicks/impressions

with open('nytimes.csv','w') as f:
    print 'Writing to file %s' % (f.name)