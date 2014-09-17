import requests
import csv

web_request = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')

web_data = web_request.text

status= {}
status_female= {}
reader = csv.reader(web_data.splitlines())
for row in reader:
    # this will just print the zero-index 
    if len(row) > 2:
        name = row[3] + ' ' + row[9]
        if name in status_male: 
            status[name] += 1
        else:
            status[name] = 1

print status
        
hours= {}
status_female= {}
avehours = {}
reader = csv.reader(web_data.splitlines())
for row in reader:
    # this will just print the zero-index 
    if len(row) > 2:
        name = row[3] + ' ' + row[9]
        if name in status_male: 
            status[name] += 1
            hours[name] += row[12]                        
        else:
            status[name] = 1
            hours[name] = row[12] 

