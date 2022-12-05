```


                    $$$$$$$$\        $$\       $$$$$$$\                  $$\                 
                    \__$$  __|       $$ |      $$  __$$\                 $$ |                
                       $$ | $$$$$$\  $$ |  $$\ $$ |  $$ | $$$$$$\   $$$$$$$ |                
                       $$ |$$  __$$\ $$ | $$  |$$$$$$$  |$$  __$$\ $$  __$$ |                
                       $$ |$$ /  $$ |$$$$$$  / $$  ____/ $$$$$$$$ |$$ /  $$ |                
                       $$ |$$ |  $$ |$$  _$$<  $$ |      $$   ____|$$ |  $$ |                
                       $$ |\$$$$$$  |$$ | \$$\ $$ |      \$$$$$$$\ \$$$$$$$ |                
                       \__| \______/ \__|  \__|\__|       \_______| \_______|                



               $$$$$$\                                                                       
              $$  __$$\                                                                      
              $$ /  \__| $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
              \$$$$$$\  $$  _____|$$  __$$\ \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
               \____$$\ $$ /      $$ |  \__|$$$$$$$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
              $$\   $$ |$$ |      $$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
              \$$$$$$  |\$$$$$$$\ $$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      
               \______/  \_______|\__|      \_______|$$  ____/ $$  ____/  \_______|\__|      
                                                     $$ |      $$ |                          
                                                     $$ |      $$ |                          
                                                     \__|      \__|                          


```                                                                                                                                                 



<div align="center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Python 3.5](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
  
</div>
---

## Table of Contents
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Authors](#authors)

## Getting Started <a name = "getting_started"></a>

### Prerequisites

- Python
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
- Chrome Browser

--- 
### How To Use
1. Clone the Repository
   ``` 
   - git clone https://github.com/Cyper24/Tokped-Scrapper
   ```
2. Install Requirements
   ```
   - cd Tokped-Scrapper
   - pip install -r requirements.txt
   ```
3. Run

    Replace 'Your Chromedriver Dir' with your chromedriver directory in TokpedS and TokpedD
    ```
     driver = webdriver.Chrome(r'Your Chromedriver Dir')
    ```
      - Product Search
        ```
        - python TokpedS.py
        ```
      - Product Detail
        ```
        - python TokpedD.py
        ```
        
### Note
  - Run TokpedS.py first and will auto generate csv file for TokpedD.py urllist
  - Access Denied = Selenium detect 

## Built Using <a name = "built_using"></a>
  - Python 
  - Selenium 
  - BeautifulSoup
  - Pandas
  
## Authors <a name = "authors"></a>
 - [@Cyper24](https://github.com/Cyper24)


