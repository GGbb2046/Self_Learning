from lxml import html
import csv
import requests
from requests import get
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import time
from tqdm import tqdm 
import re
import unicodedata

tic = time.perf_counter()

#initiate data storage

# with open('ETF.csv','r') as ETF:
#    reader = csv.reader(ETF)
#    for row in reader:
#        print(row)


html = BeautifulSoup(requests.get('https://etfdb.com/etf/VGT/#etf-ticker-profile').content, 'lxml').find('div',class_= 'col-sm-6 col-xs-12').find_all('span')

#a = re.sub('<span>|</span>|<span class=\"(.*?)\">|</a>|<a href=\"(.*?)\">|[\n]',"",str(html))

b = re.sub('[\n]',"",str(html))


keys = []
values = []
for item in re.finditer("<span>(.*?)</span>",str(b)):
    keys.append(re.sub("'","",re.sub('[(|,)]',"", str(item.groups()))))

for item in re.finditer('<span class.*?>(.*?)</span>',str(b)):
    values.append(re.sub("'","",re.sub('<a href=".*/.*">|</a>|["(|,)]',"",str((item.groups())))))

#for i in keys:
    #keys[i] = keys[i][1:(len(keys[i])-1)]

print(keys)
print(values)





    











'''print(html)
print(a)
for i in range(0,len(Attributes)):
    b = a.find(Attributes[i])
    l=len(Attributes[i])
    c = int(b)+int(l)+2
    print(c)
    print(a[c:(a.find(Attributes[i+1]))])'''


