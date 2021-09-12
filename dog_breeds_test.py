import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from pathlib import Path

url = "https://www.thekennelclub.org.uk/search/breeds-a-to-z/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#tbl = soup.find("table")
#data_frame = pd.read_html(str(tbl))[0]
link = soup.find("a",{"class":"m-breed-card__link"}, href=True)  
title = soup.find("strong",{"class":"m-breed-card__title"})  
category = soup.find("div",{"class":"m-breed-card__category"})  
image = soup.find("img",{"class":"a-media__image"})
details = soup.find("dd",{"class":"m-breed-summary__value"})  

elements = soup.select("a",{"class":"m-breed-card__link"})
print(elements[0]['href'])

#print(link)
#print(link[0]['href'])
print(image)
print(title)
print(category)
print(details)
