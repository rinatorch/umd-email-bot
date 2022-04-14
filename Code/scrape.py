##next step, remove newlines
import requests
import bs4
import pandas as pd
import numpy as np
import re

URL = 'https://president.umd.edu/taxonomy/term/campus-messages'

message_page = requests.get(URL)
soup = bs4.BeautifulSoup(message_page.text, 'html.parser')

divs = []
divs = soup.find_all('div', class_="feed-item")

titles = soup.find_all('h2', class_="feed-item-title")

dates = soup.find_all('div', class_="feed-item-date")

descs = soup.find_all('div', class_="feed-item-description")

#print(divs)
url_list = []
for h in divs:
    a = h.find('a')
    if 'href' in a.attrs:
        url = a.get('href')
        url_list.append("https://president.umd.edu" + url)
    else:
        pass
#for elements in div:
    #title = soup.find('div', class_="feed-item-title")

#for div in divs:
    #print(div.text)
#print(titles)

title_list = []
for title in titles:
    title = title.text
    title = re.sub("\n","",str(title))
    title_list.append(title)

#for item in title_list:
    #item = re.sub("\n","",str(item))



date_list = []
for date in dates:
    date = date.text
    date = re.sub("\n","",str(date))
    date_list.append(date)


desc_list = []
for desc in descs:
    desc = desc.text
    desc = re.sub("\n","",str(desc))
    desc_list.append(desc)
#print(desc_list)
#print(title_list)

#df = pd.DataFrame (title_list, columns = ['subjects'])
#print (df)

df = pd.DataFrame(zip(date_list, title_list, desc_list, url_list))
columns=['date','subject', 'desc', 'url']
print(df)

df.to_csv('data.csv')

"""
for date in dates:
    print(date.text)

for desc in descs:
    print(desc.text)

"""
