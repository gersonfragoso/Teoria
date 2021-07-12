import requests
import requests
from bs4 import BeautifulSoup
import re

def testeSite(link): #Testando se tem conexão com a intenet ou se o site está online
        ehValido = False       
        html = requests.get(link)        
        if (html.status_code != 200):
                print(">>  Falha na requisição  <<") 
                return ehValido == False   
        else:
                print(">> Conexão OK <<")
                return ehValido == True  
       
def testeLink(link): #Testando se o link é da wikipedia
        ehValido = False
        if re.match('( *?https{0,1}:\/\/?...*?wikipedia.org\/wiki\/*| *?...wikipedia.org\/wiki\/)', link):
                print(">>  Link Valido  <<")
                return ehValido == True    
        else:
                print(">>  Link Invalido  <<")
                return ehValido == False
       

requestOk = False
ehWiki = False
while True:
        artigoDesejado = str(input('digite sua url: ')) #pegando url
        ehWiki = testeLink(artigoDesejado)
        if not ehWiki:
                requestOk = testeSite(artigoDesejado)
        if not requestOk and not ehWiki:
                break     
        else:
                print('Verifique o link e tente novamente')

qualSeuDesejo = int(input('Você deseja buscar por: \n'
+'1 - Indices \n'
+'2 - Referencias \n'
+'3 - Imagens \n'))


if qualSeuDesejo == 1 :
        html = requests.get(artigoDesejado)
        html_content = html.content
        soup = BeautifulSoup(html_content, "html.parser")
        #soup.find_all()
        indiceGeral = soup.find('div',attrs={'class':'toc'})
        indice = indiceGeral.find('ul')

        print(' Listando Indices')
        print(indice.text)

if qualSeuDesejo == 2 :
       print('nada ainda')

if qualSeuDesejo == 3 :
        print('nada ainda')