#General Assembly Lecture 3
#Created joseph solway 9/10/2014
#Last updated joseph solway 9/10/2014
#Exercise 3

#Lab: Munging data
#1. Count the number of each instance in index 3 (bachelors, hs-grad, etc)
#2. Count the number of each combinatino in index 3 and index 10 (gender)
#3. Find the average hours per week (index 13) for the groups in number 2
#4. Given the counts available between 2 and the average hours in 3, do you believe any sample sizes seem to small to have a meaningful average?
#Extra: Find other interesting ways to aggregate the data available. Keep in mind potential problems you may want to solve.

import requests
import csv
#web_request = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
#Saved locally:
web_request = requests.get('adult.data')
web_data = web_request.text


#1. Count the number of each instance in index 3 (bachelors, hs-grad, etc)
counter = {}
reader = csv.reader(web_data.splitlines())
for row in reader:
    if len(row) > 2:
        name = row[3] 
        if name in counter: 
            counter[name] += 1
        else:
            counter[name] = 1
names = counter.keys()
print 'Grade Completion'
for key, value in sorted(counter.items()): 
	print '%s : %d' %(key, value)

#2. Count the number of each combinatino in index 3 and index 10 (gender)       
counter_gender = {}
reader = csv.reader(web_data.splitlines())
for row in reader:
    if len(row) > 2:
        name = row[3] + ' ' + row[9]
        if name in counter_gender: 
            counter_gender[name] += 1
        else:
            counter_gender[name] = 1
names = counter_gender.keys()
print 'Grade Completion by Gender'
for key, value in sorted(counter_gender.items()): 
    print '%s : %d' %(key, value)

#3. Find the average hours per week (index 13) for the groups in number 2
hours= {}
reader = csv.reader(web_data.splitlines())
for row in reader:
    if len(row) > 2:
        name = row[3] + ' ' + row[9]
        if name in hours: 
            hours[name] += int(row[12])
        else:
            hours[name] = int(row[12])
average_hours = {}
print 'Average Hours per Week by Grade and by Gender'
for name in names:
    average_hours[name] = hours[name] / counter_gender[name]
    print '%s : %d' %(name, average_hours[name])

#4. Given the counts available between 2 and the average hours in 3, do you believe any sample sizes seem to small to have a meaningful average?
#Answer: 
print 'I think the sample sizes are okay'  
 
#Extra: Find other interesting ways to aggregate the data available. Keep in mind potential problems you may want to solve.



