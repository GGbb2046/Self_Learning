import requests
from requests import get
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import time
from tqdm import tqdm 

tic = time.perf_counter()

#initiate data storage

title = []
description = []
location = []
links = []
sector = []
certified = []
overall_score = []
crtf_date = []
website = []
score_category = []
absent = []
score_value = []
site = []
k=[]
v=[]
category_list = ["Governance", "Workers","Community", "Environment", "Customers"]
v_list = ['0','0','0','0','0']
honors =[]

last_page = BeautifulSoup(requests.get('https://bcorporation.net/directory?page=0').content, 'html.parser').find('li', class_='pager-last').a.get('href')[-3:]

page_num = np.arange(0,int(last_page),1)


for pg in tqdm(page_num):

    page = requests.get('https://bcorporation.net/directory?page='+str(pg))

    soup = BeautifulSoup(page.content, 'html.parser')

    view_row = soup.find_all('div', class_='views-row')
   
    #count = 0

    for container in view_row:
       
        name = container.a.h3.text
        title.append(name)

        
        descr = container.a.find(class_='field-item').text
        if bool(descr):
            description.append(descr)
        else:
            description.append('0')


        loc = container.a.find(class_='field-name-field-country').text
        if bool(loc):
            location.append(loc)
        else:
            location.append('0')
        
        
        lnk = container.a.get('href')      
        lnk_check=lnk[11:]
        if bool(lnk_check):
            links.append(lnk)
            URL = 'https://bcorporation.net'+str(lnk)
            page1 = requests.get(URL)
            soup1 = BeautifulSoup(page1.content, 'html.parser')
            
        

            class_sector = soup1.find('div', class_='field field-name-field-sector field-type-text field-label-hidden sans-serif')
            sctr = str(class_sector)[151:(len(str(class_sector))-18)]
            sector.append(sctr)
            
            class_ovscr = soup1.find('span', class_='text-grey-text').text.strip()
            if bool(class_ovscr):
                overall_score.append(class_ovscr)
            else:
                overall_score.append('0')

            #print(count)
            
            category = soup1.find_all('section', class_='profile__impact_scores')
            scores = soup1.find_all('section', class_='profile__impact_scores')         

            certified = soup1.find('span',class_='date-display-single').text.strip()
            if bool(certified):
                crtf_date.append(certified)
            else:
                crtf_date.append('0')


            web = soup1.find('div',class_='field field-name-field-website field-type-text field-label-hidden text-uppercase sans-serif') 
            if bool(web):
                webs = web.text.strip()
                website.append(webs)
            else: 
                website.append('0')
            
            
            if bool(category):

                for container1 in category:

                    innercategory = container1.find_all('span', class_= 'heading4')
            
                    for container2 in innercategory:
                        
                        ctgr = container2.text.strip()    
            
                        score_category.append(ctgr)
                        k.append(ctgr)
                        absent = set(category_list).difference(score_category)
                    
                 
                
                score_category.extend(absent)
                k.extend(absent)
                score_category.clear()

            else:
                k.extend(category_list)

            if bool(scores):

                for container3 in scores:
                    
                    innerscores = container3.find_all(class_='circle') 

                    for container4 in innerscores:

                        scr = container4.text.strip()
                        score_value.append(scr)
                        v.append(scr)

            else:
                score_value.extend(v_list)
                v.extend(v_list)
            
            #count = count + 1   

            rem = ((len(score_value))%5)
            if rem != 0:
                residual = 5-rem
                while residual > 0:
                    score_value.append('0')
                    v.append('0')
                    residual = residual -1

            honor = soup1.find_all('div', class_='profile__best-world col-md-12 col-sm-6 col-xs-12')
            
            
            if bool(honor):

                for container5 in  honor:
                
                    hnr = container5.text.replace('\nBest for the World Honoreeinfo_outline\nlink','').replace('link',', ')
                    honors.append(hnr)
                                
            else:
                
                honors.append('0')    
        
        else:
            
            sector.append('0')
            overall_score.append('0')
            links.append('0')
            crtf_date.append('0')
            website.append('0')
            honors.append('0')
            k.extend(category_list)
            v.extend(v_list)

    #Check arrays for equal length        
        if ((len(k))/5)!=len(title):
            print('Inconsistency in page' + str(pg)+ ',title: ' + name)
            break


            

#creating a dictionary        
score = defaultdict(list)
for key, value in zip(k,v):
    score[key].append(value) 

for x,y in score.items():
    print (x, len(list(filter(None, y))))

print("The number of titles is : " + str(len(title)))

#panda dataframe
company = pd.DataFrame({'Company':title, 'Description':description, 'Location':location, 'Links':links, 'Sector':sector, 'Certified Date': crtf_date, 'Website': website,'Overall Score':overall_score, list(score.keys())[0]:score[list(score.keys())[0]],list(score.keys())[1]:score[list(score.keys())[1]],list(score.keys())[2]:score[list(score.keys())[2]],list(score.keys())[3]:score[list(score.keys())[3]],list(score.keys())[4]:score[list(score.keys())[4]], 'Honors': honors})

#Formatting data

company['Location'] = company['Location'].str.replace('Location: ','').astype(str)

company['Links'] = company['Links'].str.replace('/directory','https://bcorporation.net/directory').astype(str)


#add dataframe to csv file named 'company.csv'
company.to_csv('Bcorp.csv')

toc = time.perf_counter()
print(f"Downloaded the database in {toc-tic:0.4f} seconds")


