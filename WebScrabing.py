from bs4 import BeautifulSoup
import requests
import json

def get_souop(URL, jar=None):
    request_headers = {}


def page_name(soup):
  h2= soup.find("h2)
  if h2 is not None:
          return h2.text
