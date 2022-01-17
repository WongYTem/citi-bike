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

am_start_list = Q4.loc[(Q4['starttime'].dt.hour==(7 or 8))&(Q4['starttime'].dt.weekday!=(5 & 6)), 'start station name'].value_counts()
am_start_list
am_end_list = Q4.loc[(Q4['starttime'].dt.hour==(7 or 8))&(Q4['starttime'].dt.weekday!=(5 & 6)), 'end station name'].value_counts()
am_end_list
am= pd.merge(left=am_start_list, left_index=True, right=am_end_list, right_index=True, how='inner')
am.columns = ['am bikes in','am bikes out']
am
#get the number of weeks from Sep to Dec
from datetime import date
days=abs(date(2020,9,1)-date(2020,12,31)).days
days
#calcuate the bike logistic for every day average
am['am bikes in']/=days
am['am bikes out']/=days

#add new column to show how many bikes are idle
am['am difference']=am['am bikes in']-am['am bikes out']
am=am.sort_values(by=['am difference'], ascending=True)
am

##pm

pm_start_list = Q4.loc[(Q4['starttime'].dt.hour==(18 or 19))&(Q4['starttime'].dt.weekday!=(5 & 6)), 'start station name'].value_counts()
pm_start_list
pm_end_list = Q4.loc[(Q4['starttime'].dt.hour==(18 or 19))&(Q4['starttime'].dt.weekday!=(5 & 6)), 'end station name'].value_counts()
pm_end_list
pm= pd.merge(left=pm_start_list, left_index=True, right=pm_end_list, right_index=True, how='inner')
pm.columns = ['pm bikes in','pm bikes out']
pm

#get the number of weeks from Sep to Dec
from datetime import date
days=abs(date(2020,9,1)-date(2020,12,31)).days
days
#calcuate the bike logistic for every day average
pm['pm bikes in']/=days
pm['pm bikes out']/=days

#add new column to show how many bikes are idle
pm['pm difference']=pm['pm bikes in']-pm['pm bikes out']
pm=pm.sort_values(by=['pm difference'], ascending=True)
pm
am

