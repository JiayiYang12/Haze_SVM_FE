# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:54:59 2019

@author: asus
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
data=pd.read_csv('D:/data bank/statiatics2019/result1.csv',sep=',',encoding='utf-8')#读取csv文件
#data = pd.read_csv('D:/data bank/statiatics2019/result_new.txt', sep='\t', names=['kernel', 'gamma', 'C','accuracy'])#读取txt文件

#data.to_excel('D:/data bank/statiatics2019/result2.xlsx')#将TXT文件输出为csv文件

#按照hue分组的柱状图,默认统计的是age_dec变量的均值，estimator=np.mean
sns.barplot(x="gamma", y="accuracy",hue='kernel',data=data,palette=sns.color_palette("Set2", 10))
#按照hue分组的柱状图,默认统计的是age_dec变量的均值，estimator=np.mean
sns.barplot(x="C", y="accuracy",hue='kernel',data=data,palette=sns.color_palette("Set2", 10))
#按照hue分组的柱状图,默认统计的是age_dec变量的均值，estimator=np.mean
sns.barplot(x="gamma", y="accuracy",hue='kernel',data=data,palette=sns.color_palette("Set2", 10))

