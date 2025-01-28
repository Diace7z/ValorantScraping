import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def numeric_extraction(text):
    """
    value = value.replace(',','')
    value = float(re.search(r'\d+', value).group())
    """
    text = text.replace(',','')
    text = float(re.search(r'\d+', text).group())
    return text


def link_maker(Nick, episode):
    
    Episode = {'Current':'', 'V25A1':'?season=476b0893-4c2e-abd6-c5fe-708facff0772', 
               'E9A3':'?season=dcde7346-4085-de4f-c463-2489ed47983b',
              'E9A2':'?season=292f58db-4c17-89a7-b1c0-ba988f0e9d98',
              'E9A1':'?season=52ca6698-41c1-e7de-4008-8994d2221209'} 
    episode1 = Episode[episode]
    ID = str(Nick)
    if " " in ID:
        ID = ID.replace(" "," %20")
    ID = ID.replace("\n#","#")
    hashtag = ID.find("#")
    nick = ID[:hashtag]
    tag = ID[hashtag+1:]
    link = f'https://tracker.gg/valorant/profile/riot/{nick}%23{tag}/overview' + episode1
    return link

def mainbar(link, driver, div_nomor=3):
    
    overview=[]
    
    
    #rank, rank_rating, rank_number, level, match, playtime_hours
    list_xpath1=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]', #rank
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[2]', #rankrating
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[3]', #ranknumber
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span[2]', #level
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[2]', #Match
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[1]'] #Playhours
    
    #['rank','rank_rating','level', 'match', 'playtime_hours']
    for i in list_xpath1:
        try:
            # Tunggu sampai elemen dengan XPath tertentu muncul
            X_Path = i
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            value = element.text
            if i != list_xpath1[0]:
                value = value.replace(',','')
                value = float(re.search(r'\d+', value ).group())
                overview.append(value)
            else:
                if value == 'Rating':
                    element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, 
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[2]')))
                    overview.append(element.text)
                else:
                    overview.append(value)
            

        except Exception as e:
            overview.append(float("nan"))
    #Damage/Round, K/D Ratio, Headshot%, Win%
    #['damage_round','kill_death_ratio','headshot_rate','winrate']
    for i in range(1,5):
        try:
            X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[{i}]/div/div[2]/span[2]/span'
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_path)))
            value = element.text
            value = value.replace(',','')
            value = float(re.search(r'\d+', value ).group())
            overview.append(value)
        except Exception as e:
            
            overview.append(float("nan"))
        
    #Wins, KAST, DDA/Round, Kills, Deaths, Assists, ACS, KAD Ratio, Kills/Round, First Blood
    #['win', 'kast','damage_roun','kills','death','assist','acs','kad_ratio','kill_round_ratio','first_blood','flawless_round','aces']
    for i in range(1,13):
        try:
            X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[2]/span[2]/span'
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
                    
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            value = element.text
            value = value.replace(',','')
            value = float(re.search(r'\d+', value ).group())
            overview.append(value)
            
                       #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
        except:
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[5]/div/div[1]/span[2]/span
            
            try:
                X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[1]/span[2]/span'
                element = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, X_Path)))
                value = element.text
                value = value.replace(',','')
                value = float(re.search(r'\d+', value ).group())
                overview.append(value)
            except Exception as e:
                overview.append(float("nan"))
                
    #['round_win']
    list_xpath2=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]']#RoundWin%]
                 
    for i in list_xpath2:
        try:
            X_path = i
            element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path)))
            value = element.text
            value = value.replace(',','')
            value = float(re.search(r'\d+', value).group())
            overview.append(value)
        except Exception as e:
            overview.append(float("nan"))
            
    
    
    """
    ['agent1','agent1_hours' ,'matches1', 'win_rate1', 'k/d1', 'adr1', 'acs1', 'average_ddealt_round1', 'best_map1','map1_wr',
     'agent2', 'agent2_hours','matches2', 'win_rate2', 'k/d2', 'adr2', 'acs2', 'average_ddealt_round2', 'best_map2','map2_wr',
     'agent3', 'agent3_hours','matches3', 'win_rate3', 'k/d3', 'adr3', 'acs3', 'average_ddealt_round3', 'best_map3','map3_wr',]
    """
    path_rows_agents = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div'
    n_rows_agents = int(len(driver.find_elements(by='xpath', value=path_rows_agents))/2)
    n_nan_agents = 3-n_rows_agents
    
    for i in range(1,n_rows_agents*2,2):
        try:
            X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[1]'
            value_agent = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path))).text
            value_agent_final = value_agent[:value_agent.find('\n')]
            overview.append(value_agent_final)
        except:
            overview.append(float("NoAgent"))
        
        try:
            value_agent_hours = value_agent.replace(',','')
            value_agent_hours = float(re.search(r'\d+', value_agent_hours).group())
            overview.append(value_agent_hours)
        except:
            overview.append(float(0))
        
        for j in range(2,8):
            try:
                X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[{j}]'
                value = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path))).text
                value = element.text
                value = value.replace(',','')
                value = float(re.search(r'\d+', value ).group())
                overview.append(value)
                    
            except Exception as e:
                overview.append(float(0))

        try:
            X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[8]'
            value_map_raw = (WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path)))).text
            value_map = value_map_raw[:value_map_raw.find('\n')]
            overview.append(value_map)
        except:
            overview.append(float('NoMap'))
            
        try:
            value_map_wr = value_map_raw.replace(',','')
            value_map_wr = float(re.search(r'\d+', value_map_wr).group())
            overview.append(value_map_wr)
            
        except:
            overview.append(float(0))
        
    if n_nan_agents>0:
        overview = overview + [float("nan")]*n_nan_agents*8
    return overview

