import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm


data = pd.read_csv("data.csv")
print(data.isnull().sum())
#数据描述性统计分析
print(data.describe())
#数据摘要信息
print(data.info())
#删除数据项
data=data.drop(['Unnamed: 0'],axis=1)
#转换信息格式并排序
data['Date'] = pd.to_datetime(data.Date)
data.sort_values(by=['Date'],inplace=True,ascending=True)
#随时间推移的Conventional Avocados的平均价格
x = data['Date']
y = data['AveragePrice']
plt.scatter(x,y,s=75,alpha=0.5)
plt.show()
#相关性分析
data_corr = pd.DataFrame({'智商':[106,86,100,101,99,103,97,113,112,110],
                    '每周看电视小时数':[7,0,27,50,28,29,20,12,6,17]})
print(data_corr.corr(method='spearman'))
#SVR回归模型
Svr = svm.SVR(kernel='rbf',C=1,gamma=0.5)
