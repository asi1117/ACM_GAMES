#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import traceback
# %%% relevent website

# %%% initialize chrome
# open website
driver = Chrome()
time_star = time.time()
# %%% collect all reviews
condition_to_continue = True
dataframe = pd.DataFrame()
count = 0

id_list = []
print(len(id_list))
n = 0
k = 0
worry_list = []

while condition_to_continue:
    while(n<len(id_list)) :
   
        url = 'https://www.viveport.com/' + str(id_list[n])
        n = n+1
        k = k+1
        driver.get(url)
        driver.maximize_window()
        driver.find_element(by=By.XPATH,value='//option[@class="view-jp_v_enus"]').click()
        time.sleep(2)
        windows = driver.window_handles  
        print(windows)
        #node_handle = driver.current_window_handle
        driver.switch_to.window(windows[-1])
        #print(node_handle)
        #driver.switch_to.window(windows[0])
        time.sleep(2)
        try:
            page = driver.find_element(by=By.XPATH, value='/html/body/div[1]')
            #print(page)
            soup2 =BeautifulSoup(page.get_attribute('innerHTML'),"html.parser")
        except:
            print('')
        try:
            app_details = soup2.find_all('div', attrs={'class': 'meta-block'})
            #print(app_details)
        except:
            print("")
        try:
            iteam_name = soup2.find('div', attrs={'class': 'page-title-wrapper product'}).text
            print(iteam_name)
        except:
            iteam_name = ''
            print('')
        try:
            iteam_description = soup2.find('div', attrs={'class': 'description-block'}).text
            print(iteam_description)
        except:
            iteam_description = ''
            print('')
        try:
            iteam_price = soup2.find('span', attrs={'class': 'price'}).text
        except:
            iteam_price = ''
            print('')
        try:
            iteam_language = soup2.find('table', attrs={'class': 'lang-supported-table'}).text
        except:
            iteam_language = ''
            print('')

        try:
            print(len(app_details))
            print(id_list[n-1]+'.csv')
            dataframe = dataframe.append(pd.DataFrame({
                'Game_Id': id_list[n-1],
                'Game_Name': iteam_name,
                'Game_price': iteam_price,
                'Game_description': iteam_description,
                'Game_platform': app_details[0].text.replace('COMPATIBLE WITH ','').replace(' ',''),
                'Game_genre':app_details[1].text.replace('GENRE:',''),
                'Game_playArea':app_details[2].text.replace('Play Area',''),
                'Game_Controllers':app_details[3].text.replace('Input Method',''),
                'Game_rating':app_details[4].text.replace('Content Rating',''),
                'Game_releaseDate':app_details[5].text.replace('Release Date',''),
                'Game_latestDate':app_details[6].text.replace('Latest Update',''),
                'Game_version':app_details[7].text.replace('Version',''),
                'Game_type': app_details[8].text.replace('Media Type',''),
                'Game_modes':app_details[9].text.replace('Number of Players',''),
                'Game_languages':iteam_language.replace(' ',''),
                'Game_developer': app_details[18].text.replace('Developer',''),
                'Game_mail': app_details[19].text.replace('Contact',''),
                'Game_Graphics':app_details[16].text.replace('Graphics',''),
                'Game_space':app_details[15].text.replace('Disk Space','')
            },
                index=[count]))
            count += 1
            print(count)
            dataframe.to_csv("viveProt_iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
            time.sleep(2)
            break
        except:
            print(id_list[n-1] ,"")
            worry_list.append(id_list[n-1])
            print('worry_list',worry_list)
            n = k
            continue












