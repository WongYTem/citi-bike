# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 06:51:44 2022

@author: Emily
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 09:47:57 2022

@author: Emily
"""

import numpy as np
import pandas as pd
from IPython.display import clear_output

# Load dataset.
Q419 = pd.read_csv('2019Q4_Citibike.csv')
Q4 = pd.read_csv('2020Q4_Citibike.csv')
Q4= pd.concat([Q419, Q4],axis=0, ignore_index=True)
Q4['starttime'] = pd.to_datetime(Q4['starttime'], format='%Y-%m-%d %H:%M:%S.%f')

weather = pd.read_csv('2020Q4_Weather.csv')
weather19 = pd.read_csv('2019Q4_Weather.csv')
weather= pd.concat([weather19, weather],axis=0, ignore_index=True)
weather['DATE'] = pd.to_datetime(weather['DATE'], format='%Y-%m-%d')


tripcount=Q4.groupby(Q4['starttime'].dt.date)['tripduration'].agg(['count'])
tripcount=tripcount.reset_index()

tripcount.dtypes
tripcount['starttime'] = pd.to_datetime(tripcount['starttime'], format='%Y-%m-%d %H:%M:%S.%f')

df= pd.merge(tripcount, weather, how='outer', left_on='starttime', right_on='DATE')
df= df.drop('DATE', 1)
df=df.rename(columns={'count': 'tripcount'})

import datetime as dt
df['starttime']=df['starttime'].map(dt.datetime.toordinal)

# remove special character
df.columns = df.columns.str.replace(' ', '_')
#move to last column
cols = list(df.columns.values) 
cols.pop(cols.index('tripcount')) 
df = df[cols+['tripcount']]

X = df.iloc[:, :-1]
y = df.iloc[:, -1].values

X.dtypes
categorical_cols= X.select_dtypes(include=['object'])
categorical_cols.dtypes
X_num_cols=X.select_dtypes(exclude=['object'])

from sklearn.preprocessing import LabelEncoder
# instantiate labelencoder object
le = LabelEncoder()
# apply le on categorical feature columns
categorical_cols = categorical_cols.apply(lambda col: le.fit_transform(col))  


#One-hot-encode the categorical columns, which outputs an array instead of dataframe.  
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()

array_hot_encoded = ohe.fit_transform(categorical_cols).toarray()
#Convert it to df
X_hot_encoded = pd.DataFrame(array_hot_encoded)
#Concatenate the two dataframes and turn to array : 
X = pd.concat([X_hot_encoded, X_num_cols], axis=1).values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

n_cols = X_train.shape[1] 
# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

keras.backend.clear_session()
#Initializing Neural Network
model = Sequential()


# Adding the input layer and the first hidden layer
model.add(Dense(500,  activation = 'relu', input_shape = (n_cols,)))
# Adding the second hidden layer
model.add(Dense(300, activation = 'relu'))
# Adding second third layer
model.add(Dense(250, activation = 'relu'))
# Adding second forth layer
model.add(Dense(150, activation = 'relu'))
# Adding the fifth layer
model.add(Dense(110, activation = 'relu'))
# Adding the sixth layer
model.add(Dense(80, activation = 'relu'))
# Adding the seventh layer
model.add(Dense(50, activation = 'relu'))
# Adding the eighth layer
model.add(Dense(30, activation = 'relu'))
# Adding the ninth layer
model.add(Dense(20, activation = 'relu'))
# Adding the tenth layer
model.add(Dense(1, activation = 'linear'))
model.summary()

# Compiling Neural Network
model.compile(optimizer='adam',loss='mae',metrics=['mse','mae'])
#modelcheckpoint
from keras.callbacks import ModelCheckpoint
checkpoint = ModelCheckpoint("best_model.hdf5", monitor='loss',
    save_best_only=True, mode='auto', save_freq=100)
# Fitting our model
EPOCHS=20000
BATCHSIZE=32
history=model.fit(X_train, y_train, batch_size = BATCHSIZE, epochs = EPOCHS, 
                  validation_data = (X_test,y_test), callbacks=[checkpoint],verbose=1)
from keras.models import load_model
loaded_model = load_model('best_model.hdf5')
'''
# saving the model in tensorflow format
model.save('./MyModel_tf',save_format='tf')
 # loading the saved model
loaded_model = tf.keras.models.load_model('./MyModel_tf')
'''

'''
# retraining the model
history=loaded_model.fit(X_train, y_train, batch_size = BATCHSIZE, epochs = EPOCHS, 
                         validation_data = (X_test,y_test), callbacks=[checkpoint],verbose=1)

print(history)
loaded_model = load_model('best_model2.hdf5')
'''

import matplotlib.pyplot as plt 
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Predicting the Test set results
y_pred = loaded_model.predict(X_test)
# accuracy
import sklearn.metrics as sm
print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred), 2)) 
print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred), 2)) 
print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred), 2)) 
print("R2 score =", round(sm.r2_score(y_test, y_pred), 2))
