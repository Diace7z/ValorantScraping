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
def sidebar(driver,dv_num=3, error = 'n'):
    sidebar_xpath=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div/div'
                   #//*[@id="app"]/div[2]/div[3]/div/main/div[3]          /div/div[2]/div[3]/div/div[1]
                   #//*[@id="app"]/div[2]/div[3]/div/main/div[3]          /div/div[2]/div[3]/div
    time.sleep(5)
    elements= driver.find_elements(by='xpath', value=sidebar_xpath)
    title_index = {'ACCURACY':-1,
             'ROLES':-1,
             'TOP WEAPONS':-1,
             'TOP MAPS':-1}
    keys_list = list(title_index.keys())
    elements = [element.text for element in elements]
    title = []
    for element in elements:
        sep_ = element.find("""\n""")
        a = element[:sep_]
        title.append(a)
    for key in keys_list:
        try:
            index = title.index(key) + 1
            title_index[key] = index
        except:
            None
    accuracy_list = []
    roles_list = []
    top_weapons_list = []
    top_map_list=[]
    #ACCURACY SECTION
    if title_index['ACCURACY'] != -1:
        accuracy_paths = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['ACCURACY']}]/div/div[1]/table/tbody/tr[{j+1}]/td[{i+1}]' \
                          for j in range(3) for i in range(2)]
        for path in accuracy_paths:
            try:
                data = driver.find_element(By.XPATH, value=path)
                accuracy_list.append(data.text)
            except Exception as e:
                if error =='y':
                    print(e)
                accuracy_list.append(float('nan'))
    else:
        accuracy_list = [float("nan")]*6
    #ROLES SECTION
    if title_index['ROLES']!= -1:
        roles_init_ = ['Initiator',float("nan"),float("nan"),float("nan"),float("nan"),
                       'Duelist',float("nan"),float("nan"),float("nan"),float("nan"),
                       'Controller',float("nan"),float("nan"),float("nan"),float("nan"),
                       'Sentinel',float("nan"),float("nan"),float("nan"),float("nan")] 
        roles_path = []
        n_role = len(driver.find_elements(By.XPATH, value=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['ROLES']}]/div/div/div'))
        for row in range(1,n_role+1):
            roles_path = roles_path + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['ROLES']}]/div/div/div[{row}]/h5'
                             ] + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['ROLES']}]/div/div/div[{row}]/div[2]/div[{j}]/span[{i}]' for j in range(1,3) for i in range(1,3)
                             ]
        for path in roles_path:
            try:
                data = driver.find_element(By.XPATH, value=path)
                roles_list.append(data.text)
            except Exception as e:
                if error =='y':
                    print(e)
                roles_list.append(float('nan'))
        roles_list = roles_list + [float('nan')]*(4-n_role)*5
    else:
        roles_list = [float("nan")]*4*5
    for i in range(0,4):
        try:
            role_init_= roles_init_[i*5]
            index_pre = roles_list.index(role_init_)
            roles_init_[i*5:i*5+5] = roles_list[index_pre:index_pre+5]
            roles_list = roles_init_
        except:
            None
    
    #TOP WEAPONS
    if title_index['TOP WEAPONS']!= -1:
        weapon_path = []
        for row in range(1,4):
            weapon_path = weapon_path + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['TOP WEAPONS']}]/div/div[1]/div[{row}]/div[1]/div[{i}]' for i in range(1,3)
                                         ] + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['TOP WEAPONS']}]/div/div[1]/div[{row}]/div[2]/div/span[{i}]' for i in range(1,4)
                                         ] + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['TOP WEAPONS']}]/div/div[1]/div[{row}]/div[3]/span[2]'
                                         ]
            """
                                               #//*[@id="app"]/div[2]/div[3]/div/main/div[3]       /div/div[2]/div[3]/div/div[1]/div[4]                          /div/div[1]/div[1]    /div[2]/div/span[1]
                                               #//*[@id="app"]/div[2]/div[3]/div/main/div[3]       /div/div[2]/div[3]/div/div[1]/div[4]                          /div/div[1]/div[1]    /div[2]/div/span[2]
                                               #//*[@id="app"]/div[2]/div[3]/div/main/div[3]       /div/div[2]/div[3]/div/div[1]/div[4]                          /div/div[1]/div[2]    /div[2]/div/span[2]
            """
        for path in weapon_path:
            try:
                data = driver.find_element(By.XPATH, value=path)
                top_weapons_list.append(data.text)
            except Exception as e:
                if error =='y':
                    print(e)
                top_weapons_list.append(float('nan'))
    else:
        top_weapons_list = [float("nan")]*3*6
    #TOP MAPS
    if title_index['TOP MAPS']!= -1:
        map_path = []
        for row in range(2,9):
            map_path = map_path + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['TOP MAPS']}]/div/div[1]/div[{row}]/div[1]'
                                  ] + [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[1]/div[{title_index['TOP MAPS']}]/div/div[1]/div[{row}]/div[2]/div[{i}]' for i in range(1,3)
                                  ]
        for path in map_path:
            try:
                data = driver.find_element(By.XPATH, value=path)
                top_weapons_list.append(data.text)
            except Exception as e:
                if error =='y':
                    print(e)
                top_weapons_list.append(float("nan"))
    else:
        top_map_list = [float("nan")]*7*3
    sidebar_overview = accuracy_list + roles_list + top_weapons_list + top_map_list
    return sidebar_overview