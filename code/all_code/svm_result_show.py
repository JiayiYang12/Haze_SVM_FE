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
data=pd.read_csv('D:/data bank/statiatics2019/result1.csv',sep=',',encoding='utf-8')#��ȡcsv�ļ�
#data = pd.read_csv('D:/data bank/statiatics2019/result_new.txt', sep='\t', names=['kernel', 'gamma', 'C','accuracy'])#��ȡtxt�ļ�

#data.to_excel('D:/data bank/statiatics2019/result2.xlsx')#��TXT�ļ����Ϊcsv�ļ�

#����hue�������״ͼ,Ĭ��ͳ�Ƶ���age_dec�����ľ�ֵ��estimator=np.mean
sns.barplot(x="gamma", y="accuracy",hue='kernel',data=data,palette=sns.color_palette("Set2", 10))
#����hue�������״ͼ,Ĭ��ͳ�Ƶ���age_dec�����ľ�ֵ��estimator=np.mean
sns.barplot(x="C", y="accuracy",hue='kernel',data=data,palette=sns.color_palette("Set2", 10))
#����hue�������״ͼ,Ĭ��ͳ�Ƶ���age_dec�����ľ�ֵ��estimator=np.mean
sns.barplot(x="gamma", y="accuracy",hue='kernel',data=data,palette=sns.color_palette("Set2", 10))

