import requests, zipfile
import pandas as pd
import io
import os
import numpy as np 
from matplotlib import pyplot as plt
from io import StringIO
url = 'https://data.binance.vision/data/spot/monthly/klines/BNBBUSD/12h/BNBBUSD-12h-2022-'
zip = '.zip'
x = np.array([], dtype=np.uint32)
y = np.array([], dtype=np.uint32)

for i in range(1, 12):
        num = '0'+str(i) if i < 10 else str(i)
        patho = url+num+zip
        #download all months in a year
        #patho = os.path.normpath(patho)
        #r = requests.get(patho, stream=True)
        #print(r.status_code)
        #z = zipfile.ZipFile(io.BytesIO(r.content))
        #z.extractall(os.path.join(os.getcwd(), 'data'))
        pathi = 'BNBBUSD-12h-2022-'+num+'.csv'
        df  =    pd.read_csv(os.path.join(os.getcwd(), 'data', pathi)
        , header = None
        , names = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore'])
        x_time = df[['Open time']].to_numpy()
        x = np.append(x, x_time)
        y_price_high = df[['High']].to_numpy()
        y_price_close = df[['Low']].to_numpy()
        y_promedio = np.add(y_price_high, y_price_close)
        y_promedio =  y_promedio/2
        y = np.append(y, y_promedio)
plt.plot(x,y)
plt.show()




