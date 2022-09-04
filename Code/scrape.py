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


#define URL
URL = 'https://president.umd.edu/taxonomy/term/campus-messages'

#begin to extract and scrape
message_page = requests.get(URL)
soup = bs4.BeautifulSoup(message_page.text, 'html.parser')


divs = soup.find_all('umd-feed-item')

titles = soup.find_all('h2', class_="normal-san-serif")

dates = soup.find_all('div', class_="extra-small-san-serif")

descs = soup.find_all('div', class_="rich-text")

url_list = []
for h in divs:
    a = h.find('a')
    if 'href' in a.attrs:
        url = a.get('href')
        url_list.append(url)
    else:
        pass

title_list = []
for title in titles:
    title = title.text
    title = re.sub("\n","",str(title))
    title_list.append(title)

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

#convert lists to data frame
df = pd.DataFrame(list(zip(date_list, title_list, desc_list, url_list)))

#add column titles
df.columns = ["Date","Title","Teaser","URL"]

#add csv_urls to dict
def get_urls():
    infile = open("data.csv", encoding='utf8', newline='')
    reader = csv.DictReader(infile)
    csv_urls = []
    for item in reader:
        csv_urls.append(item['URL'])
    return csv_urls

def sendSlackMsg():
#get unique/new url

    csv_urls = get_urls()
    for_message = [item for item in url_list if item not in csv_urls]
    df.to_csv('data.csv')
    for item in for_message:
    #turn that into a dict
        infile = open("data.csv", newline='')
        reader = csv.DictReader(infile)
        csv_titles = []
        csv_dates = []
        csv_desc = []

        for item in reader:
            csv_titles.append(item['Title'])
            csv_dates.append(item['Date'])
            csv_desc.append(item['Teaser'])

    #prep slack token

        slack_token = os.environ["SLACK_API_TOKEN"]
        client = WebClient(token=slack_token)
        ts_id = ""
        try:
          response = client.chat_postMessage(
            channel="news_desk",
            blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": f":rotating_light: New UMD email on {csv_dates[0]}:rotating_light:\n*{csv_titles[0]}*\nRead the teaser in :thread: or see <{for_message[0]}|the full email here.>\nSee recent <https://github.com/rinatorch/umd-email-bot/blob/main/Code/data.csv|emails here.>"}}]
          )
          ts_id = ts_id+response['ts']
        except SlackApiError as e:
          # You will get a SlackApiError if "ok" is False
          assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    for item in for_message:
        try:
            response = client.chat_postMessage(
            channel="news_desk",
            thread_ts=ts_id,
            blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": f"*Start reading*\n{desc_list[0]}\n<{for_message[0]}|*Read the full email here.*>\n<https://president.umd.edu/taxonomy/term/campus-messages|Explore all emails here.>"}}]
              )
        except SlackApiError as e:
          # You will get a SlackApiError if "ok" is False
          assert e.response["error"]


sendSlackMsg()
