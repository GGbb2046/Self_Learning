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


html = BeautifulSoup(requests.get('https://etfdb.com/screener/').content, 'html.parser').tbody.find_all('tr')

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
    """

p_returns="""
    ("Symbol.*[\n].*>)(?P<Symbol>[A-Z]+)  #Symbol
    (</a>[\n]</td>,\s<td\sdata-th="Name.*[\n].*>)(?P<Name>.*[A-Z])  #Name
    (</a>[\n]</td>,\s<td\sdata-th="1\sWeek.*[\n])(?P<One_Week>.*) #1 Week
    ([\n]</td>,\s<td\sdata-th="4\sWeek.*[\n])(?P<Four_Week>.*) #4 Week
    ([\n]</td>,\s<td\sdata-th="YTD.*[\n])(?P<YTD>.*) #YTD
    ([\n]</td>,\s<td\sdata-th="1\sYear*[\n])(?P<One_Year>.*) #1 Year 
    ([\n]</td>,\s<td\sdata-th="3\sYear*[\n])(?P<Three_Year>.*) #3 Year
    ([\n]</td>,\s<td\sdata-th="5\sYear*[\n])(?P<Five_Year>.*) #5 Year
    """
p_risks="""
    ("Symbol.*[\n].*>)(?P<Symbol>[A-Z]+)  #Symbol
    (</a>[\n]</td>,\s<td\sdata-th="Name.*[\n].*>)(?P<Name>.*[A-Z])  #Name
    (</a>[\n]</td>,\s<td\sdata-th="Standard\sDeviation.*[\n])(?P<STDEV>.*) #STDEV
    ([\n]</td>,\s<td\sdata-th="P/E\sRatio.*[\n])(?P<PE_Ratio>.*) #PE_ratio
    ([\n]</td>,\s<td\sdata-th="Beta.*[\n])(?P<Beta>.*) #Beta
    ([\n]</td>,\s<td\sdata-th="5-Day\sVolatility*[\n])(?P<5Day_Vol>.*) #5_Day_Vol 
    ([\n]</td>,\s<td\sdata-th="20-Day\sVolatility*[\n])(?P<20Day_Vol>.*) #20_Day_Vol
    ([\n]</td>,\s<td\sdata-th="50-Day\sVolatility*[\n])(?P<50Day_Vol>.*) #50_Day_Vol
    ([\n]</td>,\s<td\sdata-th="200-Day\sVolatility*[\n])(?P<200Day_Vol>.*) #200_Day_Vol
    """


for i in range(len(data)):
    for item in re.finditer(p_overview,str(data[i]),re.VERBOSE):
        print(item.groupdict())
            
            #heading = (re.findall('["].*(?=\")',str(data[i][j])))[0][1:]
            #splt = (re.split('\n',str(data[i][j])))
            #parts = (re.split('td data-th="',str(splt)))[1]
            #r1 = re.sub('["<>/\.!?]',"",str(parts))
            #r2 = re.sub('a href=etf',"",str(r1))
            #r3 = re.sub("Overall rating', 'a class=restricted href=membersjoina","",str(r2))[:(len(r2)-7)]

    #("Symbol.*[\n].*>)(?P<Symbol>[A-Z]+)  #Symbol
    #(</a>[\n]</td>,\s<td \s data-th="Name.*[\n].*>)(?P<Name>.*[A-Z])  #Name
    #("Price.*[\n])(?P<Price>.*) #Price
    #("Assets.*[\n])(?P<Assets>.*) #Assets
    #("Average \ volume.*[\n])(?P<Volume>.*) #Volume
    #("Ytd.*[\n])(?P<YTD_Change>.*) #YTD change
    