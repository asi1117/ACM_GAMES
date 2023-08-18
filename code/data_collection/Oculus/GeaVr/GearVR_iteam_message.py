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
n = 0
k = 0
worry_list = []

while(condition_to_continue):
    while(n<len(id_list)) :


        url = 'https://www.oculus.com/experiences/gear-vr/' + str(id_list[n])
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
        time.sleep(2)
        try:
            page = driver.find_element(by=By.XPATH, value='//*[@id="mount"]/div/div[2]/div/div/div[2]')
            #print(page)
            soup2 =BeautifulSoup(page.get_attribute('innerHTML'),"html.parser")
        except Exception as e:
            print(e)
        try:
            app_details = soup2.find_all('div', attrs={'class': 'app-details-row__right'})
        except Exception as e:
            print(e)
        try:
            iteam_name = soup2.find('div', attrs={'class': 'app-description__title'}).text 
          except Exception as e:
            iteam_name = ''
            print(e)
        try:
            iteam_description = soup2.find('div', attrs={'class': 'clamped-description__content'}).text
            print(iteam_description)
        except Exception as e:
            iteam_description = ''
            print(e)
        try:
            iteam_price = soup2.find('span', attrs={'class': 'app-purchase-price'}).text
        except Exception as e:
            iteam_price = ''
            print(e)
        try:
            if len(app_details) == 13:
                print(id_list[n-1]+'.csv')
                dataframe = dataframe.append(pd.DataFrame({
                    'Game_Id': id_list[n - 1],
                    'Game_Name': iteam_name,
                    'Game_price': iteam_price,
                    'Game_description': iteam_description,
                    'Game_Modes': app_details[0].text,
                    'Game_PlayerModes': '',
                    'Game_Tracking': '',
                    'Game_Controllers': app_details[1].text,
                    'Game_Platforms': app_details[2].text,
                    'Category': app_details[3].text,
                    'Game_Genres': app_details[4],
                    'Game_Languages': app_details[5].text,
                    'Game_Version': app_details[6].text,
                    'Game_Developer': app_details[7].text,
                    'Game_Publisher': app_details[8].text,
                    'Game_Website': app_details[9].text,
                    'Game_ReleaseDate': app_details[10].text,
                    'Game_Policy': app_details[11].text,
                    'Game_RecommrndedCPU': '',
                    'Game_RecommrndedGraphics': '',
                },
                    index=[count]))
                count += 1
                print(count)
                dataframe.to_csv("GearVR_Iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
                time.sleep(2)
                break
            if len(app_details) == 14:
                print(len(app_details))
                print(id_list[n-1]+'.csv')
                dataframe = dataframe.append(pd.DataFrame({
                    'Game_Id': id_list[n - 1],
                    'Game_Name': iteam_name,
                    'Game_price': iteam_price,
                    'Game_description': iteam_description,
                    'Game_Modes': app_details[0].text,
                    'Game_PlayerModes': '',
                    'Game_Tracking': '',
                    'Game_Controllers': app_details[1].text,
                    'Game_Platforms': app_details[2].text,
                    'Category': app_details[3].text,
                    'Game_Genres': app_details[4].text,
                    'Game_Languages': app_details[5].text,
                    'Game_Version': app_details[6].text,
                    'Game_Developer': app_details[7].text,
                    'Game_Publisher': app_details[8].text,
                    'Game_Website': app_details[9].text,
                    'Game_ReleaseDate': app_details[10].text,
                    'Game_Policy': app_details[11].text,
                    'Game_RecommrndedCPU': '',
                    'Game_RecommrndedGraphics': '',
                },
                    index=[count]))
                count += 1
                print(count)
                dataframe.to_csv("GearVR_Iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
                time.sleep(2)
                break
            if len(app_details) == 15:
                print(len(app_details))
                print(id_list[n - 1] + '.csv')
                dataframe = dataframe.append(pd.DataFrame({
                    'Game_Id': id_list[n - 1],
                    'Game_Name': iteam_name,
                    'Game_price': iteam_price,
                    'Game_description': iteam_description,
                    'Game_Modes': app_details[0].text,
                    'Game_PlayerModes': app_details[1].text,
                    'Game_Tracking': app_details[2].text,
                    'Game_Controllers': app_details[3].text,
                    'Game_Platforms': app_details[4].text,
                    'Category': app_details[5].text,
                    'Game_Genres': app_details[6].text,
                    'Game_Languages': app_details[7].text,
                    'Game_Version': app_details[8].text,
                    'Game_Developer': app_details[9].text,
                    'Game_Publisher': app_details[10].text,
                    'Game_Website': app_details[11].text,
                    'Game_ReleaseDate': app_details[12].text,
                    'Game_Policy': app_details[13].text,
                    'Game_RecommrndedCPU': '',
                    'Game_RecommrndedGraphics': '',
                },
                    index=[count]))
                count += 1
                print(count)
                dataframe.to_csv("GearVR_Iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
                time.sleep(2)
                break
            if len(app_details) == 16:
                print(len(app_details))
                print(id_list[n - 1] + '.csv')
                dataframe = dataframe.append(pd.DataFrame({
                    'Game_Id': id_list[n - 1],
                    'Game_Name': iteam_name,
                    'Game_price': iteam_price,
                    'Game_description': iteam_description,
                    'Game_Modes': app_details[0].text,
                    'Game_PlayerModes': app_details[1].text,
                    'Game_Tracking': app_details[2].text,
                    'Game_Controllers': app_details[3].text,
                    'Game_Platforms': app_details[4].text,
                    'Category': app_details[5].text,
                    'Game_Genres': app_details[6].text,
                    'Game_Languages': app_details[7].text,
                    'Game_Version': app_details[8].text,
                    'Game_Developer': app_details[9].text,
                    'Game_Publisher': app_details[10].text,
                    'Game_Website': app_details[11].text,
                    'Game_ReleaseDate': app_details[12].text,
                    'Game_Policy': app_details[13].text,
                    'Game_RecommrndedCPU': '',
                    'Game_RecommrndedGraphics': '',
                },
                    index=[count]))
                count += 1
                print(count)

                dataframe.to_csv("GearVR_Iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
                time.sleep(2)
                break
            if len(app_details) == 17:
                print(id_list[n-1]+'.csv')
                print(len(app_details))
                print('到这一步了')
                dataframe = dataframe.append(pd.DataFrame({
                    'Game_Id': id_list[n - 1],
                    'Game_Name': iteam_name,
                    'Game_price': iteam_price,
                    'Game_description': iteam_description,
                    'Game_Modes': app_details[0].text,
                    'Game_PlayerModes': app_details[1].text,
                    'Game_Tracking': '',
                    'Game_Controllers': app_details[2].text,
                    'Game_Platforms': app_details[3].text,
                    'Category': app_details[4].text,
                    'Game_Genres': app_details[5].text,
                    'Game_Languages': app_details[6].text,
                    'Game_Version': app_details[7].text,
                    'Game_Developer': app_details[8].text,
                    'Game_Publisher': app_details[9].text,
                    'Game_Website': app_details[10].text,
                    'Game_ReleaseDate': app_details[11].text,
                    'Game_Policy': app_details[12].text,
                    'Game_RecommrndedCPU': '',
                    'Game_RecommrndedGraphics': '',
                },
                    index=[count]))
                count += 1
                print(count)
                dataframe.to_csv("GearVR_Iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
                time.sleep(2)
                break
            else:
                print(len(app_details))
                print(id_list[n-1]+'.csv')
                print('到这一步了')
                dataframe = dataframe.append(pd.DataFrame({
                    'Game_Id': id_list[n-1],
                    'Game_Name': iteam_name,
                    'Game_price': iteam_price,
                    'Game_description': iteam_description,
                    'Game_Modes': app_details[0].text,
                    'Game_PlayerModes': app_details[1].text,
                    'Game_Tracking':app_details[2].text,
                    'Game_Controllers': app_details[3].text,
                    'Game_Platforms': app_details[4].text,
                    'Category': app_details[5].text,
                    'Game_Genres': app_details[6].text,
                    'Game_Languages': app_details[7].text,
                    'Game_Version': app_details[8].text,
                    'Game_Developer': app_details[9].text,
                    'Game_Publisher': app_details[10].text,
                    'Game_Website': app_details[11].text,
                    'Game_ReleaseDate': app_details[12].text,
                    'Game_Policy': app_details[13].text,
                    'Game_RecommrndedCPU':app_details[16].text,
                    'Game_RecommrndedGraphics':app_details[17].text,
                },
                    index=[count]))
                count += 1
                print(count)
                dataframe.to_csv("GearVR_Iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
                time.sleep(2)
                break
        except:
            print(id_list[n-1] ,"write wrong")
            worry_list.append(id_list[n-1])
            print('worry_list',worry_list)
            n = k
            continue

















