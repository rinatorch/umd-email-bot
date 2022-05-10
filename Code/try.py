# -*- coding: utf-8 -*-

#load packages
import requests
import bs4
import pandas as pd
import numpy as np
import re
import os
from slack import WebClient
from slack.errors import SlackApiError
import csv
from csv import DictWriter


URL = 'https://president.umd.edu/taxonomy/term/campus-messages'

#begin to extract and scrape
message_page = requests.get(URL)
soup = bs4.BeautifulSoup(message_page.text, 'html.parser')

results = []
divs = soup.find_all('umd-feed-item')

for div in divs:
    title = div.find('a').text
    datetime = div.find('time')['datetime']
    description = div.find('p').text.strip()
    url = div.find('a')['href']
    for h in divs:
        a = h.find('a')
        if 'href' in a.attrs:
            url = a.get('href')
        else:
            pass
    results.append({'url': url, 'title': title, 'datetime': datetime, 'description': description})

#results.to_csv('data.csv')
df = pd.DataFrame(results)
#print(df)
df.to_csv('data.csv')
