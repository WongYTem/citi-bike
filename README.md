# citi-bike

The sharebike system data are retrieved from Citi Bike System Data webpage: https://www.citibikenyc.com/system-data
The data used for NN is from Q4 (September, October, November, December) of 2019 and 2020

## A neural network written in Keras (TensorFlow backend) to predicting number of bike trip per day 

### source of data 
Since weather may play an important role in affecting the usage of bikes, weather data of the same period will be taken into account in the model
Weather data of New York City from https://www.ncdc.noaa.gov/cdo-web/search. 
New York Central Park is selected as the representative of the New York weather 2019 and 2020 Q4.

### performance

## Customer analysis
### By age
![image](https://user-images.githubusercontent.com/97471111/149835302-e4ecd2e9-606e-42f0-a888-892c62f179cb.png)

### Gender and User Type
![image](https://user-images.githubusercontent.com/97471111/149835543-f7377370-3223-48e7-b8a8-1362ee76e1ba.png)

### Mean of Trip duration for different User Type
*Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member

![image](https://user-images.githubusercontent.com/97471111/149835675-607b9b1c-6883-4469-9aac-51f2979282aa.png)

![image](https://user-images.githubusercontent.com/97471111/149836091-c6efaaeb-e750-462f-80b6-8417ddadd5a8.png)
From the co-efficients, 
When is a “Subscriber”, “Trip Duration” increase 815 seconds
When is a “Customer”, “Trip Duration” increase 2872 seconds
Both P-value is very small, <0.05, which means customer type very significant for predicting variable Trip Duration


