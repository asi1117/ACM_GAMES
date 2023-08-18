'''
将评论数量按月份计数
2020.01 ~ 2022.04
'''
import time
import csv
from textblob import TextBlob

def covert_time(time_stamp):
    time_array = time.localtime(time_stamp)
    other_style = time.strftime("%Y-%m-%d %H:%M:%S", time_array)

    return other_style


if __name__ == '__main__':
    first = 0
    reviews_date = []
    pos2015 = []
    pos20152 = []
    pos2016 = []
    pos20162 = []
    pos2017 = []
    pos20172 = []
    pos2018 = []
    pos20182 = []
    pos2019 = []
    pos20192 = []
    pos2020 = []
    pos20202 = []
    pos2021 = []
    pos20212 = []
    pos2022 = []
    pos20222 = []
    count = 0
    path = r'G:\CHI\datasets\FliterAfter\time_cover\resolution.csv'
    with open(path, 'r', encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if first > 0:
                    reviews_date.append(covert_time(int(row[1])))
                    date_new = covert_time(int(row[1]))
                    blob = TextBlob(row[0])
                    if "2015" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2015.append(row[2])
                        if blob.sentiment.polarity > 0:
                            pos20152.append(row[1])
                    if "2016" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2016.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20162.append(row[1])
                    if "2017" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2017.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20172.append(row[1])
                    if "2018" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2018.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20182.append(row[1])
                    if "2019" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2019.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20192.append(row[1])
                    if "2020" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2020.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20202.append(row[1])
                    if "2021" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2021.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20212.append(row[1])
                    if "2022" in date_new:
                        # if row[3] in 'TRUE':
                        #     pos2022.append(row[3])
                        if blob.sentiment.polarity > 0:
                            pos20222.append(row[1])
                else:
                    first += 1
        print(count)
        years = [[], [], [],[],[],[],[],[]]
        # print(len(reviews_date))

        # for date in reviews_date:
        #


        for date in reviews_date:
            if "2015" in date:
                years[0].append(date.split(' ')[0])
            elif "2016" in date:
                years[1].append(date.split(' ')[0])
            elif "2017" in date:
                years[2].append(date.split(' ')[0])
            elif "2018" in date:
                years[3].append(date.split(' ')[0])
            elif "2019" in date:
                years[4].append(date.split(' ')[0])
            elif "2020" in date:
                years[5].append(date.split(' ')[0])
            elif "2021" in date:
                years[6].append(date.split(' ')[0])
            elif "2022" in date:
                years[7].append(date.split(' ')[0])


        monthes = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        base = 2015
        for i in range(len(years)):
            # print(i)
            for y in years[i]:
                if str(base + i) + '-01' in y:
                    monthes[i][0] += 1
                elif str(base + i) + '-02' in y:
                    monthes[i][1] += 1
                elif str(base + i) + '-03' in y:
                    monthes[i][2] += 1
                elif str(base + i) + '-04' in y:
                    monthes[i][3] += 1
                elif str(base + i) + '-05' in y:
                    monthes[i][4] += 1
                elif str(base + i) + '-06' in y:
                    monthes[i][5] += 1
                elif str(base + i) + '-07' in y:
                    monthes[i][6] += 1
                elif str(base + i) + '-08' in y:
                    monthes[i][7] += 1
                elif str(base + i) + '-09' in y:
                    monthes[i][8] += 1
                elif str(base + i) + '-10' in y:
                    monthes[i][9] += 1
                elif str(base + i) + '-11' in y:
                    monthes[i][10] += 1
                else:
                    monthes[i][11] += 1

        # print(monthes)
        b = 0
        for a in monthes:
            print(b,a)
            b += 1
        allMonth = monthes[0] + monthes[1] + monthes[2][:4]

        # print(len(allMonth))
        # print(allMonth)
        print('2015: ', sum(monthes[0]),'pos:',len(pos2015),'利率2',len(pos20152)/sum(monthes[0]),len(pos20162)/sum(monthes[1]),len(pos20172)/sum(monthes[2]),len(pos20182)/sum(monthes[3]),len(pos20192)/sum(monthes[4]),len(pos20202)/sum(monthes[5]),len(pos20212)/sum(monthes[6]),len(pos20222)/sum(monthes[7]))
        print('2016: ', sum(monthes[1]),'pos:',len(pos2016),'利率2',len(pos20162)/sum(monthes[1]))
        print('2017: ', sum(monthes[2]),'pos:',len(pos2017),'利率2',len(pos20172)/sum(monthes[2]))
        print('2018: ', sum(monthes[3]),'pos:',len(pos2018),'利率2',len(pos20182)/sum(monthes[3]))
        print('2019: ', sum(monthes[4]),'pos:',len(pos2019),'利率2',len(pos20192)/sum(monthes[4]))
        print('2020: ', sum(monthes[5]),'pos:',len(pos2020),'利率2',len(pos20202)/sum(monthes[5]))
        print('2021: ', sum(monthes[6]),'pos:',len(pos2021),'利率2',len(pos20212)/sum(monthes[6]))
        print('2022: ', sum(monthes[7]),'pos:',len(pos2022),'利率2',len(pos20222)/sum(monthes[7]))



