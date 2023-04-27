""" This script will be a simple web scraper.
    I am setting it's default URL to https://scrapethissite.com/pages/
    and scanning for h3 with class "page-title"
""""

import requests
from bs4 import BeautifulSoup


def fetch_content(url):
 
