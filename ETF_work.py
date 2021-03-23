import requests
from requests import get
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import time
from tqdm import tqdm 
import re

tic = time.perf_counter()

#initiate data storage

data = []
rows = BeautifulSoup(requests.get('https://etfdb.com/screener/#page=1').content, 'html.parser').tbody.find_all('tr')

for container in rows:    
    cols = container.find_all('td')
    data.append(cols)

pattern="""
("Symbol.*[\n].*>)(?P<Symbol>[A-Z]+)  #Symbol
(</a>[\n]</td>,\s<td \s data-th="Name.*[\n].*>)(?P<Name>.*[A-Z])  #Name
(</a>[\n]</td>,\s<td \s data-th="Price.*[\n])(?P<Price>.*) #Price
([\n]</td>,\s<td \s data-th="Assets.*[\n])(?P<Assets>.*) #Assets
([\n]</td>,\s<td \s data-th="Average \ volume.*[\n])(?P<Volume>.*) #Volume
([\n]</td>,\s<td \s data-th="Ytd.*[\n])(?P<YTD_Change>.*) #YTD change
"""

for i in range(len(data)):
    for item in re.finditer(pattern,str(data[i]),re.VERBOSE):
        print(item.groupdict())
        
        #heading = (re.findall('["].*(?=\")',str(data[i][j])))[0][1:]
        #splt = (re.split('\n',str(data[i][j])))
        #parts = (re.split('td data-th="',str(splt)))[1]
        #r1 = re.sub('["<>/\.!?]',"",str(parts))
        #r2 = re.sub('a href=etf',"",str(r1))
        #r3 = re.sub("Overall rating', 'a class=restricted href=membersjoina","",str(r2))[:(len(r2)-7)]

print(str(data[0]))
#("Symbol.*[\n].*>)(?P<Symbol>[A-Z]+)  #Symbol
#(</a>[\n]</td>,\s<td \s data-th="Name.*[\n].*>)(?P<Name>.*[A-Z])  #Name
#("Price.*[\n])(?P<Price>.*) #Price
#("Assets.*[\n])(?P<Assets>.*) #Assets
#("Average \ volume.*[\n])(?P<Volume>.*) #Volume
#("Ytd.*[\n])(?P<YTD_Change>.*) #YTD change

#