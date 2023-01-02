"""
Scrape website to get data and create a csv with that data
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.audible.in/search?node=21881796031&sort=popularity-rank&ref=a_cat_Scien_c7_showmore&pf_rd_p" \
      "=b8365243-4d3c-4970-bc28-3a3fa316fce6&pf_rd_r=Z1MFCKKKF1C7ER2KTWSX&pageLoadId=XuzXsWylEkPnMHRp&creativeId" \
      "=fa240ef5-2ebf-4f43-b1b1-11c01bce5b1b "
response = requests.post(url)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

list_items = soup.select(selector="#center-3 .productListItem")

audio_book = [
    ["index", "title", "writer", "narrator", "stars"],
]

for item in list_items:
    book_content = item.select(selector=".bc-list-item")
    title = item.select(selector="h2")[0].getText()
    writer = ""
    narrator = ""
    rating = item.select(selector=".bc-text")[0].getText()
    for content in book_content:
        if content and "Written by:" in content.getText():
            writer = content.getText().replace("Written by:", "").replace("\n", "").strip()
        if content and "Narrated by:" in content.getText():
            narrator = content.getText().replace("Narrated by:", "").replace("\n", "").strip()

    audio_book.append([title, writer, narrator, rating,])

a_books = pd.DataFrame(audio_book)
a_books.to_csv("data/audible_audio_books.csv", header=False)
