import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
import winsound
import random
import subprocess

# List of proxies


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



#//*[@id="app"]/div[2]/div[3]/div/main/div[4]
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

def page_available(link, driver):
    #Condition:
    #"0" : Available 
    #"1" : Not Available
    #"2" : Bot Detected
    #"3" : Error Pages, switch IP
    n = 3
    condition = 2
    text = 'Error_3'
    while condition > 1:
        try:
            driver.get(link)
            time.sleep(7)
        except:
            driver = uc.Chrome(headless=False,use_subprocess=True)
            driver.maximize_window()
            driver.get(link)
            time.sleep(7)

        n = div_n(driver)
        print(n)
        path_0 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div/div[2]/div[3]/div' #Mainbar and Sidebar
        path_1_1 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div'   #Not found
        path_1_2 = f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div' #Privated 
        path_2 = f'/html/body/div[1]/div/h1' #Bot detected, need verify
        path_3 =   f'//*[@id="app"]/div[2]/div[3]/div/main/div[{n}]/div'
        try:
            response = driver.find_element(By.XPATH, value = path_0)
            condition = 0
            text = '0, Data available'
            print(text)
        except Exception as e:
            #print(e)
            None
        if condition != 0 :
            try:
                response = driver.find_element(By.XPATH, value = path_1_1)
                print('respon : ',response.text)
                if 'error' in (response.text).lower() :
                    condition = 3
                    print('error/detected')
                elif 'private' in (response.text).lower() :
                    condition = 1
                    print('privated')
                elif 'not found' in (response.text).lower() :
                    condition = 1
                    print('id not found')
                else:
                    condition = 2
                    print('something error')
            except Exception as e:
                #print(e)
                None
            #
        if condition > 1:
            print('Programs will start in 0.5 minutes')
            disable_warp()
            time.sleep(30)
            driver.quit()
        else:
            print("Page accessable")
    return driver

