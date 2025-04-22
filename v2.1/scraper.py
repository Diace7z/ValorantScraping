import mainbar
import sidebar
import page_avaible
import sys_sampling
import link_id
import pandas as pd
import numpy as np
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from IPython.display import clear_output

def human_delay(min_time=1.5, max_time=4):
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

def div_n(driver):
    n_m = 3
    path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n_m}]/div/div[2]/div[3]/div/div[1]'
    try: 
        driver.find_element(By.XPATH, value = path).text
    except Exception as e:
        print('div : 4')
        n_m = 4
    return n_m

def scraper (filename, r = 1, ep_act = 'V25A2', error = 'n'):
    df = pd.read_csv(filename)
    try:
        overview = pd.read_csv("overview_"+filename)
        overview = np.array(overview)
        overview = list(overview)
        start = len(overview)
        print('file found')
    except:
        overview = []
        start = 0
        print('file not found')
    ids = sys_sampling.sys_sampling(list(df['id']), r)
    n_link = [ link_id.link_id(x,ep_act) for x in ids]
    print('size of data:', len(n_link))
    count = 0 + start
    for link in n_link[start:]:
        t0 = time.time()
        if count%10 == 0:
            clear_output(wait=True)
        persen = int((count*100)/(len(n_link)))
        loading_bar = ["█" for x in range(persen)] + ["|" for x in range(100 - persen) ]
        print(''.join(loading_bar),persen,'%')
        print('Player no.',count, )
        driver = page_avaible.page_available(link)
        n = div_n(driver)
        record = [link] + mainbar.mainbar(driver,dv_num = n, error = error) + sidebar.sidebar(driver,dv_num = n, error = error)
        overview.append(record)
        if n_link.index(link)%1 == 0:
             df = pd.DataFrame(overview)
             df.to_csv("overview_"+filename)
        driver.quit()
        print(record)
        human_delay()
        count+=1
        print("Scrap duration:",time.time()-t0)
    df = pd.DataFrame(overview)
    df.to_csv("overview_"+filename)
    
        


