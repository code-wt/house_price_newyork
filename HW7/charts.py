import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sci
df=pd.read_csv('E:\python_code\house_price\HW7/housing.csv')
date=df['yr_built']
data=df['price']
print(date)
sns.jointplot(x='yr_built',y='price',data=df,color = 'b', #设置颜色
              s = 50, edgecolor = 'w', linewidth = 1,#设置散点大小、边缘颜色及宽度(只针对scatter)
              stat_func=sci.pearsonr,
              kind = 'scatter',#设置类型：'scatter','reg','resid','kde','hex'
              #stat_func=<function pearsonr>,
              space = 0.1, #设置散点图和布局图的间距
              size = 8, #图表大小(自动调整为正方形))
              ratio = 5, #散点图与布局图高度比，整型
              marginal_kws = dict(bins=15, rug =True), #设置柱状图箱数，是否设置rug)
)
plt.show()