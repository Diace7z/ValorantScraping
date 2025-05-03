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
#//*[@id="oqbP7"] [verify]
def human_delay(min_time=1.5, max_time=4):
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

data_columns = ['link','rating ','level ','win_lose','playtime','dmg_round','kd_ratio','hs_rate',
                  'win_rate','wins','kast ','deal_receive','kills ','deaths ','assists '
                  ,'acs','kad_ratio','kill_per_round','first_blood','flawless','aces',
                  'round_win%','kast_score','acs_score','agent1','matches1','win_rate1',
                  'k_d_ratio1','adr_1','acs1','d_receive1','map_agent_1','agent2','matches2',
                  'win_rate2','k_d_ratio2','adr_2','acs2','d_receive2','map_agent_2','agent3',
                  'matches3','win_rate3','k_d_ratio3','adr_3','acs3','d_receive3','map_agent_3',
                  'tracker_score','past_tier','past_episode','head_rate','head_hits','body_rate',
                  'body_hits','legs_rate','legs_hits','role_1','wrate_initiator','win_lose_initiator','kda_rate_initiator',
                  'kda_num_initiator','role_2','wrate_duelist','win_lose_duelist','kda_rate_duelist','kda_num_duelist',
                  'role_3','wrate_controller','win_lose_controller','kda_rate_controller','kda_num_controller',
                  'role_4','wrate_sentinel','win_lose_sentinel','kda_rate_sentinel','kda_num_sentinel',
                  'wp_name_1','wp_type_1','wp_head_rate_1','wp_body_rate_1','wp_legs_rate_1','wp_kills_1',
                  'wp_name_2','wp_type_2','wp_head_rate_2','wp_body_rate_2','wp_legs_rate_2','wp_kills_2',
                  'wp_name_3','wp_type_3','wp_head_rate_3','wp_body_rate_3','wp_legs_rate_3','wp_kills_3',
                  'map_name_1','map_wr_1','map_win_lose_1','map_name_2','map_wr_2','map_win_lose_2',
                  'map_name_3','map_wr_3','map_win_lose_3','map_name_4','map_wr_4','map_win_lose_4',
                  'map_name_5','map_wr_5','map_win_lose_5','map_name_6','map_wr_6','map_win_lose_6','map_name_7','map_wr_7','map_win_lose_7']

def div_n(driver):
    n_m = 3
    path =  f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n_m}]'
    try: 
        respon = driver.find_element(By.XPATH, value = path).text
        if ('private' in respon.lower()) or ('not found' in respon.lower()) or ('error' in respon.lower()) or ('overview' in respon.lower()):
            n_m = 3
        else :
            n_m = 4
    except Exception as e:
        n_m = 4
    return n_m

def scraper (filename, r = 1, ep_act = 'V25A2', error = 'n', prefix = ''):
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
    driver=''
    for link in n_link[start:]:
        t0 = time.time()
        if count%2 == 0:
            clear_output(wait=True)
        persen = int((count*100)/(len(n_link)))
        loading_bar = ["█" for x in range(persen)] + ["|" for x in range(100 - persen) ]
        print(''.join(loading_bar),persen,'%')
        print('Player no.',count, )
        driver = page_avaible.page_available(link,driver)
        n = div_n(driver)
        record = [link] + mainbar.mainbar(driver,dv_num = n, error = error) + sidebar.sidebar(driver,dv_num = n, error = error)
        overview.append(record)
        if n_link.index(link)%1 == 0:
             df = pd.DataFrame(overview)
             df.columns = data_columns
             df.to_csv("overview_"+filename,  index = False)
        display(df)
        human_delay()
        count+=1
        print("Scrap duration:",time.time()-t0)
    clear_output(wait=True)
    loading_bar = ["█" for x in range(100)] 
    print(''.join(loading_bar),persen,'%')
    driver.quit()
    df = pd.DataFrame(overview)
    df.columns = data_columns
    df.to_csv("overview_"+prefix+filename,  index = False)

    
        


