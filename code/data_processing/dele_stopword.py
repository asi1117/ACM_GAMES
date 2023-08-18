# import nltk
# nltk.download()
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import csv
example_sent = 'This is a sample sentence, showing off the stop words filtration.'
readfile = 'F:/HMDdataset/other/first.csv'
writfile = 'F:/HMDdataset/stop/first.csv'
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', 'I','"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
                'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her',
                'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was',
                'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
                'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by',
                'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
                'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
                'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
                'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn',
                'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren',
                'won', 'wouldn','gear', 'vr','!', ',' ,'.' ,'?' ,'-s' ,'</s> ', 's','platform','vive','oculus',,
            'one','viveport','would','https','half','saber','www','lift','...','..',])
print(stop_words)

pf1 = pd.DataFrame()
count1 = 0

with open(readfile, encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        word_tokens = word_tokenize(row[0].lower())
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        review = str(filtered_sentence)

        print(filtered_sentence)
        pf1 = pf1.append(pd.DataFrame({
            'review': review.replace('[','').replace(']','').replace("'",'').replace(',',' '),
            'data': row[1],
        },
            index=[count1]))
        count1 += 1
    pf1.to_csv(writfile, index=False, sep=',', encoding='utf_8_sig')