def sidebar(link,driver,div_nomor=3):
    
    xpath=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[1]/div'
    driver.implicitly_wait(3)
    elements= driver.find_elements(by='xpath', value=xpath)
    section=[]
    for i in elements:
        judul = i.text

        index=(judul.find("""\n"""))
        section.append((i.text)[0:index])

    accuracy_list = []
    roles_list = []
    top_weapons_list = []
    top_map_list=[]
    if ("Accuracy" or "Accurac") in section:
        if "Accurac" in section:
            number = section.index("Accurac")
        else:
            number = section.index("Accuracy")

                          #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]
        xpath_accuracy = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[1]/div[{number+1}]/'
        """
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[1]

        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[1]

        """
        #['head_rate','head_hits','body_rate','body_hits','legs_rate','legs_hits']
        for row in range(1,4):    
            for col in range(1,3):
                try:
                    list_path = f'div[1]/table/tbody/tr[{row}]/td[{col}]'
                    x_path = xpath_accuracy + list_path
                    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, x_path)))
                    value = element.text
                    value = value.replace(',','')
                    value = float(re.search(r'\d+', value ).group())
                    accuracy_list.append(value)
                    
                except:
                    accuracy_list.append(float("nan"))

    else:
        accuracy_list = [float("nan")]*6
    #
    """
    ['role1', 'win_rate1', 'win_lose1', 'kda_rate1', 'kda1', 
    'role2', 'win_rate2', 'win_lose2', 'kda_rate2', 'kda2',
     'role3', 'win_rate3', 'win_lose3', 'kda_rate3', 'kda3',
     'role4', 'win_rate4', 'win_lose4', 'kda_rate4', 'kda4']
    """
    if "Roles" in section:
        number = section.index("Roles")
        xpath_roles = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[1]/div[{number+1}]/'

        path_rows = xpath_roles+ 'div/div'
        rows_roles = driver.find_elements(by='xpath', value=path_rows)
        n_roles = len(rows_roles)
        n_nan_roles = 4-n_roles
        
        
        for i in range(1,n_roles+1):
            path_tail = [f'div/div[{i}]/h5',f'div/div[{i}]/div[2]/div[1]/span[1]', f'div/div[{i}]/div[2]/div[1]/span[2]',
                         f'div/div[{i}]/div[2]/div[2]/span[1]', f'div/div[{i}]/div[2]/div[2]/span[2]']
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[3]/div/div[1]/h5
            for tail in path_tail:
                try: 
                    x_path = xpath_roles+tail
                    element = driver.find_element(by='xpath', value=x_path).text
                    if (tail != path_tail[0]) or (tail != path_tail[2]) :
                        value = element
                        value = value.replace(',','')
                        try:
                            value = float(re.search(r'\d+', value ).group())
                            roles_list.append(value)
                        except:
                            roles_list.append(element)
                    else:
                        roles_list.append(element)
                except Exception as e:
                    print("In Roles", element,e)
                    roles_list.append(float("nan"))
        if n_nan_roles>0:
            roles_list = roles_list + [float("nan")]*n_nan_roles*5
            
    else:
        roles_list = [float("nan")]*4*5
    
    """
    ['weapon_name1', 'weapon_type1', 'head_rate1', 'body_rate1', 'legs_rate1', 'kills1',
     'weapon_name2', 'weapon_type2', 'head_rate2', 'body_rate2', 'legs_rate2', 'kills2',
     'weapon_name3', 'weapon_type3', 'head_rate3', 'body_rate3', 'legs_rate3', 'kills3']
    """
    
    if "Top Weapons" in section:
        number = section.index("Top Weapons")
        xpath_top_weapon = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[1]/div[{number+1}]/div/'
                            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[3]        /div/div[1]/div[2]/div/span[1]
        
        path_rows = xpath_top_weapon + 'div/div'
        rows_weapons = driver.find_elements(by='xpath', value=path_rows)
        n_weapons = min(len(rows_weapons),3)
        n_nan_weapons = 3-n_weapons
        
        for i in range(1,n_weapons+1):
            path_tail = [f'div[{i}]/div[1]/div[1]',f'div[{i}]/div[1]/div[2]',
                         f'div[{i}]/div[2]/div[1]/span[1]', f'div[{i}]/div[2]/div[1]/span[2]', f'div[{i}]/div[2]/div[1]/span[3]',
                         f'div[{i}]/div[3]/span[2]']
            for tail in path_tail:
                try:
                    x_path = xpath_top_weapon+tail
                    element = driver.find_element(by='xpath', value=x_path).text
                    if (tail != path_tail[0]) or  (tail != path_tail[1]):
                        value = element
                        value = value.replace(',','')
                        
                        try:
                            value = float(re.search(r'\d+', value ).group())
                            top_weapons_list.append(value)
                        except:
                            top_weapons_list.append(element)
                    else:
                        top_weapons_list.append(element)
            
                except Exception as e:
                    print("Weapon", element)
                    top_weapons_list.append(float("nan"))
            if n_nan_weapons>0:
                top_weapons_list = top_weapons_list + [float("nan")]*n_nan_weapons*6
            else:
                print()
                
    else:
        top_weapons_list = [float("nan")]*3*6

    if "Top Maps" in section:
        number = section.index("Top Maps")
        xpath_top_map = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div[2]/div[2]/div[1]/div[{number+1}]/div'

        """
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{i}]/div[1] Map name
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{i}]/div[2]/div[1] Winrate
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{i}]/div[2]/div[2] win-lose

        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[3]/div[1]
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[8]/div[1]

        """
        """
        ['map_name1', 'win_rate1', 'win_lose1',
         'map_name2', 'win_rate2', 'win_lose2',
         'map_name3', 'win_rate3', 'win_lose3',
         'map_name4', 'win_rate4', 'win_lose4',
         'map_name5', 'win_rate5', 'win_lose5',
         'map_name6', 'win_rate6', 'win_lose6',
         'map_name7', 'win_rate7', 'win_lose7']
        """
        for i in range(1,8):
            path_tail = [f'/div[{i+1}]/div[1]',
                         f'/div[{i+1}]/div[2]/div[1]',
                         f'/div[{i+1}]/div[2]/div[2]']
            for tail in path_tail:
                try:
                    x_path = xpath_top_map+tail
                    element = driver.find_element(by='xpath', value=x_path).text
                    if tail != path_tail[0]:
                        value = element
                        value = value.replace(',','')
                        value = float(re.search(r'\d+', value ).group())
                        top_map_list.append(value)
                    else:
                        top_map_list.append(element)
                except Exception as e:
                    top_map_list.append(float("nan"))
    else:
        top_map_list = [float("nan")]*7*3

    sidebar_overview = accuracy_list+roles_list+top_weapons_list+top_map_list
    
    return sidebar_overview

