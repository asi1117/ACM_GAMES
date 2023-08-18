# 导包
import csv
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import textblob
import nltk
nltk.download('punkt')
nltk.download('stopwords')




# 文档读取
def read_file(file_path):
    file = os.listdir(file_path)
    for i in file:

        file_name = file_path+'/'+i
        return file_name
#利用textblob 构建模型

def text_blb(filename,write1_path):
    pf1 = pd.DataFrame()
    pf2 = pd.DataFrame()
    pf3 = pd.DataFrame()
    count1 = 0
    count2 = 0
    count3 = 0
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        for row in reader:
            #积极的情况
            blob = textblob.TextBlob(row[0])

            if blob.sentiment.polarity > 0:
                pf1 = pf1.append(pd.DataFrame({
                    'review': row[0],
                    'data': row[1],
                },
                    index=[count1]))
                count1 += 1
                print(count1)
                pf1.to_csv(write1_path + "positive.csv", index=False, sep=',', encoding='utf_8_sig')
            if blob.sentiment.polarity == 0:
                pf2 = pf2.append(pd.DataFrame({
                    'review': row[0],
                    'data': row[1],
                },
                    index=[count2]))
                count2 += 1
                print(count2)
                pf2.to_csv(write1_path + "neutral.csv", index=False, sep=',', encoding='utf_8_sig')
            if blob.sentiment.polarity < 0:

                pf3 = pf3.append(pd.DataFrame({
                    'review': row[0],
                    'data': row[1],
                },
                    index=[count3]))
                count3 += 1
                print(count3)
                pf3.to_csv(write1_path + "negative.csv", index=False, sep=',', encoding='utf_8_sig')

if __name__ == '__main__':
    file_path = 'C:/Users/ENeS/Desktop/datasets/Filter/FliterAfter/DRRFilter/third/cybersickness.csv'
    write1_path = 'C:/Users/ENeS/Desktop/datasets/Filter/FliterAfter/DRRFilter/third/sentation/cybersickness/'

    text_blb(file_path, write1_path)