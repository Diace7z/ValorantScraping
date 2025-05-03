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

def mainbar(driver, dv_num=3, error='n'):
    overview=[]
    #rank, rank_rating, rank_number, level, match, playtime_hours
    general = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[{i}]' for i in range(1,4)]
    playtime = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/span[{i}]' for i in range(1,2)]
    main_1 = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[{i}]/div/div[2]/span[2]' for i in range(1,5)]
    main_2 = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div[{i}]' for i in range(1,13)]
    main_3 = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[{i}]' for i in range(1,4)]
    agents = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[{j}]/div[{i}]' for j in range(1,6,2) for i in range(1,9)]
    score = [f'//*[@id="app"]/div[2]/div[3]/div/main/div[{dv_num}]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]']
    paths = general + playtime + main_1 + main_2 + main_3 + agents + score
    for path in paths:
        try:
            data = driver.find_element(By.XPATH, value = path).text
            overview.append(data)
        except Exception as e:
            if error == 'y':
                print(e)
            overview.append(float('nan'))
    return overview
    """
    general     = {rank, level, win-lose} ; n=3
    playtime    = {hours, matches}; n=2
    main_1      = {Damage/round, k/d_ratio, headshot%, win%}; n=4
    main_2      = {wins, kast, dda/round, kills, deaths, assists, acs, kad_ratio, kills/round, first_bloods, flawless_rounds, aces}; n=12
    main_3      = {roundwin%, kast, acs, dda/round}; n=4
    agents      = {agent1, win%1, k/d1, adr1, acs1, dda1, best_map1, agent2, win%2, k/d2, adr2, acs2, dda2, best_map2, agent3, win%3, k/d3, adr3, acs3, dda3, best_map3; n=24 
    score       = {tracker score}; n=1

    total columns = 50
    """