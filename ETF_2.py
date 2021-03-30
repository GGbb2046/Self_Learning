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
attr = ['overview', 'returns', 'risk']
data = []



html = BeautifulSoup(requests.get('https://etfdb.com/screener/#sort_by=assets&sort_direction=desc&page=95').content, 'html.parser').tbody.find_all('tr')


for container in html:    
    cols = container.find_all('td')
    data.append(cols)

p_overview="""
    ("Symbol.*[\n].*>)(?P<Symbol>[A-Z]+)  #Symbol
    (</a>[\n]</td>,\s<td\sdata-th="Name.*[\n].*>)(?P<Name>.*[A-Z])  #Name
    (</a>[\n]</td>,\s<td\sdata-th="Price.*[\n])(?P<Price>.*) #Price
    ([\n]</td>,\s<td\sdata-th="Assets.*[\n])(?P<Assets>.*) #Assets
    ([\n]</td>,\s<td\sdata-th="Average \ volume.*[\n])(?P<Volume>.*) #Volume
    ([\n]</td>,\s<td\sdata-th="Ytd.*[\n])(?P<YTD_Change>.*) #YTD change
    ([\n]</td>,\s<td\sdata-th="Overall.*[\n])(?P<Overall_rating>.*[a-z]>) #Rating
    ([\n]</td>,\s<td\sdata-th="Asset.*[\n])(?P<Class>.*[a-z]) #Class       
 
    """
out={}
for i in range(len(data)):
    for item in re.finditer(p_overview,str(data[i]),re.VERBOSE):
        print(item.groupdict())
