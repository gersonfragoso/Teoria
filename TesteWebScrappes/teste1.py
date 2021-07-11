import requests
import requests
import pandas as pd
from bs4 import BeautifulSoup
import selenium




#pegando url de teste

def testeSite():
        artigoDesejado = str(input('digite sua url'))
        url = artigoDesejado
        html = requests.get(url)
        if (html.status_code != 200):
                print(">>  Falha na requisição  <<")    
        else:
                print("Site ok. Entrando.")
                print("Site ok. Entrando..")  
                print("Site ok. Entrando...") 
                html_content = html.content
        soup = BeautifulSoup(html_content, "html.parser")
        indice = soup.findAll('ul')
        
        return indice
print(testeSite())


