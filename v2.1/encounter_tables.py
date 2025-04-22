import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import datetime
import math
import random
import re
import os
import winsound

def human_delay(min_time=2, max_time=5):
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)


def encounter(df ,rename, eps = 'V25A2'):
    episode =  {'E1A1':'3f61c772-4560-cd3f-5d3f-a7ab5abda6b3',
                'E1A2':'0530b9c4-4980-f2ee-df5d-09864cd00542',
                'E1A3':'46ea6166-4573-1128-9cea-60a15640059b',
                'E2A1':'97b6e739-44cc-ffa7-49ad-398ba502ceb0',
                'E2A2':'ab57ef51-4e59-da91-cc8d-51a5a2b9b8ff',
                'E2A3':'52e9749a-429b-7060-99fe-4595426a0cf7',
                'E3A1':'2a27e5d2-4d30-c9e2-b15a-93b8909a442c',
                'E3A2':'4cb622e1-4244-6da3-7276-8daaf1c01be2',
                'E3A3':'a16955a5-4ad0-f761-5e9e-389df1c892fb',
                'E4A1':'573f53ac-41a5-3a7d-d9ce-d6a6298e5704',
                'E4A2':'d929bc38-4ab6-7da4-94f0-ee84f8ac141e',
                'E4A3':'3e47230a-463c-a301-eb7d-67bb60357d4f',
                'E5A1':'67e373c7-48f7-b422-641b-079ace30b427',
                'E5A2':'7a85de9a-4032-61a9-61d8-f4aa2b4a84b6',
                'E5A3':'aca29595-40e4-01f5-3f35-b1b3d304c96e',
                'E6A1':'9c91a445-4f78-1baa-a3ea-8f8aadf4914d',
                'E6A2':'34093c29-4306-43de-452f-3f944bde22be',
                'E6A3':'2de5423b-4aad-02ad-8d9b-c0a931958861',
                'E7A1':'0981a882-4e7d-371a-70c4-c3b4f46c504a',
                'E7A2':'03dfd004-45d4-ebfd-ab0a-948ce780dac4',
                'E7A3':'4401f9fd-4170-2e4c-4bc3-f3b4d7d150d1',
                'E8A1':'ec876e6c-43e8-fa63-ffc1-2e8d4db25525',
                'E8A2':'22d10d66-4d2a-a340-6c54-408c7bd53807',
                'E8A3':'4539cac3-47ae-90e5-3d01-b3812ca3274e',
                'E9A1':'52ca6698-41c1-e7de-4008-8994d2221209',
                'E9A2':'292f58db-4c17-89a7-b1c0-ba988f0e9d98',
                'E9A3':'dcde7346-4085-de4f-c463-2489ed47983b',
                'V25A1':'476b0893-4c2e-abd6-c5fe-708facff0772',
                'V25A2':'16118998-4705-5813-86dd-0292a2439d90'}
    ep = episode[eps]
    driver = uc.Chrome(headless=False,use_subprocess=True)
    driver.maximize_window()
    
    df = list(df['id'])
    df1 = [ x.replace('#','%23') for x in df]
    
    tabel = []
    for ID in df1:
        try:
            link = f'https://tracker.gg/valorant/profile/riot/{ID}/encounters?platform=pc&playlist=competitive&season={ep}'
            driver.get(link)
            time.sleep(10)
            n_m = 3
            path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n_m}]/div/div[2]/div[3]/div/div[2]'
                    #//*[@id="app"]/div[2]/div[3]/div/main/div[4]    /div/div[2]/div[3]/div/div[2]
            try: 
                driver.find_element(By.XPATH, value = path).text
                print('div = 3')
            except:
                n_m = 4
                print('div = 4')

            
            #Find table element, row, and table data
            table = driver.find_element(By.TAG_NAME, 'tbody')
            trow = table.find_elements(By.TAG_NAME, 'tr')
            
            tables_r = []
            for row in trow:
                data = row.find_elements(By.TAG_NAME, 'td')
                player = []
                for column in data:
                    player.append(column.text)
                tables_r.append(player)
                print(player)
            
            #Element interaction to open "Played against"'s table
            path_button = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n_m}]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div/button'
            played_with = driver.find_element(By.XPATH, path_button)
            played_with.click()

            human_delay()
            
            path_button2 = '//*[@id="trn-teleport-dropdown"]/div[6]/div[2]'
            played_against = driver.find_element(By.XPATH, path_button2)
            played_against.click()
            
            #Find table element, row, and table data
            table = driver.find_element(By.TAG_NAME, 'tbody')
            trow = table.find_elements(By.TAG_NAME, 'tr')
            
            for row in trow:
                data = row.find_elements(By.TAG_NAME, 'td')
                player = []
                for column in data:
                    player.append(column.text)
                tables_r.append(player)
                print(player)
            tabel = tabel + tables_r
            time.sleep(10)
        except Exception as e:
            print(e)

            #Alarm when code fail
            duration = 1000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            human_delay(5.2,9)

            #Restart driver
            print("Data not found")
        try:
            path_3 = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div/h1'
            driver.find_element(By.XPATH, path_3)
            driver.quit()
            driver = uc.Chrome(headless=False,use_subprocess=True)
            driver.maximize_window()
            time.sleep(300)
        except:
            None
    driver.quit()
    
    #Change  ID format to subtitutable to link
    df = pd.DataFrame(tabel)
    df.columns = ['id','encounters','rank','wr','kd','match','date']
    new_ID = []
    for ID in df['id']:
        ID = ID.replace('\n#','%23')
        new_ID.append(ID)
    df['id'] = new_ID
    
    #drop duplicate row by id
    df = df.drop_duplicates(subset='id')
    df.to_csv(rename + '.csv')
    return df

def recursive_encounter(df,rename,r=3, ep = 'V25A2'):
    for x in range(r):
        df= encounter(df ,rename, eps =  ep)
        human_delay(10,30)
    df.to_csv(str(r)+'_'+rename)
    return df