def id_collector(start=1, last=190,regions=["na", "eu", "ap","kr", "br", "latam"], episode='Current'):

    Episode = {'Current':'', 'V25A1':'&act=476b0893-4c2e-abd6-c5fe-708facff0772',
              'E9A3':'&act=dcde7346-4085-de4f-c463-2489ed47983b',
              'E9A2':'&act=292f58db-4c17-89a7-b1c0-ba988f0e9d98',
              'E9A1':'&act=52ca6698-41c1-e7de-4008-8994d2221209'} 
    
    tanggal = str(datetime.datetime.now())[:10]
    tail_name = tanggal
    driver = uc.Chrome()
    driver.maximize_window()
    for region in regions:
        table = []
        no_data_text=''
        for page in range(start,last+1):
            t0 = time.time()
            try:
                driver.get("https://tracker.gg/valorant/leaderboards/ranked/pc/default?region="+region+"&page="+str(page)+Episode[episode])
                try: 
                    path_nod = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div/div/div[1]/div/div/span'
                    element_nod = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, path_nod))).text
                    if element_nod == 'No players to rank':
                        break
                    else:
                        print('nothing')
                except:
                    print('table found')
                table_XPath = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div/div/div[1]/div/table/tbody/'
                              #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div/div/div[1]/div[]/table/tbody/tr[1]
                              #//*[@id="app"]/div[2]/div[3]/div/main/div[4]/div[2]/div/div/div[1]/div/table
                              #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div/div/div[1]/div/table/tbody
                num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
                num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[1]/td'))

                for row in range(1,num_rows):
                        row_data = []
                        for col in range(1, num_cols):
                            text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                            row_data.append(text)
                        table.append(row_data)
                print("Page "+str(page)+" on region "+region+ " Clear!")
            except:
                print("Page "+str(page)+" on region "+region+ " Failed!")
                
            t1 = time.time()
            print("Time Spent: ", t1-t0)
        print("Region "+region+" Clear!")
        column_name = ['no','id','change','rr','tier']
        df = pd.DataFrame(table)
        df.columns = column_name
        df.to_csv("valnames"+region+episode+tail_name+'.csv')
    driver.quit()

