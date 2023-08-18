'''
VR Only, VR Supported
'''
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

sys.setrecursionlimit(2000)


def get_html(url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'https://store.steampowered.com/'
    }
    try:
        r = requests.get(url, headers=headers, timeout=1000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()

    except:
        return ""


if __name__ == '__main__':
    cont = 1
    count1 = 0
    count2 = 0
    dataframe = pd.DataFrame()
    dataframe2 = pd.DataFrame()
    vrOnly_list = []
    support_list = []
    while cont < 8000:
        print('1')
        print(cont)
        url = 'https://store.steampowered.com/search/results/?query&start='+str(cont)+'&count=100&dynamic_data=&sort_by=_ASC&term=vr&snr=1_7_7_151_7&infinite=1'
        cont = cont+100
        json_game = get_html(url)
        html = json_game.get('results_html')
        page = BeautifulSoup(html, 'html.parser')
        #print(page)
        link = page.find_all(name='a', attrs={"class": "search_result_row ds_collapse_flag"})

        vr_requireds = page.find_all('span', attrs={"class": "vr_required"})
        #print(vr_requireds)
        for j in link:
            title = j.find('span', attrs={"class": "title"}).text
            try:
                vr_required = j.find('span', attrs={"class": "vr_required"}).text
                try:
                    if vr_required == 'VR Only':

                        print(vr_required)
                        print("game title:", title)
                        game_id = j["href"].split('/')[4]
                        vrOnly_list.append(game_id)
                        dataframe = dataframe.append(pd.DataFrame({
                            'title': title,
                            'id': game_id,
                            'vr_type': vr_required,
                            'href': j["href"].split('?')[0]},
                            index=[count1]))
                        count1 += 1
                    dataframe.to_csv("VR_Only_titles.csv", index=False, sep=',', encoding='utf_8_sig')
                    print(count1)

                except:
                    print("vr_only")
            except:
                print('vronly')
            try:
                vr_support = j.find('span', attrs={"class": "vr_supported"}).text
                try:
                    if vr_support == 'VR Supported':
                        print("game title:", title)
                        game_id = j["href"].split('/')[4]
                        dataframe2 = dataframe2.append(pd.DataFrame({
                            'title': title,
                            'id': game_id,
                            'vr_type': vr_support,
                            'href': j["href"].split('?')[0]},
                            index=[count2]))
                        count2 += 1
                    dataframe2.to_csv("VR_Support_titles.csv", index=False, sep=',', encoding='utf_8_sig')
                    print(count2)
                except:
                    print("vr_support")
            except:
                print("vrsupport")
 



