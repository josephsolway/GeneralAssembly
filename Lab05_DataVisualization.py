#Lab05_DataVisualization.py
#Last updated Joseph Solway 09/21/14

from pandas import Series, DataFrame #Series and DataFrame are used alot so imported direclty to local namespace
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time
import pylab

filename = 'trip_data_1.csv'
df = pd.read_csv(filename,nrows=100000)
df = df[(df.dropoff_longitude < -10)]
df = df[(df.dropoff_latitude > 10) & (df.dropoff_latitude < 150)]
df = df[(df.pickup_longitude < -10)]
df = df[(df.pickup_latitude > 10) & (df.pickup_latitude < 150)]


df['pickup_hour'] = df.pickup_datetime.apply(lambda d: datetime.strptime(d,'%Y-%m-%d %H:%M:%S').hour)
df['pickup_day'] = df.pickup_datetime.apply(lambda d: datetime.strptime(d,'%Y-%m-%d %H:%M:%S').strftime("%A"))


# = df['pickup_longitude'].groupby(df['pickup_day'])

#  SCATTER PLOT - Pickup
fig = plt.figure(1,(14, 8.8),facecolor="white")
ax1 = fig.add_subplot( 6, 4, 1)

#plt.ion()
#plt.show()
for i in range(24):
	ax = fig.add_subplot( 6, 4, i)
	ax.scatter(df.pickup_longitude[df.pickup_hour == i], df.pickup_latitude[df.pickup_hour == i], color="blue",alpha = 0.2)
	time_label = (str(i)+':00')
	plt.title(time_label)
#	plt.xlim([-74.7, -73.2])
#	plt.ylim([40.4, 41.2])
#	plt.draw()
#	time.sleep(0.1)



ax1.scatter(df['pickup_longitude'], df['pickup_latitude'], color="blue",alpha = 0.2)
plt.xlabel('Pickup Longitude')
plt.ylabel('Pickup Latitude')
plt.xlim([-74.7, -73.2])
plt.ylim([40.4, 41.2])
plt.title('Pickup Locations')
#  SCATTER PLOT - Dropoff



#  SCATTER PLOT - Pickup
fig = plt.figure(1,(14, 9),facecolor="white")
ax1 = fig.add_subplot( 2, 2, 1)\\
ax1.scatter(df['pickup_longitude'], df['pickup_latitude'], color="blue",alpha = 0.2)
plt.xlabel('Pickup Longitude')
plt.ylabel('Pickup Latitude')
plt.xlim([-74.7, -73.2])
plt.ylim([40.4, 41.2])
plt.title('Pickup Locations')
#  SCATTER PLOT - Dropoff
ax2 = fig.add_subplot( 2, 2, 2)
ax2.scatter(df['dropoff_longitude'], df['dropoff_latitude'], color = "red",alpha = 0.5)
plt.xlabel('Dropoff Longitude')
plt.ylabel('Dropoff Latitude')
plt.xlim([-74.7, -73.2])
plt.ylim([40.4, 41.2])
plt.title('Dropoff Locations')

# LINE PLOT
df1 = df[(df.medallion == df.medallion[7])]
i = 0
longitude = []
latitude = []
for i in range(len(df1)):
	longitude.append(df1.iloc[i,10])
	longitude.append(df1.iloc[i,12])
	latitude.append(df1.iloc[i,11])
	latitude.append(df1.iloc[i,13])
ax3 = fig.add_subplot( 2, 2, 3)
ax3.plot(longitude, latitude, color="green",linestyle ='--', marker ='o')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('One Medallion Route')

# HIST PLOT
ax4 = fig.add_subplot( 2, 2, 4)
ax4.hist(df['trip_time_in_secs']/60, bins = range(0,60,2), color="brown")
plt.title('Trip Time')
plt.xlabel('Trip time / mins')
plt.xlim([0,60])

#End of File