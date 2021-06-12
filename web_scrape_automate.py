# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:02:17 2020

@author: jashj
"""

import requests, re
from bs4 import BeautifulSoup
from googlesearch import search 
import pandas as pd
from tqdm import tqdm

df=pd.read_excel("Web_scrapping.xlsx", sheet_name='IT companies')
l=[]
df=df[500:1000]
l=[]

for emp in tqdm(df['Employer'][:1]): 
    
    for j in search(emp+" myvisajob",num=1,stop=1):

        if 'myvisajobs.com' in j:
            r=requests.get(j)
            c=r.content

            ## Web scraper
            soup=BeautifulSoup(c,"html.parser")

            try:

                all=soup.find_all("table",{"class":"tbl"})[0]

                var=all.find_all("td")
                
                H1B_Dependent=soup.find_all("td",{"align":"right","valign":"top"},text="H1B Dependent:")[0].findNextSiblings()

                Yes_No=H1B_Dependent[0].contents[0][:-2]
                
                Citizenship=soup.find_all("td",{"align":"right","valign":"top"},text="Citizenship:")[0].findNextSiblings()
                
                Country=Citizenship[0].contents[0]
                
                NAICS = soup.find_all("td",{"align":"right","valign":"top"},text="NAICS Industry:")[0].findNextSiblings()

                NAICS_field=NAICS[0].contents[0]
                
                x=[(lambda x: x.text)(x) for x in var][:-2]

                length=len(x)

                counter=length//5
                
                for i in range(1,counter):

                    dict={}
                    dict['Employer']=emp
                    dict['Contact(edit)']=x[i*5]
                    dict['Name']=x[i*5 + 1]
                    dict['Job Title']=x[i*5 + 2]
                    dict['Phone']=x[i*5 + 3]
                    dict['Email']=x[i*5 + 4]
                    dict['H1B Dependent']=Yes_No
                    dict['Country']=Country
                    dict['NAICS']=NAICS_field

                    l.append(dict)

            except:
                dict={}
                dict['Employer']=emp
                dict['Contact(edit)']='-'
                dict['Name']='-'
                dict['Job Title']='-'
                dict['Phone']='-'
                dict['Email']='-'
                dict['H1B Dependent']='-'
                dict['Country']='-'
                dict['NAICS']='-'
                

                l.append(dict)
            
        else:
            dict={}
            dict['Employer']=emp
            dict['Contact(edit)']='-'
            dict['Name']='-'
            dict['Job Title']='-'
            dict['Phone']='-'
            dict['Email']='-'
            dict['H1B Dependent']='-'
            dict['Country']='-'
            dict['NAICS']='-'

            l.append(dict)
        


df1=pd.DataFrame(l)
df1.to_csv('final(501-1000).csv',index=None)