'''
    网络爬虫,爬取2014年至2019年3月最高、低温度
    url:http://www.fjtxj.com/2017beijing1yuetianqi/ (2017 和1 可替换,注意2019年不需要输入)
    从2018年3月原始数据的列交换,,需要单独考虑一下！
    数据说明: 第一列日期，第二列最高温，第三列最低温
    吐槽一下:网站太随意，数据错乱现象会出现,需手动修正数据集(第二列大于第三列即可)
    2019/5/16
    By：Wsg
'''
import urllib.request
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

OUPUT_PATH = './data/yinsu.csv'
year = [2014,2015,2016,2017,2018,'']
MONTH = [1,2,3,4,5,6,7,8,9,10,11,12]
fout = open(OUPUT_PATH, 'w', encoding='utf-8')

for each in year:
    for month in MONTH:

        max_temp=[]  #存储最高温
        min_temp=[]  #存储最低温
        date=[]    #存储日期
        wind = []   #存储风力

        url = 'http://www.fjtxj.com/'+str(each)+'beijing'+str(month)+'yuetianqi/'
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        # pat1 ='日</a>(.*?)<td class="'
        pat2 = '<td>(.*?)</td>'
        result = re.compile(pat2).findall(data)

        result = list(result)

        # print(result)
        if each ==2018:
            if month >=3:
                for i in range(0,len(result)):     #提取需要的数据，初次爬取的数据混乱

                    if (i-1)%6 ==1:
                         min_temp.append(result[i])
                    elif (i-1)%6 ==0:
                        max_temp.append(result[i])
                    elif (i-1)%6 ==4:
                        wind.append(result[i])
            else:
                for i in range(0, len(result)):  # 提取需要的数据，初次爬取的数据混乱

                    if (i - 1) % 6 == 0:
                        min_temp.append(result[i])
                    elif (i - 1) % 6 == 1:
                        max_temp.append(result[i])
                    elif (i - 1) % 6 == 4:
                        wind.append(result[i])
        elif each =='':
            if month <=3:     #将截止日期设置为2019年3月
                for i in range(0, len(result)):  # 提取需要的数据，初次爬取的数据混乱

                    if (i - 1) % 6 == 1:
                        min_temp.append(result[i])
                    elif (i - 1) % 6 == 0:
                        max_temp.append(result[i])
                    elif (i - 1) % 6 == 4:
                        wind.append(result[i])
            else:
                break
        else:
            for i in range(0, len(result)):  # 提取需要的数据，初次爬取的数据混乱

                if (i - 1) % 6 == 0:
                    min_temp.append(result[i])
                elif (i - 1) % 6 == 1:
                    max_temp.append(result[i])
                elif (i - 1) % 6 == 4:
                    wind.append(result[i])

        k = 0
        for i in range(0,len(min_temp)):  #将最高温，最低温，等文字剔除
            if (i+k)%11 ==0:
                min_temp.pop(i)
                wind.pop(i)
                max_temp.pop(i)
                k = k +1
            if k == 3:
                break
        # print(k)
        for i in range(0,len(min_temp)):   #规范日期格式统一成像20180101的格式
            if each != '':
                if month <=9:
                    if i+1 <=9:
                        date.append(str(each)+"0"+str(month) +"0"+ str(i+1))
                    else:
                        date.append(str(each) + "0" + str(month) + str(i+1))
                else:
                    if i+1 <=9:
                        date.append(str(each)+str(month) +"0"+ str(i+1))
                    else:
                        date.append(str(each)+str(month) + str(i+1))
            else:
                if month <=9:
                    if i+1 <=9:
                        date.append("2019"+"0"+str(month) +"0"+ str(i+1))
                    else:
                        date.append("2019" + "0" + str(month) + str(i+1))
                else:
                    if i+1 <=9:
                        date.append("2019"+str(month) +"0"+ str(i+1))
                    else:
                        date.append("2019"+str(month) + str(i+1))

        for i in range(0,len(min_temp)):
            fout.write(date[i])
            fout.write(',')
            fout.write(min_temp[i][0:len(min_temp[i])-2])    #爬下来的是字符串，需要把℃去掉
            fout.write(',')
            fout.write(max_temp[i][0:len(max_temp[i])-2])
            # fout.write(',')
            # fout.write(wind[i])     #这个网站的风力数据用不上，此处懒得删就留下了
            fout.write('\n')
        print("第"+str(each)+"年"+str(month)+"月爬取成功")

fout.close()
print('数据爬取完成')
