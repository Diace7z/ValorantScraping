def mainbar(link, driver, div_nomor=3):
    
    overview=[]
    #rank, rank_rating, rank_number, level, match, playtime_hours
    list_xpath1=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]', #rank
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[2]', #rankrating
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[3]', #ranknumber
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span[2]', #level
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[2]', #Match
                f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[1]'] #Playhours
    
    #['rank','rank_rating','level', 'match', 'playtime_hours']
    for i in list_xpath1:
        try:
            # Tunggu sampai elemen dengan XPath tertentu muncul
            X_Path = i
            element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            value = element.text
            if i != list_xpath1[0]:
                value = numeric_extraction(value)
                overview.append(value)
            else:
                if value == 'Rating':
                    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, 
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[2]')))
                    overview.append(element.text)
                else:
                    overview.append(value)
            

        except Exception as e:
            overview.append(float("nan"))
    #Damage/Round, K/D Ratio, Headshot%, Win%
    #['damage_round','kill_death_ratio','headshot_rate','winrate']
    for i in range(1,5):
        try:
            X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[{i}]/div/div[2]/span[2]/span'
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span[2]/span

                    #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[2]/span[2]/span
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, X_path)))
            value = element.text
            value = numeric_extraction(value)
            overview.append(value)
        except Exception as e:
            
            overview.append(float("nan"))
        
    #Wins, KAST, DDA/Round, Kills, Deaths, Assists, ACS, KAD Ratio, Kills/Round, First Blood
    #['win', 'kast','damage_roun','kills','death','assist','acs','kad_ratio','kill_round_ratio','first_blood','flawless_round','aces']
    for i in range(1,13):
        try:
            X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div[{i}]/div/div[2]/span[2]/span'
                      #'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div[{i}]/div/div[2]/span[2]/span'
                      #'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[2]/span[2]/span
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            value = element.text
            value = numeric_extraction(value)
            overview.append(value)
            
                       #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
        except:
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[5]/div/div[1]/span[2]/span
            
            try:
                X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[1]/span[2]/span'
                element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_Path)))
                value = element.text
                value = numeric_extraction(value)
                overview.append(value)
            except Exception as e:
                overview.append(float("nan"))
                
    #['round_win']
    list_xpath2=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]']#RoundWin%]
                 
    for i in list_xpath2:
        try:
            X_path = i
            element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path)))
            value = element.text
            value = numeric_extraction(value)
            overview.append(value)
        except Exception as e:
            overview.append(float("nan"))
            
    
    
    """
    ['agent1','agent1_hours' ,'matches1', 'win_rate1', 'k/d1', 'adr1', 'acs1', 'average_ddealt_round1', 'best_map1','map1_wr',
     'agent2', 'agent2_hours','matches2', 'win_rate2', 'k/d2', 'adr2', 'acs2', 'average_ddealt_round2', 'best_map2','map2_wr',
     'agent3', 'agent3_hours','matches3', 'win_rate3', 'k/d3', 'adr3', 'acs3', 'average_ddealt_round3', 'best_map3','map3_wr',]
    """
    path_rows_agents = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div'
    n_rows_agents = int(len(driver.find_elements(by='xpath', value=path_rows_agents))/2)
    n_nan_agents = 3-n_rows_agents
    
    for i in range(1,n_rows_agents*2,2):
        try:
            X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[1]'
            value_agent = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path))).text
            value_agent_final = value_agent[:value_agent.find('\n')]
            value_agent_hours = numeric_extraction(value_agent)
            overview.append(value_agent_final)
            overview.append(value_agent_hours)
        except:
            overview.append("NoAgent")
            overview.append(float(0))
        
        for j in range(2,8):
            try:
                X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[{j}]'
                value = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path))).text
                value = numeric_extraction(value)
                overview.append(value)
                    
            except Exception as e:
                overview.append(float(0))

        try:
            X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[8]'
            value_map_raw = (WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path)))).text
            value_map = value_map_raw[:value_map_raw.find('\n')]
            value_map_wr = numeric_extraction(value_map_raw)
            overview.append(value_map)
            overview.append(value_map_wr)
            
        except Exception as e:
            print(e)
            overview.append('NoMap')
            overview.append(float(0))
        
    if n_nan_agents>0:
        overview = overview + [float("nan")]*n_nan_agents*10

    try:
        X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{div_nomor}]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]'
        tracker_score = (WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, X_path)))).text
        tracker_score = float(re.search(r'\d+', tracker_score).group())
        overview.append(tracker_score)
    except:
        overview.append(9999)
        
    return overview