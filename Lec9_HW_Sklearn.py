#Homework for General Assembly Data Science Week9
#Using sklearn to analyze bike rental data set

# Homework submission
# included in ./data is a dataset called days.csv, which is the number of registered and nonregistered (casual) bike share 
# users given a particular day and other features (wind speed, actual temperature, and "feeling temperature" (atemp).
# Build a multiple linear regression predicting registered users, and another for predicting non registered users.
# Your output files should easily replicate an R-Squared value for each model. We'll measure your success based on R-Squared 
# and share results with the rest of the class on Wednesday.
# Your output should include comments that explain how the models are different and how some variables better explain registered 
# users vs non registered.


#Load CSV Data
import pandas as pd
import numpy as np
from datetime import datetime
import time
filename = './data/days.csv'
df = pd.read_csv(filename, parse_dates = True)
df['dteday'] = df.dteday.apply(lambda d: datetime.strptime(d,'%m/%d/%Y'))


#Plot Time History of registered and casual bike use
import matplotlib.pyplot as plt
fig = plt.figure(1,(18,8))
ax1 = fig.add_subplot( 2, 1, 1)
ax1.bar(df.dteday, df.registered, color="blue",alpha = 0.4)
ax2 = fig.add_subplot( 2, 1, 2)
ax2.bar(df.dteday, df.casual, color="green",alpha = 0.4)
plt.xlabel('Date')
plt.ylabel('Resgistered Users')
plt.title('Time History of Registered Users')

#Compute P-Value and R-Squared Value for each variable
from sklearn import feature_selection
from sklearn import linear_model
def p_value(input, response):    
    values = feature_selection.univariate_selection.f_regression(input, response)  
    return values
[x, p_score] = p_value(df.iloc[:,2:11], df['registered'])
[x, p_casual] = p_value(df.iloc[:,2:11], df['casual'])
stats_results = pd.DataFrame({'p_score' : p_score})
stats_results.index = df.columns[2:11]                     
stats_results['p_casual'] = p_casual

lm = linear_model.LinearRegression()
R_Sq = []
R_Cas = []

for x in range(2,11):
    x = [x]
    lm.fit(df.iloc[:,x], df['registered'])
    R = lm.score(df.iloc[:,x], df['registered'])
    R_Sq = R_Sq + [R]

    lm.fit(df.iloc[:,x], df['casual'])
    Rc = lm.score(df.iloc[:,x], df['casual'])
    R_Cas = R_Cas + [Rc]
    
stats_results['R_Sq'] = R_Sq
stats_results['R_Sq_Casual'] = R_Cas

#Print table of P and R Values
print stats_results

# For Registered users the three most highly correlated variables are:
# 'yr', 'temp', 'atemp'
lm.fit(df[['yr','temp','atemp']], df['registered'])
R_sq_test1 = lm.score(df[['yr','temp','atemp']], df['registered'])
print 'R-Squared value for Year, Temp, and ATemp, for Registered Riders is %s' % R_sq_test1


# For Casual users the three most highly correlated variables are:
# 'workingday', 'temp', 'atemp'
lm.fit(df[['workingday','temp','atemp']], df['casual'])
R_sq_test2 = lm.score(df[['workingday','temp','atemp']], df['casual'])
print 'R-Squared value for Workingday, Temp, and ATemp, for Casual Riders is %s' % R_sq_test2


