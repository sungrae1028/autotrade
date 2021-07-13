import pandas as pd
from pandas import Series, DataFrame
import numpy as np
data = pd.read_csv('C:\Users\ROKAF\Desktop\autotrade\btc5min.csv')
data=DataFrame(data)

seq_len = 24*12*1


day= []
for i,rows in data.iterrows():
  day.append([rows['open'],rows['high'],rows['low'],rows['close'],rows['volume'],rows['value']])

result = []
for index in range(len(day) - seq_len):
  result.append(day[index: index + seq_len])
  df=DataFrame(result)
  if index%100==0:
      df.to_csv("C:\Users\ROKAF\Desktop\autotrade\btc_seq1.csv")
