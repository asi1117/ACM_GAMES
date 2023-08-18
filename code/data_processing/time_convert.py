
import csv
import os
import re
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import time


def cheak_month(mon):
    month = mon
    if month == 'Jan':
        month = '1'
    elif month == 'Feb':
        month = '2'
    elif month =='Mar':
        month = '3'
    elif month == 'Apr':
        month = '4'
    elif month == 'May':
        month = '5'
    elif month == 'Jun':
        month = '6'
    elif month == 'Jul':
        month = '7'
    elif month == 'Aug':
        month = '8'
    elif month == 'Sep':
        month = '9'
    elif month == 'Oct':
        month = '10'
    elif month == 'Nov':
        month = '11'
    else:
        month = '12'

    return month

def cheak_year(mon):
    year = mon
    if year == '15':
        year = '2015'
    elif year == '16':
        year = '2016'
    elif year == '17':
        year = '2017'
    elif year == '18':
        year = '2018'
    elif year == '19':
        year = '2019'
    elif year == '20':
        year = '2020'
    elif year == '21':
        year = '2021'
    elif year == '22':
        year = '2022'

    return year

def vive_time(str):
    timeStamp = 0
    try:
        element = str.split(',')
        year = element[1].split(' ')[1]
        month = element[0].split(' ')[0]
        day = element[0].split(' ')[1]
        month = cheak_month(month)
        ymd = year + '-' + month + '-' + day + ' 12:23:34'

  
        timeArray = time.strptime(ymd, "%Y-%m-%d %H:%M:%S")

   
        timeStamp = int(time.mktime(timeArray))

    except Exception as e:
        print(e)
    return timeStamp


def oculus_time(str):
    timeStamp = 0
    try:
        if '-' in str:
            return vive2_time(str)
        if 'ago' in str:
            timeStamp = 1653922800  
        if 'at' in str:
            element = str.split('at')[0]
            # element = str
            if ',' in element:
                timeStamp = vive_time(element)
                # print(element)
                # print(timeStamp)
                # print('-----------------------------')
            else:
                # print(element)
                day = element.split(' ')[1]
                month = element.split(' ')[0]

                if month in 'May, Jun':
                    # 说明评论时间是20220430之后
                    timeStamp = 1653922800
                else:
                    if month in 'Aug, Sep, Oct, Nov, Dec':
                        year = '2021'
                    else:
                        year = '2022'
                    month = cheak_month(month)
                    ymd = year + '-' + month + '-' + day + ' 12:23:34'
                    
                    timeArray = time.strptime(ymd, "%Y-%m-%d %H:%M:%S")
                
                    timeStamp = int(time.mktime(timeArray))

        else:
            timeStamp = str
    except Exception as e:
        print(e,'错误')
        # return timeStamp
    return timeStamp


def vive2_time(str):
    timeStamp = 0
    try:
        year = cheak_year(str.split('-')[2])

        month = cheak_month(str.split('-')[1])
        day = str.split('-')[0]
        ymd = year + '-' + month + '-' + day + ' 12:23:34'


        timeArray = time.strptime(ymd, "%Y-%m-%d %H:%M:%S")


        timeStamp = int(time.mktime(timeArray))
    except Exception as e:
        print(e)
    return timeStamp


if __name__ == '__main__':
    totalNum = 0
    # files = os.listdir(r'C:\Users\ENeS\Desktop\datasets\SentimentAnalyze\')
    gameCnt = 0
    first = 0
    df = pd.DataFrame()

    with open(r'C:\Users\ENeS\Desktop\datasets\Filter\FliterAfter', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                # print(row[1])
                df = df.append(pd.DataFrame({
                    'Reviews': row[0],
                    'Review_date': oculus_time(row[1]),
                },
                    index=[gameCnt]))
                gameCnt += 1
        df.to_csv(r'C:\Users\ENeS\Desktop\datasets\Filter\FliterAfter\, index=False, sep=',', encoding='utf_8_sig')
    print('review cnt: ', gameCnt)

