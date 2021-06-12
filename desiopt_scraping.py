# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:17:30 2021

@author: yash1
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests, re
from bs4 import BeautifulSoup
import time
import pandas as pd

# Desiopt credentials
username = "t.gurumehar"
password = "Yashkumar.94"


comp_list = []
for i in range(1,3047):
    
    
    if (i == 1 or i == 300 or i == 600 or i == 900 or i == 1200 or i == 1500 or i == 1800 or i == 2100 or i == 2400 or i == 2700 or i == 3000) :
        
        # initialize the Chrome driver
        driver = webdriver.Chrome("C:\\Users\\yash1\\OneDrive\\Desktop\\chromedriver.exe")
        
        # Open link
        driver.get("http://desiopt.com/search-results-jobs/?searchId=1623053554.4322&action=search&page={}&view=list".format(i))
    
    
        # Login 
        driver.find_element_by_class_name("username").send_keys(username)
        driver.find_element_by_class_name("password").send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"blank\"]/div/form/fieldset[5]/div[2]/input").click()
        
    time.sleep(3)
    
    # Open link
    driver.get("http://desiopt.com/search-results-jobs/?searchId=1623053554.4322&action=search&page={}&view=list".format(i))
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
        
    # Class priority listing
    all = soup.find_all(attrs={"class":"priorityListing"})
    for a in all:
        var = a.find_all("a",attrs={"href":True})
        x=[(lambda x: x.text)(x) for x in var][1]
        comp_list.append(x)
        print(x)
        print("\n")

    # Class evenrow
    all = soup.find_all(attrs={"class":"evenrow"})

    for a in all:
        var = a.find_all("a",attrs={"href":True})
        x=[(lambda x: x.text)(x) for x in var][1]
        comp_list.append(x)
        print(x)
        print("\n")
     
    
    # Class oddrow
    all = soup.find_all(attrs={"class":"oddrow"})

    for a in all:
        var = a.find_all("a",attrs={"href":True})
        x=[(lambda x: x.text)(x) for x in var][1]
        comp_list.append(x)
        print(x)
        print("\n")


# All company names
df = pd.DataFrame(comp_list, columns=['company_name'])
df.to_csv('desiopt_company.csv',index=None)

# Unique company names 
df1 = pd.Series(comp_list).unique()
df1 = pd.DataFrame(df1,columns=['company_name'])
df1.to_csv('desiopt_company_unq.csv',index=None)





