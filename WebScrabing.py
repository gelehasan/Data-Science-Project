from bs4 import BeautifulSoup
import requests
import json

def get_souop(URL, jar=None):
    request_headers = {}
