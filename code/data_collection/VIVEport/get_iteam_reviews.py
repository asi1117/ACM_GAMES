#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: luyijun
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv


# %%% relevent packages & modules

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
import  traceback
# %%% relevent website
id2_list =[]

id = 0
driver = Chrome()
worry_list =[]
while (id<len(id2_list)):
    website = 'https://www.viveport.com/'+str(id2_list[id])
    time.sleep(3)
    # %%% initialize chrome
    # open website
    driver.get(website)
    driver.maximize_window()
    if id==0:
        try:

            driver.find_element(by=By.XPATH, value='//option[@class="view-jp_v_enus"]').click()
            time.sleep(3)
            cookie = driver.find_element(by=By.XPATH, value='//button[@class="amgdprcookie-button -allow"]')
            cookie.click()

        except:
            print("" , id)
            id=id+1
            continue
    time_star = time.time()
    # %%% collect all reviews
    condition_to_continue = True
    dataframe = pd.DataFrame()
    count = 0
    reviews_count = 1
    try:
        while (condition_to_continue):
            try:
                WebDriverWait(driver, 10).until(
                   
                    EC.visibility_of_element_located((By.XPATH, '//li[@class="item review-item amreview-review-wrapper"]')))
            except:
                print("")
                worry_list.append(id2_list[id])
                print(worry_list)
                print(len(id2_list))
                break
            reviews = driver.find_elements(by=By.XPATH, value='//li[@class="item review-item amreview-review-wrapper"]')
            print(len(reviews))
            # Finding all the reviews in the website and bringing them to python
            for r in range(len(reviews)):
                try:
                    soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
                except:
                    # I got an errorr saying that element is not attached to the page document
                    # To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//li[@class="item review-item amreview-review-wrapper"]')))
                    # reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
                reviews = driver.find_elements(by=By.XPATH, value='//li[@class="item review-item amreview-review-wrapper"]')
                soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
                # scrape raw html
                try:
                    scrap_date = datetime.datetime.now()

                except:
                    info = traceback.format_exc()
                    print(info)
                try:
                    review_text = soup.find('span', attrs={'class': 'amrev-text'}).text
                    #print(review_text)
                except:
                    review_text = ''
                    print("")
                try:
                    review_data = soup.find('p', attrs={'class': 'amreview-date'}).text
                    print(review_data)
                except:
                    review_data = ''

                try:
                    review_title = soup.find('h1', attrs={'class': 'bxHeading bxHeading--level-5 app-review__title'}).text

                    print(review_title)
                except:
                    review_title = ''
                    print('')
                try:
                    review_rating = soup.find('span', attrs={'itemprop': 'ratingValue'}).text
                    print(review_rating)
                except:
                    review_rating = ''
                    print('')
                try:
                    review_helpful = soup.find('span', attrs={'class':'amrev-voteqty'}).text
                    print(review_helpful)
                except:
                    review_helpful= ''
                    print('')
                try:
                    review_response = soup.find('p', attrs={'class':'bxParagraph bxParagraph--level-1 developer-response__body'}).text
                   # print(review_response)
                except:
                    review_response = ''
                    print('')
                try:
                    review_author = soup.find('p', attrs={'class': 'amreview-author'}).text
                    print(review_author)
                except:
                    review_author = ''
                    print('')
                try:
                    dataframe = dataframe.append(pd.DataFrame({
                        'scrapping_date': scrap_date,
                        'review_author': review_author,
                        'review_title': review_title,
                        'one_reviews_text': review_text,
                        'review_date': review_data,
                        'review_rating': review_rating,
                        'review_helpful': review_helpful,
                        'review_feedback':review_response,
                        },
                        index=[count]))
                    count += 1
                    print(count)

                    dataframe.to_csv(str(id2_list[id])+".csv", index=False, sep=',', encoding='utf_8_sig')
                    print(str(id2_list[id])+".csv")
                except:
                    print(id2_list[id],'')

            print('', reviews_count)
            reviews_count = reviews_count + 1
            #driver.find_element(by=By.XPATH, value='a[@class="action  next"]').click()
            try:
                before = driver.page_source
  
                next_page = driver.find_element_by_xpath('//a[@class="action  next"]')
                print(next_page)
                next_page.click()
      
                after = driver.page_source
                if before == after:
                    break
                else:
                    time.sleep(3)
            except:
                print("")
                break
    except:
        print('', id)
        print(worry_list)
        id = id+1
        break
    id = id + 1



















