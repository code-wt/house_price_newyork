import pandas as pd
import numpy as np
import csv
df=pd.read_csv('rollingsales_queens.csv',encoding='ISO-8859-1')
print(type(df))
data_zero=[]
for i in range(len(df[' SALE PRICE '])):
    if 10000000>=df[' SALE PRICE '][i]>=10000:
        data_zero.append(i)
    else:
        pass
with open('queens.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(df.columns.values)
    for i in data_zero:
        writer.writerow(df.iloc[i])

df=pd.read_csv('queens.csv',encoding='ISO-8859-1')
for i in range(len(df['LAND SQUARE FEET'])):
    if 15000>=df['LAND SQUARE FEET'][i]>100:
        data_zero.append(i)
    else:
        pass
with open('queens.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(df.columns.values)
    for i in data_zero:
        writer.writerow(df.iloc[i])