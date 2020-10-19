import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sci
df=pd.read_csv('queens.csv',encoding='ISO-8859-1')
date=df['YEAR BUILT']
data=df[' SALE PRICE ']
print(data.describe())
sns.jointplot(x='YEAR BUILT',y=' SALE PRICE ',data=df,color = 'b', #设置颜色
            stat_func=sci.pearsonr,
            kind = 'scatter',#设置类型：'scatter','reg','resid','kde','hex'
)
#sns.boxplot(x='LOT',y=' SALE PRICE ',data=df)
plt.show()