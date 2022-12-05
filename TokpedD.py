import pandas as pd
from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0')
driver = webdriver.Chrome(r'Your Chromedriver Dir',chrome_options=chrome_options)
driver.maximize_window()
contents = []
detail = []

source = 'list.csv'
with open(source, 'rt', encoding='utf-8-sig') as cp_csv:
    cp_url = csv.reader(cp_csv)
    for row in cp_url:
        url = row[0]
        contents.append(url)
    # print(contents)
       
for links in contents:
    time.sleep(1)
    driver.get(links)
    time.sleep(1)
    try:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        elem = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div[4]/div/h1')
        if elem.is_displayed():
            x = soup.select('h1.css-1320e6c')[0].text.strip()
            s = soup.find('span', {'data-testid' : 'lblPDPDetailProductRatingNumber'}).text
            h = soup.find("div", {"class": "price"}).text
            for k in soup.find_all('div', {'data-testid' : 'lblPDPDescriptionProduk'}):
                f = k.get_text(separator="\n").strip()
            kondisi = soup.select('li.css-1dmo88g')[0].text.strip()
            w = soup.select('li.css-1dmo88g')[1].text.strip()
            li = links
            det = {'Nama Produk' : x,'Rating' : s,'Harga' : h,'Keterangan' : f,'Kondisi' : kondisi,'Berat' : w,'Link' : li}
            detail.append(det)
        df = pd.DataFrame(detail)
        df.to_csv('Detail.csv',index=False)
        print('Success | Next')
            
    except:
        print('Access Denied')
        time.sleep(1)
    


# driver.quit()