from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By 
import pandas as pd

cari = input('Cari Apa= ')
url="https://www.tokopedia.com/search?page=1&q={}&rf=true&st=product".format(cari)
driver = webdriver.Chrome(r'Your Chromedriver Dir')
driver.maximize_window()
driver.get(url)
barang = []

for x in url:
    try:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        elem = driver.find_element(By.CSS_SELECTOR,"[aria-label='Laman berikutnya']")
        if elem.is_displayed():          
            for tag in soup.find_all("div", {"class": "css-974ipl"}):        
                n = tag.find("div", {"class": "prd_link-product-name css-svipq6"}).text
                h = tag.find("div", {"class": "prd_link-product-price css-1ksb19c"}).text
                li = tag.find('a').get('href')
                total = {'Link' : li,'Name' : n,'Price' : h,}
                barang.append(total)
            df = pd.DataFrame(barang)
            df.to_csv('list.csv',header=False, index=False)
            time.sleep(1)
            elem.click() 
            print("Success | Next Page")   
    except:
        driver.execute_script("window.scrollBy(0,800)","")
        time.sleep(1)
            