import pandas
from GetSoup import get_soup
from Busca import Busca  

url = "https://pt.wikipedia.org/wiki/Jo%C3%A3o_Pessoa"
def format_text(element):
    text = element.text.title()
    return text

events = {}
titles = []
dates = []



soup = get_soup(url)
found_titles = Busca(soup,"span", "class", "titulo-pagina") 
found_dates  = Busca(soup,"div", "class", "data-publicacao")