import csv
import requests
import urllib2
import StringIO

url = 'http://stat.columbia.edu/~rachel/datasets/nyt1.csv'

#opens up the url and store the response as 'response'
response = urllib2.urlopen(url)

#start a csv iteratros by using the csv reader function
nyt = csv.reader(response)

counts, gender, signins = 0, 0, 0

# ignores the header row
next(nyt, None)

for line in nyt:
    counts += 1
    gender += int(line[1])
    signins += int(line[4])

gender_0 = counts - gender
signins_0 = counts - signins

print "Gender 0:", gender_0
print "Gender 1:", gender
print "Signin 0:", signins_0
print "Signin 1:", signins