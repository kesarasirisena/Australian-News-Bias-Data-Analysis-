import requests as rq
from bs4 import BeautifulSoup
from time import sleep
from time import time
from random import randint
from warnings import warn
import json

import csv


#URL From Internet Archive 
#url = 'https://web.archive.org/cdx/search/cdx?url=abc.net.au/news/&collapse=digest&from=20200125&to=20210904&output=json'
url = 'https://web.archive.org/cdx/search/cdx?url=abc.net.au/news/&collapse=digest&from=20200125&to=20200126&output=json'
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
req = []

soup = []

titles = []





superlist1=[]

superlist2=[]




for i in range(0,len(final_url)): 
    req.append(rq.get(final_url[i]).text) 
    soup.append(BeautifulSoup(req[i],'lxml'))
    titles.append(soup[i].findAll("h3"))
    for title in titles:
        for subtitle in title:

            mydict = {} 
            
            mydict["Date"]=dates[i]
            mydict["Titles"]=subtitle.text
            
            superlist1.append(mydict["Date"])
            superlist2.append(mydict["Titles"])






# with open('abc.csv', 'w') as csv_file:  
#     writer = csv.writer(csv_file , delimiter=',')
#     writer.writerow(headers)
#     for i in superlist2:
#        writer.writerow([i])

headers = ["Date", "Titles"]
#Create CSV File
for i in range(0, len(superlist1)): 
    with open('abc.csv', 'w') as csvfile:   
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        writer.writerows(zip(superlist1, superlist2))
