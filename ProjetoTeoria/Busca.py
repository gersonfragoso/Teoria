import requests as rq
from bs4 import BeautifulSoup

def Busca(soup,tag,identifier,desc):
    event_found = soup.findAll(tag, {identifier: desc})
    return event_found 