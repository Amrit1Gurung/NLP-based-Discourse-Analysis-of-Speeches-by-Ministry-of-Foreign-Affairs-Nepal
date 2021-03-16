"""
   @author: Amrit Gurung

"""i

mport re
import requests
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://mofa.gov.np/category/speech/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
speech_title = []
date_of_speech = []
contents = []
all_speech_links = []
for i in tqdm(range(1,17)):
  if i == 1:
    all_speech_blocks = soup.find_all('div', class_="entry-container")
    for block in all_speech_blocks:
      speech_link = block.find("a").get('href')
      speech_page = BeautifulSoup(requests.get(speech_link).content, 'html.parser')
      speech = speech_page.find("div", class_="entry-container")
      title = speech.find('h1').string
      date = speech.find('time').string
      content = speech.text
      speech_title.append(title)
      date_of_speech.append(date)
      contents.append(content)
      all_speech_links.append(speech_link)
  else:
    url = URL+"page/"+str(i)+"/"
    soup2 = BeautifulSoup(requests.get(url).content, 'html.parser')
    all_speech_blocks = soup2.find_all('div', class_="entry-container")
    for block in all_speech_blocks:
      speech_link = block.find("a").get('href')
      speech_page = BeautifulSoup(requests.get(speech_link).content, 'html.parser')
      speech = speech_page.find("div", class_="entry-container")
      title = speech.find('h1').string
      date = speech.find('time').string
      content = speech.text
      speech_title.append(title)
      date_of_speech.append(date)
      contents.append(content)
      all_speech_links.append(speech_link)
speech_df = pd.DataFrame()
speech_df['Date'] = list(date_of_speech)
speech_df['Title'] = list(speech_title)
speech_df['Speech'] = list(contents)
speech_df.to_csv('../data/speeches.csv')