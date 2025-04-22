import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
import winsound
import random
import subprocess

# List of proxies
proxies = [
    "134.209.29.120:8080",
    "109.160.20.134:8080",
    "103.22.99.235:8080",
    "47.88.3.19:8080",
    "15.204.161.192:18080",
    "47.88.62.42:80",
    "64.225.8.142:10005",
    "128.199.6.201:10010",
    "192.53.126.207:10232",
    "192.53.126.207:10096"
]



def get_driver_with_proxy(proxy):
    options = uc.ChromeOptions()
    options.add_argument(f'--proxy-server=http://{proxy}')
    driver = uc.Chrome(options=options,headless=False,use_subprocess=True)
    
    return driver



def disable_warp():
    try:
        result = subprocess.run(["warp-cli", "disconnect"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ WARP disconnected successfully.")
            time.sleep(10)
            result = subprocess.run(["warp-cli", "connect"], capture_output=True, text=True)
            print("✅ WARP connected successfully.")
        else:
            print(f"❌ Failed to disconnect WARP: {result.stderr}")
        result = subprocess.run(["warp-cli", "connect"], capture_output=True, text=True)
    except FileNotFoundError:
        print("⚠️ warp-cli not found. Make sure Cloudflare WARP is installed and added to PATH.")




def div_n(driver):
    n = 3
    count = 0
    path_0 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/div[2]/div[3]/div' #Mainbar and Sidebar
    path_1_1 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/h1'   #Not found
    path_1_2 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/span' #Privated
    path_2 = f'/html/body/div[1]/div/h1' #Bot detected, need verify
    path_3 =   f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/h1'
    try: 
        driver.find_element(By.XPATH, value = path_0).text
    except Exception as e:
        count +=1
    try: 
        element = driver.find_element(By.XPATH, value = path_1_1).text
    except Exception as e:
        count +=1
    try: 
        element = driver.find_element(By.XPATH, value = path_1_2).text
    except Exception as e:
        count +=1
    try: 
        element = driver.find_element(By.XPATH, value = path_2).text
    except Exception as e:
        count +=1
    try: 
        element = driver.find_element(By.XPATH, value = path_3).text
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        disable_warp()
    except Exception as e:
        count +=1
    print(count)
    if count==5:
        n = 4
    return n

def page_available(link):
    #Condition:
    #"0" : Available 
    #"1" : Not Available
    #"2" : Bot Detected
    #"3" : Error Pages, switch IP
    n = 3
    condition = 3
    text = 'Error_3'
    while condition > 1:

        driver = uc.Chrome(headless=False,use_subprocess=True)
        driver.maximize_window()
        driver.get(link)
        time.sleep(6)

        n = div_n(driver=driver)
        path_0 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/div[2]/div[3]/div' #Mainbar and Sidebar
        path_1_1 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/h1'   #Not found
        path_1_2 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/span' #Privated 
        path_2 = f'/html/body/div[1]/div/h1' #Bot detected, need verify
        path_3 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/h1'
        try:
            response = driver.find_element(By.XPATH, value = path_0)
            condition = 0
            text = '0, Data available'
        except Exception as e:
            #print(e)
            None
        if condition != 0 :
            try:
                response = driver.find_element(By.XPATH, value = path_1_1)
                condition = 1
                print(response)
                text = '1.1, ID not found/changed'
            except Exception as e:
                #print(e)
                None
            try:
                response = driver.find_element(By.XPATH, value = path_1_2)
                condition = 1
                print(response)
                text = '1.2, account privated'
            except Exception as e:
                #print(e)
                None
            try:
                response = driver.find_element(By.XPATH, value = path_2)
                print(response)
                condition = 2
                text = '2, Bot detected'
            except Exception as e:
                #print(e)
                None
            #
        if condition > 1:
            print('Programs will start in 5 minutes')
            time.sleep(300)
            print(text)
            driver.quit()
        else:
            print("Page accessable")
            print(text)
    return driver

