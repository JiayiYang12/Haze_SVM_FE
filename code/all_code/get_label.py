'''
将数据集中pm2.5的数值按照以下标准进行分类
0~35 为优 标签为0
36~75 良  标签1
76~150 中  标签2
151~...差   标签3
By:Wsg
2015/5/19
'''

import pandas as pd

INPUT_DATA = './data_pro/data_pro.csv'
OUT_PATH = './data_pro/hour_label.csv'
data = pd.read_csv(INPUT_DATA)
pm25 = data["pm2.5"]
pm25_label = []
for i in range(0,len(pm25)):
    if pm25[i]>150:
        pm25_label.append("3")
    elif 75<pm25[i]<=150 :
        pm25_label.append('2')
    elif 36<=pm25[i]<=75:
        pm25_label.append("1")
    else:
        pm25_label.append("0")

print(pm25_label)
print(len(pm25_label))
fn = open(OUT_PATH,'w')
for i in range(0,len(pm25_label)):
    fn.write(pm25_label[i])
    fn.write("\n")
fn.close()

print("OK")