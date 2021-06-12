# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 19:18:29 2021

@author: yash1
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests, re
from bs4 import BeautifulSoup
import time
import pandas as pd



# initialize the Chrome driver
driver = webdriver.Chrome("C:\\Users\\yash1\\OneDrive\\Desktop\\chromedriver.exe")

comp_list = []
for i in range(1,45):   
     
    # Open link
    driver.get("https://www.optnation.com/it-jobs?&page={}".format(i))

        
    time.sleep(3)

    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    
    # Class job cent box
    all = soup.find_all(attrs={"class":"job_cent_box"})
    for a in all:
        var = a.find_all("a",attrs={"href":True})
        # String cleaning
        x=[(lambda x: x.text)(x) for x in var][0]
        temp = x.split('\n')[3].replace(u'\xa0', u' ').split(' – ')[0]
        comp_list.append(temp)
        print(temp)
        print("\n")


df = pd.DataFrame(comp_list, columns=['company_name'])
df.to_csv('optnation_company.csv',index=None)