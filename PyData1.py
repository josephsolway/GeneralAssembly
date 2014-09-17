#LWS EC2
#strings are immutable. Have to use regex (re) to change it.
#immutable objects are faster to use in Python






Series, DataFrame #Series and DataFrame are used alot so imported direclty to local namespace
import pandas as pd
import os

os.chdir('C:/Users/joe.solway/Documents/GitHub/GeneralAssembly/')   # Change current working directory

df = pd.read_csv('nyt1.csv') #csv import uses comma as delimeter
df.ix[:,:5]

gender1 = sum(df.Gender==1)
gender0 = sum(df.Gender==0)
signin1 = sum(df.Signed_In==1)
signin0 = sum(df.Signed_In==0)

print('count for gender=1 is %s' % gender1)
print('count for gender=0 is %s' % gender0)
print('count for sign-in=1 is %s' % signin1)
print('count for sign-in=0 is %s' % signin0)



## Download the file into ~/Downloads
## run: python nytimes_counter.py < ~/Downloads/nyt1.csv
# Import required libraries
import sys

# Start a counter and store the textfile in memory
gender = 0

signins = 0
lines = sys.stdin.readlines() #stdin - Standard Input
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
  gender = gender + int(line.strip().split(',')[1])

for line in lines:
  signins = signins + int(line.strip().split(',')[4])

gender_0 = len(lines) - gender
signins_0 = len(lines) - signins

print "Gender 0: ", gender_0
print "Gender 1: ", gender_1
print "Signin 0: ", signins_0
print "Signin 1: ", signins_1



import csv
import requests
import urllib2
import StringIO

url = 'http://stat.columbia.edu/~rachel/datasets/nyt1.csv'

## urllib2 version
response = urllib2.urlopen(url)
nyt = csv.reader(response)


## requests version
r = requests.get(url)
data = r.text
nyt = csv.reader(data.splitlines(), delimiter='\t')


