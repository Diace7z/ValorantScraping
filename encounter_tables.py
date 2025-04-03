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

def encounter(df ,rename ):
    driver = uc.Chrome(headless=False,use_subprocess=True)
    driver.maximize_window()
    
    tabel = []
    for ID in (df['id'])[:]:
        try:
            link = f'https://tracker.gg/valorant/profile/riot/{ID}/encounters?platform=pc&playlist=competitive&season=16118998-4705-5813-86dd-0292a2439d90'
            driver.get(link)
            
            time.sleep(10)
            
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
            
            
            path_button = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div/button'
            played_with = driver.find_element(By.XPATH, path_button)
            played_with.click()
            
            
            path_button2 = '//*[@id="trn-teleport-dropdown"]/div[6]/div[2]'
            played_against = driver.find_element(By.XPATH, path_button2)
            played_against.click()
            
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
            duration = 1000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            time.sleep(32)
            driver.quit()
            driver = uc.Chrome(headless=False,use_subprocess=True)
            driver.maximize_window()
            print("Data not found")
    driver.quit()
    
    df = pd.DataFrame(tabel)
    df.columns = ['id','encounters','rank','wr','kd','match','date']
    new_ID = []
    for ID in df['id']:
        ID = ID.replace('\n#','%23')
        new_ID.append(ID)
    df['id'] = new_ID
    
    df = df.drop_duplicates(subset='id')
    df.to_csv(rename)
    return df
