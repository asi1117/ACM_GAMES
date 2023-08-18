'''
将评论数量按月份计数
2020.01 ~ 2022.04
'''
import time
import csv


def covert_time(time_stamp):
    time_array = time.localtime(time_stamp)
    other_style = time.strftime("%Y-%m-%d %H:%M:%S", time_array)

    return other_style


if __name__ == '__main__':
    first = 0
    reviews_date = []
    path = r'F:\CHI\HMDs\Gener\total\topic\performance_time.csv'
    with open(path, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if first > 0:
                    reviews_date.append(covert_time(int(row[1])))
                else:
                    first += 1

    years = [[], [], [],[],[],[],[],[]]
    # print(len(reviews_date))
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
    print('2015: ', sum(monthes[0]))
    print('2016: ', sum(monthes[1]))
    print('2017: ', sum(monthes[2]))
    print('2018: ', sum(monthes[3]))
    print('2019: ', sum(monthes[4]))
    print('2020: ', sum(monthes[5]))
    print('2021: ', sum(monthes[6]))
    print('2022: ', sum(monthes[7]))
print(sum(monthes[1]) + sum(monthes[2]) + sum(monthes[3]) + sum(monthes[4]) + sum(monthes[5]) + sum(monthes[6]) + sum(
    monthes[7]))


