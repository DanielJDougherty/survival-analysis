##DM Survivability -- the ability to remain alive or continue to exist. The term has more specific meaning in certain contexts. 

import pandas as pd
import datetime as dt
from lifelines import KaplanMeierFitter
from matplotlib import pyplot as plt


#load the file into a dataframe
#datecols = ['Hire Date', 'Termination Date'],
terms = pd.read_csv("terms.csv")

#convert to datetime
terms["Hire Date"]=pd.to_datetime(terms["Hire Date"])
terms["Termination Date"]=pd.to_datetime(terms["Termination Date"])

#create tenure at term column 
terms['tenure at term']=(terms['Termination Date'] - terms['Hire Date'])
#print(terms['tenure at term'])

#testing the load 
	#print(terms)
#Headers
#terms.head()
#print (terms.head(5))

#checking for missing values
	#data types
#print (terms.dtypes)
#print(terms['Hire Date'].dtypes)
#print(terms['Termination Date'].dtypes)

#columns
for columns in terms.columns:
	print(columns)


#groupings for cohorts




#Create a kaplan Meier estimate
kmf = KaplanMeierFitter() 

durations = terms["tenure at term"]
event_observed = terms["Termination Date"]

## Fit the data into the model
kmf.fit(durations, event_observed,label='Kaplan Meier Estimate')
kmf.plot(ci_show=False)
plt.show()


