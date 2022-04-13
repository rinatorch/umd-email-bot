##next step, remove newlines

import requests
import bs4
import pandas as pd
import numpy as np

URL = 'https://president.umd.edu/taxonomy/term/campus-messages'

message_page = requests.get(URL)
soup = bs4.BeautifulSoup(message_page.text, 'html.parser')

divs = []
divs = soup.find_all('div', class_="feed-item")

titles = soup.find_all('h2', class_="feed-item-title")

dates = soup.find_all('div', class_="feed-item-date")

descs = soup.find_all('div', class_="feed-item-description")


#for elements in div:
    #title = soup.find('div', class_="feed-item-title")

#for div in divs:
    #print(div.text)
#print(titles)

title_list = []
for title in titles:
    title_list.append(title.text)

date_list = []
for date in dates:
    date_list.append(date.text)
#print(date_list)

desc_list = []
for desc in descs:
    desc_list.append(desc.text)
#print(desc_list)
#print(title_list)

#df = pd.DataFrame (title_list, columns = ['subjects'])
#print (df)

df = pd.DataFrame(zip(date_list, title_list, desc_list))
columns=['date','subject', 'desc']
print(df)

df.to_csv('data.csv')

"""
for date in dates:
    print(date.text)

for desc in descs:
    print(desc.text)

"""
