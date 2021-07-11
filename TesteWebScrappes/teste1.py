import requests
import requests
from bs4 import BeautifulSoup





#pegando url de teste

def testeSite():
        artigoDesejado = str(input('digite sua url'))
        url = artigoDesejado
        html = requests.get(url)
        if (html.status_code != 200):
                print(">>  Falha na requisição  <<")    
        else:
                print("Site ok. Entrando.")

                html_content = html.content
        soup = BeautifulSoup(html_content, "html.parser")
        indiceGeral = soup.find('div',attrs={'class':'toc'})
        indice = indiceGeral.find('ul')

        
        return indice.text
print(testeSite())
