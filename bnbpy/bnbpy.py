import requests, zipfile
import pandas as pd
import io
import os
import numpy as np 
import tensorflow as tf
from matplotlib import pyplot as plt
from io import StringIO
url = 'https://data.binance.vision/data/spot/monthly/klines/BNBBUSD/12h/BNBBUSD-12h-2022-'
zip = '.zip'
x = np.array([], dtype=np.uint32)
y = np.array([], dtype=np.uint32)
for i in range(10, 12):
        num = '0'+str(i) if i < 10 else str(i)
        patho = url+num+zip
        #download all months in a year
        #patho = os.path.normpath(patho)
        print(patho)
        r = requests.get(patho, stream=True)
        print(patho)
        print(r.status_code)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(os.path.join(os.getcwd(), 'data'))
        pathi = 'BNBBUSD-12h-2022-'+num+'.csv'
        df  =    pd.read_csv(os.path.join(os.getcwd(), 'data', pathi)
        , header = None
        , names = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore'])
        x_time = df[['Open time']].to_numpy()
        x = np.append(x, x_time)
        y_price_high = df[['High']].to_numpy(dtype = 'float')
        y_price_close = df[['Low']].to_numpy(dtype = 'float')
        y_promedio = np.add(y_price_high, y_price_close)
        y_promedio =  y_promedio/2
        y = np.append(y, y_promedio)
#plt.plot(x,y)
#plt.show()
#x_tensor = tf.convert_to_tensor(x)
#y_tensor = tf.convert_to_tensor(y)

model = tf.keras.models.Sequential([
  tf.keras.layers.Input(shape=x.shape),
  tf.keras.layers.Dense(128, activation='relu' ),
  tf.keras.layers.Dense(units = 1)
])
model.compile(optimizer='adam',
              loss='mean_squared_error')
#print(x_tensor.shape, y_tensor.shape)
print(x)
'''
model.fit(x, y, epochs=10)
model.evaluate(x, y)
y_pred = model.predict(x)
print(y_pred)
print(y_pred.shape)
'''
#plt.plot(x,y_pred)
#plt.show()

'''

#plt.plot(x,y_pred)
#plt.show()
'''