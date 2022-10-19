import requests as rq
from bs4 import BeautifulSoup
from time import sleep
from time import time
from random import randint
from warnings import warn
import json
import csv

#URL From Internet Archive 
url = 'https://web.archive.org/cdx/search/cdx?url=https://www.nine.com.au/&collapse=digest&from=20210905&to=20211009&output=json'
#Get All URLS
urls = rq.get(url).text
parse_url = json.loads(urls) 
#Initialise lists 
final_url=[]

dates = []
#Append final urls and all dates to respective lists 
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = tstamp+'/'+orig_url
    final_url.append('https://web.archive.org/web/'+waylink)
    dates.append(tstamp)
#Initialise lists 

titles = []  
req = []
soup = []


mydict = {}

for i in range(0,len(final_url)): 
    req.append(rq.get(final_url[i]).text) 
    soup.append(BeautifulSoup(req[i],'lxml'))
    titles.append(soup[i].findAll("h3"))
    for title in titles:
        for subtitle in title:
            mydict[subtitle.text] = dates[i]
    titles = []  
         


headers = ["Date", "Titles"]

with open('news.csv', 'a') as csvfile:   
        writer=csv.writer(csvfile, delimiter=',')
        #writer.writerow(headers)
        for i in mydict.keys(): 
    
            
            temp1 = mydict[i]
            temp2 = i
            writer.writerow([temp1, temp2])