# Lecture 8
#September 28 2014
#http://nbviewer.ipython.org/github/teachingdatascience/data-science-course/blob/forstudentviewing/08_data_results/lab.ipynb
#Homework
#Are animal sleep patterns dependent on their weight?

#We want to test the relationships between the hours of sleep_rem or sleep_cycle an animal gets, 
#and either body weight or brain weight. Repeat the steps above in one or two cells to show:

#Is there a linear relationship between one of these variables and the number of hours?
#If so, what's the measure of goodness of fit?
#Does one seem to fit better than another?
#By practicing:
#creating histograms, scatterplots, and qqplots
#fitting a single variable linear model
#reading and interpreting the returning summary table

#ADVANCED
#There are missing values all over the data set. Which variables seem easy to interpolate? Include your code.

import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix
from matplotlib import pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import statsmodels.formula.api as smf

pd.options.display.mpl_style = 'default'
spat = pd.read_csv('https://raw.githubusercontent.com/TeachingDataScience/data-science-course/forstudentviewing/08_data_results/data/msleep.csv')

# Comparison of Brain-Weight to Sleep REM

spat_cleaned_up = pd.DataFrame(spat)
spat_cleaned_up['sleep_rem'].dropna(inplace=True)
spat_cleaned_up['brainwt'].dropna(inplace=True)
spat_cleaned_up['log_sleep_rem'] = np.log(spat_cleaned_up['sleep_rem'])
spat_cleaned_up['log_brainwt'] = np.log(spat_cleaned_up['brainwt'])
fig, axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(spat_cleaned_up.sleep_rem, spat_cleaned_up.brainwt, 'go')
axes[1].plot(spat_cleaned_up.log_sleep_rem, spat_cleaned_up.log_brainwt, 'mo')
model = smf.ols(formula='brainwt ~ sleep_rem', data=spat_cleaned_up)
results = model.fit()
print 'NORMAL FIT SUMMARY'
print(results.summary())
print
log_model = smf.ols(formula='log_brainwt ~ log_sleep_rem', data=spat_cleaned_up)
log_results = log_model.fit()
print 'LOG-LOG FIT SUMMARY'
print(log_results.summary())
print fig
print('Answer = no clear correlation between brain weight and Sleep-REM')

# Comparison of Brain-Weight to Sleep Cycle

spat_cleaned_up['sleep_cycle'].dropna(inplace=True)
spat_cleaned_up['log_sleep_cycle'] = np.log(spat_cleaned_up['sleep_cycle'])
fig, axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(spat_cleaned_up.sleep_cycle, spat_cleaned_up.brainwt, 'go')
model = smf.ols(formula='brainwt ~ sleep_cycle', data=spat_cleaned_up)
results = model.fit()
print 'NORMAL FIT SUMMARY'
print(results.summary())
print
axes[1].plot(spat_cleaned_up.log_sleep_cycle, spat_cleaned_up.log_brainwt, 'mo')
log_model = smf.ols(formula='log_brainwt ~ log_sleep_cycle', data=spat_cleaned_up)
log_results = log_model.fit()
print 'LOG-LOG FIT SUMMARY'
print(log_results.summary())
print fig
print('Answer = Correlation between log of brain weight and log of Sleep-Cycle')

#Options for removing NA values:
spat_cleaned_up.fillna(spat_cleaned_up.mean())

