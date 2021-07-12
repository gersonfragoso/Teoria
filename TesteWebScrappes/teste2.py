import requests
import requests
from bs4 import BeautifulSoup
import re

def testeSite(link):
        ehValido = False       
        html = requests.get(link)        
        if (html.status_code != 200):
                print(">>  Falha na requisição  <<") 
                return ehValido == False   
        else:
                print(">> Conexão OK <<")
                return ehValido == True  
       

  
        
       

def testeLink(link):       
        ehValido = False
        if re.match('( *?https{0,1}:\/\/?...*?wikipedia.org\/wiki\/*| *?...wikipedia.org\/wiki\/)', link):
                print(">>  Link Valido  <<")
                return ehValido == True    
        else:
                print(">>  Link Invalido  <<")
                return ehValido == False
       


def pegandoIndici():

    requestOk = False
    ehWiki = False
    while True:
            artigoDesejado = str(input('digite sua url: '))
            ehWiki = testeLink(artigoDesejado)
            if not ehWiki:
                    requestOk = testeSite(artigoDesejado)
            if not requestOk and not ehWiki:
                    break     
            else:
                    print('Verifique o link e tente novamente')

    html = requests.get(artigoDesejado)
    html_content = html.content
    soup = BeautifulSoup(html_content, "html.parser")
    indiceGeral = soup.find('div',attrs={'class':'toc'})
    indice = indiceGeral.find('ul')

    print(' Listando Indices')
    print(indice.text)
print(pegandoIndici())