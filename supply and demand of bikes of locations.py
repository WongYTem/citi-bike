# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 05:02:44 2021

@author: user
"""
#find out the most popular start station and end station
Q4['start station name']
ps=Q4['start station name'].value_counts()
pe=Q4['end station name'].value_counts()

#find out the unbalanced supply and demand in stations
sd= pd.merge(left=pe, left_index=True, right=ps, right_index=True, how='inner')
sd
#rename the cols for better understanding
sd.columns = ['bikes in','bikes out']
#get the number of weeks from Sep to Dec
from datetime import date
weeks=abs(date(2020,9,1)-date(2020,12,31)).days//7
weeks
#calcuate the bike logistic for week average
weeklySD=sd.copy()
weeklySD['bikes in']=sd['bikes in']/weeks
weeklySD['bikes out']=sd['bikes out']/weeks 
#add new column to show how many bikes are idle
weeklySD['weekly difference']=weeklySD['bikes in']-weeklySD['bikes out']

#calcuate the bike logistic for week average
weeklySD=sd.copy()
weeklySD['bikes in']=sd['bikes in']/121
weeklySD['bikes out']=sd['bikes out']/121 
#add new column to show how many bikes are idle
weeklySD['daily difference']=weeklySD['bikes in']-weeklySD['bikes out']
weeklySD=weeklySD.sort_values(by=['daily difference'], ascending=True)

#sort according to the differnce
#the lower differnces, the higher need for extra bikes supply
weeklySD=weeklySD.sort_values(by=['weekly difference'], ascending=True)
len(weeklySD)
weeklySD
#new df for stations that demand bikes only
demand=weeklySD['weekly difference']<0
demand=weeklySD.loc[weeklySD['weekly difference']<0]
demandTotal=demand['weekly difference'].sum()
demand['% of total demand']= demand['weekly difference']/demandTotal*100
demand.rename(columns={"weekly difference": "weekly demand"})
demand = demand.drop(['bikes in','bikes out'], 1)
demand

supply=weeklySD['weekly difference']>0
supply=weeklySD.loc[weeklySD['weekly difference']>0]
supplyTotal=supply['weekly difference'].sum()
supply['% of total supply']= supply['weekly difference']/supplyTotal*100
supply = supply.drop(['bikes in','bikes out'], 1)
supply=supply.sort_values(by=['weekly difference'], ascending=False)
supply=supply.rename(columns={"weekly difference": "weekly supply"})
supply

supply.count()
demand.count()
weeklySD.count()
Q4.plot('start station name','Frequency',kind="hist")
trans.plot("Month","Revenue",kind="scatter")

