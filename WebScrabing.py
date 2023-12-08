from bs4 import BeautifulSoup
import requests
import json

def get_souop(URL, jar=None):
    request_headers = {}


def page_name(soup):
  h2= soup.find("h2)
  if h2 is not None:
          return h2.text


def page_suraname(soup)
      th= soup.find("td", text="McGrath")
      if th is None:
       th= soup.find("td", text="mcGrath")
      if th is None:
      th = soup.find("td", text="Mcgrath)
     if th is not None:  
      age = th.findNext("th").text
      return age


Row (page_name(soup), page_surname(soup))

row
