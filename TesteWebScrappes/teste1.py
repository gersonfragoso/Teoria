import re
import requests
import requests
from bs4 import BeautifulSoup





#pegando url de teste

def testeSite():
        artigoDesejado = str(input('digite sua url'))
        url = artigoDesejado
        html = requests.get(url)
        urlChecking = re.compile(html)
        if (urlChecking.seach(r'?https{0,1}:\/\/?...?wikipedia.org\/wiki\/*| *?...wikipedia.org\/wiki\/')):
                if(urlChecking.seach(i)==True):

                        print("Site ok. Entrando.")

                        html_content = html.content
                
                    
        elif(html.status_code != 200):
                print(">>  Falha na requisição  <<")
        
        else:
                print("Url está errada")

        soup = BeautifulSoup(html_content, "html.parser")
        indiceGeral = soup.find('div',attrs={'class':'toc'})
        indice = indiceGeral.find('ul')
        
        
        return indice.text
print(testeSite())

