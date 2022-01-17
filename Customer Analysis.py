# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 03:53:12 2021

@author: user
"""
import pandas as pd
import datetime
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
# reading two csv files
Q4 = pd.read_csv('2020Q4_Citibike.csv')

Q4.head()
Q4.dtypes
Q4['starttime'] = pd.to_datetime(Q4['starttime'], format='%Y-%m-%d %H:%M:%S.%f')
Q4['stoptime'] = pd.to_datetime(Q4['stoptime'], format='%Y-%m-%d %H:%M:%S.%f')
Q4["Count"]=1 #for counting row

#Analysis 1 - User Age
current_age = datetime.datetime.now()
#Convert birth year to age
Q4["age"] = current_age.year - Q4['birth year']
#Seperate dataset to diffferent age group and count the total number of the group
ranges = [0,24,34,44,54,64,200]
agegroup = Q4.groupby(pd.cut(Q4.age, ranges, labels= ["24 or below", "25-34", "35-44", "45-54", "55 - 64", "65 or above"] ) ).size()
agegroup.plot.pie(title="Age group Distrubtion")

# Analysis 2 - User Gender and User Type
#gender Count
print("Gender Count Table:\n",Q4.groupby(Q4['gender'])['Count'].agg(['count']))
#User Type Count
print("User Type Count Table:\n",Q4.groupby(Q4['usertype'])['Count'].agg(['count']))

#Relationship between Gender and User Type
count_a2=pd.pivot_table(Q4,values=["Count"],index=["gender"],columns=["usertype"],aggfunc="count")
count_a2.plot.bar(xlabel='Gender', ylabel="count", title="Relationship between Gender and User Type", stacked=True)
print("Gender Count Table based on User Type:\n",count_a2)


# Analysis 3 - Trip Duration
# Minimum, Maximum and Mean seconds of trip
Q4["Month"] = Q4["starttime"].dt.month
print("Minimum, Maximum and Mean seconds of trip Table: \n",pd.pivot_table(Q4,values=["tripduration"],index=["Month"],aggfunc=[min,"mean",max]))

#Mean of Trip duration for different User Type
pd.pivot_table(Q4,values=["tripduration"],index=["usertype"],columns=["gender"],aggfunc="mean")
meantime=pd.pivot_table(Q4,values=["tripduration"],index=["usertype"],columns=["gender"],aggfunc="mean")
meantime.plot.bar(xlabel='User Type', ylabel='Trip duration (second)',title="Mean of Trip duration based on the User Type")
print("Mean of Trip duration (second) for different User Type and Gender Table:\n",meantime)


# trip duration with customer type
dummies = pd.get_dummies(Q4["usertype"], prefix = "Usertype")
Q4 = Q4.join(dummies)
y = Q4["tripduration"]
x = Q4[["Usertype_Customer","Usertype_Subscriber"]]

import statsmodels.api as sm
mymodel=sm.OLS(y,x)
result=mymodel.fit()
print("Prediction of trip duration with customer type: \n", result.summary())


# Analysis 4 - Predict User Type base on age and trip duration
Q4['usertype_number']= Q4['usertype'].str.replace("Customer ","0")
Q4['usertype_number']= Q4['usertype'].str.replace("Subscriber","1")
Q4['usertype_number'] = pd.to_numeric(Q4['usertype_number'],errors='coerce')
Q4 = Q4.replace(np.nan, 0, regex=True)
Q4['usertype_number'] = Q4['usertype_number'].astype(int)

y= Q4["usertype_number"]
x= Q4[["age","tripduration"]]

###training testing split
from sklearn import model_selection
x_train, x_test, y_train, y_test=model_selection.train_test_split(x,y,test_size=0.2,random_state=0)

import statsmodels.api as sm
mymodel=sm.OLS(y_test, x_test)
result=mymodel.fit()
print("Prediction of trip duration with customer type: \n", result.summary())


###fit model
from sklearn import linear_model
mymodel= linear_model.LogisticRegression()
mymodel.fit(x_train, y_train)
y_pred= mymodel.predict(x_test)

###evaluation
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred)
#Classification
print(metrics.classification_report(y_test, y_pred)) 
#Precision Recall Curve & ROC curve
metrics.plot_precision_recall_curve(mymodel, x_test, y_test)
metrics.plot_roc_curve(mymodel, x_test, y_test)

from sklearn import model_selection
result = model_selection.cross_val_score(mymodel, x, y, cv=5, scoring="accuracy")
print("Cross-validation: %0.2f accuracy with a standard deviation of %0.2f" % (result.mean(), result.std()))