def valo_scraper(start=0, end=-1, sample_population_rate= 0.20, episode_act:str = 'Current',
                 file_name ='',nama_file_akhir='', div_nomor=3):
    
    dtframe = []
    t0 = time.time()
    
    #INPUT LIST OF ID
    if file_name=='':
        try:
            file_name = str(input('Input nama file:'))
            data_nama = pd.read_csv(file_name)
            print("File found")
        except:
            print("File not found")
    else:
        try:
            data_nama = pd.read_csv(file_name)
            print('File found')
        except:
            print("File not found")
    if nama_file_akhir=='':
        nama_file_akhir = str(input('Input akhir file:'))
        
    print("VALO_SCRAPER V2.01")
    
    #START AND END POINT
    
    if end<0:
        end = len(data_nama["id"])
        print( f'lastest player of this program is no.{end}')
    else:
        print( f'lastest player of this program is no.{end}')
        
    file_name_akhir = nama_file_akhir+'scraped_overview_'+file_name
    
    """
    if file_name_akhir in os.listdir():
        
        
    """
    #Systematic configuration
    list_nickname = list(data_nama["id"])[start:end]
    sample_size = math.floor(len(list_nickname)*sample_population_rate)
    print("Sample Size: ", sample_size)
    print('Estimation Time', sample_size*35*(1/3600), 'Jam')
    k = int(1/sample_population_rate)
    start_systematic = random.randint(0,k)
    count = start_systematic + start
    systematic_listed = list_nickname[start_systematic::k]
    driver = uc.Chrome(headless=False,use_subprocess=True)
    driver.maximize_window()
    
    #Main Program: scrape each ID
    for nickname in systematic_listed:
        t0sub = time.time()
        nick = nickname
        link = link_maker(nick, episode_act)
        print(link)
        error_looper = 0
        while error_looper<1:
            try:
                driver.get(link)
                path404 = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/h1'
                path_private = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div/span'
                path_verify = '/html/body/div[1]/div/h1'
                pagefound = 'Found'
                try:
                    element404 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, path404)))
                    pagefound = element404.text
                    print('Page not available')
                    time.sleep(22+random.randint(0,1)*5)
                except:
                    print('Page available')
                    
                try:
                    elementprivate = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, path_private)))
                    pagefound = elementprivate.text
                    print('Page privated')
                    time.sleep(22+random.randint(0,1)*5)
                except:
                    print('Page not privated')
                    
                try:
                    verify_detected = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, path_verify)))
                    pagefound = verify_detected.text
                    print('Page detected as bot')
                except:
                    print('Page not detected as bot')
            
                if (pagefound == "404"):
                    error_looper+=1
                    
                elif 'PRIVATE' in pagefound:
                    error_looper+=1

                elif 'tracker.gg' in pagefound:
                    time.sleep(300)
                    print('BOT DETECTED, sleep for 5 minutes')
                    
                else:
                    try:
                        time.sleep(1)
                        all_bar =  [nickname.replace('\n','')]+mainbar(link, driver, div_nomor) + sidebar(link, driver, div_nomor) 
                        print(all_bar)
                        dtframe.append(all_bar)
                        error_looper+=1
                    except Exception as e:
                        print("Terjadi error di all bar.. Program berhenti selama 60 detik!")
                        print(e)
                        time.sleep(60)
                        print("Mencoba mengulang...")
            except:
                print("Terjadi error.. Program berhenti selama 60 detik!")
                time.sleep(60)
                print("Mencoba mengulang...")
        count+=k
        print(count)
        if pagefound == "Found":
            finished = pd.DataFrame(dtframe)    
            finished.columns = (['nickname'] + ['rank','rank_rr','rank_rating','level', 'match', 'playtime_hours'] + 
                                ['damage_round','kill_death_ratio','headshot_rate','winrate'] + 
                                ['win', 'kast','damage_roun','kills','death','assist','acs',
                                 'kad_ratio','kill_round_ratio','first_blood','flawless_round','aces'] +  ['round_win'] + 
                                ['agent1','agent1_hours' ,'matches1', 'win_rate1', 'k/d1', 'adr1', 'acs1', 'average_ddealt_round1', 'best_map1','map1_wr',
                                 'agent2', 'agent2_hours','matches2', 'win_rate2', 'k/d2', 'adr2', 'acs2', 'average_ddealt_round2', 'best_map2','map2_wr',
                                 'agent3', 'agent3_hours','matches3', 'win_rate3', 'k/d3', 'adr3', 'acs3', 'average_ddealt_round3', 'best_map3','map3_wr',] + 
                                ['head_rate','head_hits','body_rate','body_hits','legs_rate','legs_hits']+
                                ['role1', 'win_rate1', 'win_lose1', 'kda_rate1', 'kda1', 
                                 'role2', 'win_rate2', 'win_lose2', 'kda_rate2', 'kda2',
                                 'role3', 'win_rate3', 'win_lose3', 'kda_rate3', 'kda3',
                                 'role4', 'win_rate4', 'win_lose4', 'kda_rate4', 'kda4'] + 
                                ['weapon_name1', 'weapon_type1', 'head_rate1', 'body_rate1', 'legs_rate1', 'kills1',
                                 'weapon_name2', 'weapon_type2', 'head_rate2', 'body_rate2', 'legs_rate2', 'kills2',
                                 'weapon_name3', 'weapon_type3', 'head_rate3', 'body_rate3', 'legs_rate3', 'kills3'] + 
                                ['map_name1', 'win_rate1', 'win_lose1',
                                 'map_name2', 'win_rate2', 'win_lose2',
                                 'map_name3', 'win_rate3', 'win_lose3',
                                 'map_name4', 'win_rate4', 'win_lose4',
                                 'map_name5', 'win_rate5', 'win_lose5',
                                 'map_name6', 'win_rate6', 'win_lose6',
                                 'map_name7', 'win_rate7', 'win_lose7'])
            finished.to_csv(file_name_akhir)
            del finished
        t1sub = time.time()
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")

        print("Iteration time spent: ", t1sub-t0sub)
        time.sleep(random.randint(0,1) * 3.5)
    driver.quit()
    dtframe.clear()
    t1 = time.time()
    print("Time spent (minute):", (t1-t0)/60)
    
