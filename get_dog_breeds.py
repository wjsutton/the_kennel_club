import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thekennelclub.org.uk/search/breeds-a-to-z/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# extract data from dog breed cards
link = [x.get('href') for x in soup.find_all("a",{"class":"m-breed-card__link"}, href=True)]
title = [x.getText() for x in soup.find_all("strong",{"class":"m-breed-card__title"})]
category = [x.getText() for x in soup.find_all("div",{"class":"m-breed-card__category"})]
image = [x.get('src') for x in soup.find_all("img",{"class":"a-media__image"})]
details = [x.getText() for x in soup.find_all("dd",{"class":"m-breed-summary__value"})]
details_type = [x.getText() for x in soup.find_all("span",{"class":"m-breed-summary__key-label"})]

# initiate lists 
title_entry = []
category_entry = []
link_entry = []
image_entry = []

items = len(title)

# report metadata 10 times to match number of details
for i in range(items):
    title_entry = title_entry + [title[i]] * 10
    category_entry = category_entry + [category[i]] * 10
    link_entry = link_entry + [link[i]] * 10
    image_entry = image_entry + [image[i]] * 10

# convert lists into dataframe
df = pd.DataFrame()
df['title'] = title_entry 
df['category'] = category_entry 
df['link'] = link_entry 
df['image'] = image_entry 
df['details_type'] = details_type
df['details'] = details

# writing data to csv
df.to_csv('data\\Dog Breeds.csv', encoding="utf-8-sig", index=False)

