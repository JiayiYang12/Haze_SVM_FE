
'''
 提取UCI原始数据特定天数，将其补充到测试集中
 By：wsg
 2019/5/18

'''


import pandas as pd

INPUT_PATH1 = './data_pro/111.csv'
INPUT_PATH2= './data_pro/pm25_test.csv'
OUPUT_PATH = './data_pro/pmpm25.csv'
data = pd.read_csv(INPUT_PATH1)
data2 = pd.read_csv(INPUT_PATH2)

year = data['year']
month = data['month']
day = data['day']
hour = data['hour']
DATE = []
pm25 = data['pm2.5']


year2 = data2['date']
hour2 = data2['hour']
DATE2 = []

PM25=[]
for i in range(0,len(year)):
    DATE.append(str(year[i])+'/'+str(month[i])+'/'+str(day[i])+'/'+str(hour[i]))
for i in range(0,len(year2)):
    DATE2.append(str(year2[i])+'/'+str(hour2[i]))

j = 0
for j in range(0,len(DATE2)):
    for i in range(0,len(DATE)):
        if DATE[i] == DATE2[j]:
            PM25.append(pm25[i])
            continue

fout = open(OUPUT_PATH,'w')

for i in range(0,len(PM25)):
    fout.write(str(PM25[i]))
    fout.write('\n')
fout.close()


