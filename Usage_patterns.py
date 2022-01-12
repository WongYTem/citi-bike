# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 03:53:12 2021

@author: user
"""
import pandas as pd
import numpy as np
  
# reading two csv files
Q4 = pd.read_csv('2020Q4_Citibike.csv')

#by hour 
#convert start_time to start_hour 
Q4['start_hour'] = pd.to_datetime(Q4['starttime'], format="%Y-%m-%d %H:%M:%S.%f").dt.hour

#Visualize the Number of bike rental by hour
starthour = Q4.groupby("start_hour").size()
user_by_hour = starthour.plot.line(title="Number of bike rental by hours", figsize=(10, 10), rot=0)
#Set the label of the plot
user_by_hour.set_xlabel('Hour of the day')
user_by_hour.set_ylabel('Number of bike rental')

#Weekday
Q4['Weekday'] = pd.to_datetime(Q4['starttime'], format='%Y-%m-%d %H:%M:%S.%f').dt.weekday

#Seperate data to different group(weekday) and plot
by_weekday = Q4.groupby('Weekday').size()
user_by_weekday = by_weekday.plot(kind='bar', title='Number of bike rental by week of the day',xlabel='Day of the week', ylabel="Number of bike rental")

#Convert datetime to month
Q4['Month'] =  pd.to_datetime(Q4['starttime'], format="%Y-%m-%d %H:%M:%S.%f").dt.month_name()

#Count the total number of user in each month
by_month = Q4.groupby("Month").size()

#Plot the data and make the label
user_by_month = by_month.plot(kind='bar', title='Number of bike rental by month',xlabel='Month', ylabel="Number of bike rental")
user_by_month.set_ylabel("Number of rental")