"""
Scrape website to get data and create a csv with that data
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.audible.in/search?node=21881796031&sort=popularity-rank&ref=a_cat_Scien_c7_showmore&pf_rd_p" \
      "=b8365243-4d3c-4970-bc28-3a3fa316fce6&pf_rd_r=Z1MFCKKKF1C7ER2KTWSX&pageLoadId=XuzXsWylEkPnMHRp&creativeId" \
      "=fa240ef5-2ebf-4f43-b1b1-11c01bce5b1b "
response = requests.post(url)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

list_items = soup.select(selector="#center-3 .productListItem")

# with open("base_html_text.txt", mode="w", encoding="utf-8") as file:
#     file.write(f"{list_items[0]}")

audio_book = {}

for item in list_items:
    # headings.append(item.select(selector="h2")[0].getText())
    print(item.select(selector=".bc-list-item"))

