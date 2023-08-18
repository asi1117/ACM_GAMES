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

id_list =[]
#print(len(id2_list))
print(len(id_list))
n = 1
k = 0
worry_list = []

for id in  id_list:
    
    url = 'https://www.oculus.com/experiences/quest/' + str(id)
    print(n)
    n = n+1
    k = k+1
    driver.get(url)
    driver.maximize_window()
    windows = driver.window_handles 
    print(windows)
    #node_handle = driver.current_window_handle
    driver.switch_to.window(windows[-1])
    #print(node_handle)
    #driver.switch_to.window(windows[0]) 
    time.sleep(4)
    try:
        page = driver.find_element(by=By.XPATH, value='//*[@id="mount"]/div/div[2]/div/div/div[2]')
        #print(page)
        soup2 =BeautifulSoup(page.get_attribute('innerHTML'),"html.parser")
    except:
        print('')
        worry_list.append(id)
        continue
    try:
        app_details = soup2.find_all('div', attrs={'class': 'app-details-row__right'})
        #print(app_details)
    except:
        print("")
        worry_list.append(id)
        print(worry_list)
        continue
    try:
        iteam_name = soup2.find('div', attrs={'class': 'app-description__title'}).text
        print(iteam_name)
    except:
        iteam_name = ''
        print('')
    try:
        iteam_description = soup2.find('div', attrs={'class': 'clamped-description__content'}).text
        print(iteam_description)
    except:
        iteam_description = ''
        print('')
    try:
        iteam_price = soup2.find('span', attrs={'class': 'app-purchase-price'}).text
    except:
        iteam_price = ''
        print('')
    try:
        print(len(app_details))
        print('')
        dataframe = dataframe.append(pd.DataFrame({
            'Game_Id': str(id+','),
            'Game_Name': iteam_name,
            'Game_price': iteam_price,
            'Game_description': iteam_description,
            'Game_Modes': app_details[0].text,
            'Game_PlayerModes': app_details[1].text,
            'Game_Controllers': app_details[2].text,
            'Game_Platforms': app_details[3].text,
            'Game_Genres': app_details[4].text,
            'Game_Languages': app_details[5].text,
            'Game_Version': app_details[6].text,
            'Game_Developer': app_details[7].text,
            'Game_Publisher': app_details[8].text,
            'Game_Website': app_details[9].text,
            'Game_ReleaseDate': app_details[10].text,
        },
            index=[count]))
        count += 1
        print(count)
        print(id+'.csv')
        dataframe.to_csv("3Item_message.csv", index=False, sep=',', encoding='utf_8_sig')
        time.sleep(2)
    except:
        print(id ,"")
        worry_list.append(id)
        print(worry_list)






    # try:
    #     game_Modes = soup2.find('div',attrs={'class':'app-details-row__right'})
    # except:
    #     game_playWays = soup2.find('')
    #
    #
















