
import csv
import pandas as pd
import os
from lingua import Language, LanguageDetectorBuilder
languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
filepath = 'C:/Users/ENeS/Desktop/datasets/EnglishFliter/'
id_list = os.listdir(filepath)
df = pd.read_csv('C:/Users/ENeS/Desktop/datasets/.csv',encoding='utf_8_sig')
reviews = df['one_reviews_text'] #
df_key = reviews.keys().values#
df2 = pd.DataFrame()
for k in df_key: #
    result = detector.detect_language_of(reviews.get(k))
    if result == Language.ENGLISH:
        print('this is english',k)

        df2 = df.iloc[k]

        print(df2)
    df2.to_csv('C:/Users/ENeS/Desktop/datasets/.csv', sep=',', encoding='utf-8_sig')
    #print(result,k)

