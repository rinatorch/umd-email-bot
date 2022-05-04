##next step, remove newlines
import requests
import bs4
import pandas as pd
import numpy as np
import re
import os
from slack import WebClient
from slack.errors import SlackApiError
import csv
#import nltk
#import spacy
#from nltk import ne_chunk, pos_tag, word_tokenize
#from nltk.tree import Tree
#nlp = spacy.load("en_core_web_sm")



URL = 'https://president.umd.edu/taxonomy/term/campus-messages'

message_page = requests.get(URL)
soup = bs4.BeautifulSoup(message_page.text, 'html.parser')


#divs = []
divs = soup.find_all('umd-feed-item')
#print(divs)

titles = soup.find_all('h2', class_="normal-san-serif")
#print(titles)

dates = soup.find_all('div', class_="extra-small-san-serif")
#print(dates)

descs = soup.find_all('div', class_="rich-text")
#descs = soup.find_all('div', data-feed-item_="description")
#print(descs)


url_list = []
for h in divs:
    a = h.find('a')
    if 'href' in a.attrs:
        url = a.get('href')
        url_list.append(url)
    else:
        pass

text_list = []
for url in url_list:
    single_msg_page = requests.get(url)
    soup = bs4.BeautifulSoup(single_msg_page.text, 'html.parser')
    body_text = soup.find_all('section', id='section-body-text')
    for bodies in body_text:
        bodies = bodies.text
        bodies = re.sub("\n","",str(bodies))
        text_list.append(bodies)
        #print(bodies)
    #print(body_text)
    #for body_text
#print(text_list)


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
    date = re.sub("    ","",str(date))
    date_list.append(date)


desc_list = []
for desc in descs:
    desc = desc.text
    desc = re.sub("\n","",str(desc))
    desc = re.sub("                  ","",str(desc))
    desc_list.append(desc)



df = pd.DataFrame(list(zip(date_list, title_list, desc_list, url_list, text_list)))

#print(df)

def get_urls():
    infile = open("data.csv", encoding='utf8', newline='')
    reader = csv.DictReader(infile)
    csv_urls = []
    for item in reader:
        #print(item)
        csv_urls.append(item['3'])
    return csv_urls


#take links
#add to list


#print(url_list)

def sendSlackMsg():
#get unique/new urlpyth

    csv_urls = get_urls()
    for_message = [item for item in url_list if item not in csv_urls]
    df.to_csv('data.csv')
    for item in for_message:
    #turn that into a dict
        infile = open("data.csv", newline='')
        reader = csv.DictReader(infile)
        csv_titles = []
        csv_dates = []
    #plant
        for item in reader:
            csv_titles.append(item['1'])
            csv_dates.append(item['0'])

    #prep slack token

        slack_token = os.environ["SLACK_API_TOKEN"]
        client = WebClient(token=slack_token)

        try:
          response = client.chat_postMessage(
            channel="slack-bots",
            blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": f":rotating_light: New email on {csv_dates[0]}:rotating_light:\n*{csv_titles[0]}*\n<{for_message[0]}|Read it here.>"}}]
          )
        except SlackApiError as e:
          # You will get a SlackApiError if "ok" is False
          assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'



sendSlackMsg()

#df.to_csv('data.csv')
