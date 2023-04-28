""" This script will be a simple web scraper.
    I am setting it's default URL to https://scrapethissite.com/pages/
    and scanning for h3 with class "page-title"
"""

import requests
from bs4 import BeautifulSoup

# get the entirety of the page's content

def fetch_content(url):
    content = requests.get(url)
    if content.status_code == 200:
        return content.text
    return None

# parse the HTML content

def parse_the_page(html):
    the_words = BeautifulSoup(html, "html.parser")
    return the_words

# get the titles, specifically

def extract_titles(the_words):
    titles_data = []
    titles = the_words.find_all("h3", class_="page-title")
    for title in titles:
        titlewords = title.get_text()
        titles_data.append(titlewords)
    return titles_data

#display the titles

def display_titles(titles_data):
    for title in titles_data:
        print(f"{title}\n")

# present data

if __name__ == "__main__":
    url = "https://scrapethissite.com/pages/"
    html = fetch_content(url)
    if html:
        the_words = parse_the_page(html)
        titles_data = extract_titles(the_words)
        display_titles(titles_data)
    else:
        print("couldn't fetch the titles")
