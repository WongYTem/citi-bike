# Citi-bike data analysis

The sharebike system data are retrieved from Citi Bike System Data webpage: https://www.citibikenyc.com/system-data

## 1. Neural Network written in Keras to predicting number of bike trip per day 
###  Source of data 
The citibike data used for NN is from Q4 (September, October, November, December) of 2019 and 2020

Since weather may play an important role in affecting the usage of bikes, weather data of the same period will be taken into account in the model
Weather data of New York City from https://www.ncdc.noaa.gov/cdo-web/search. 
New York Central Park is selected as the representative of the New York weather 2019 and 2020 Q4.
![image](https://user-images.githubusercontent.com/97471111/150048780-b8a7e0bf-bd37-4df7-b358-bdc1cde613b4.png)
![image](https://user-images.githubusercontent.com/97471111/150048798-47b9bd81-bbf2-4fbd-8a3e-44a879b0dbfc.png)
R2 score IS 0.95 means that the model is able to predict the data pretty well

###   Performance

## 2. Logistics of bikes between Stations
Goals
 1) To avoid situations when stations run out of bikes or stock up too many bikes
 2) To reduce the logistic cost for transferring bikes
 3) To improve the logistic efficiency. 

###   Weekly demand and supply conditions
![image](https://user-images.githubusercontent.com/97471111/149838684-f7e82104-0b35-43e4-b670-50273f168205.png)
![image](https://user-images.githubusercontent.com/97471111/149838718-e9be112b-3a90-4a9b-bbdc-f2d9e9186311.png)

The changes of bike inventory of 51 stations varied from -486 bikes to +833 bikes during the period, which shows some stations not having enough bikes for users to start trips if refill is not done regularly. 

Suggestion: 
provide discounts for single trips ending at popular start stations including McGinley Square, Sip Ave and Hilltop, and trips that start from popular end stations like Grove St PATH, City Hall, and Hamilton Park, or remote stations like Union St, Lincoln Park and Brookfield Place

###   Locations of top supplying and demanding stations
![image](https://user-images.githubusercontent.com/97471111/149839142-954ab9ec-c19f-403d-894a-5849e2a50c61.png)

Blue dots: stations where more trips start from 
Red dot: stations where more trips end 

From the map, there are 3 remote stations that are far away from other stations and are more popular for ending bike trips, but less for starting.  
This is not cost-effective for transferring bikes as bikes were left and CitiBike have to travel long distances to bring them back.

Suggestion: 
1. discounts for round trips that start and end at the same stations to prevent bikes being left at remote stations
2. transfer bikes weekly for the top supplying and demanding stations, and bi-weekly/monthly transfer for the less busy bike stations

## 3. Customer analysis
###   By age
![image](https://user-images.githubusercontent.com/97471111/149835302-e4ecd2e9-606e-42f0-a888-892c62f179cb.png)

###   Gender and User Type
![image](https://user-images.githubusercontent.com/97471111/149835543-f7377370-3223-48e7-b8a8-1362ee76e1ba.png)

###   Mean of Trip duration for different User Type
*Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member

![image](https://user-images.githubusercontent.com/97471111/149835675-607b9b1c-6883-4469-9aac-51f2979282aa.png)

![image](https://user-images.githubusercontent.com/97471111/149836091-c6efaaeb-e750-462f-80b6-8417ddadd5a8.png)
From the co-efficients, 
When is a “Subscriber”, “Trip Duration” increase 815 seconds
When is a “Customer”, “Trip Duration” increase 2872 seconds
Both P-value is very small, <0.05, which means customer type very significant for predicting variable Trip Duration



