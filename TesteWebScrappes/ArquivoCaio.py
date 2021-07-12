import requests
import requests
from bs4 import BeautifulSoup
import re

def testeSite(link): #Testando se tem conexão com a intenet ou se o site está online
        ehValido = False       
        html = requests.get(link)        
        if (html.status_code != 200):
                print(">>       Falha na requisição  <<") 
                return ehValido == False   
        else:
                print(">>       Conexão OK           <<")
                return ehValido == True  
       
def testeLink(link): #Testando se o link é da wikipedia
        ehValido = False
        if re.match('( *?https{0,1}:\/\/?...*?wikipedia.org\/wiki\/*| *?...wikipedia.org\/wiki\/)', link):
                print(">>       Link Valido          <<")
                return ehValido == True    
        else:
                print(">>       Link Invalido        <<")
                return ehValido == False
       
requestOk = False
ehWiki = False
while True:
        artigoDesejado = str(input('    Digite sua url: ')) #pegando url
        ehWiki = testeLink(artigoDesejado)
        if not ehWiki:
                requestOk = testeSite(artigoDesejado)
        if not requestOk and not ehWiki:
                break     
        else:
                print('Verifique o link e tente novamente')

qualSeuDesejo = int(input('     Você deseja buscar por: \n'
+'       1 - Indices \n'
+'       2 - Referencias \n'
+'       3 - Imagens \n'
+'      Escolha sua opção:'))

html = requests.get(artigoDesejado)
html_content = html.content
soup = BeautifulSoup(html_content, "html.parser")

if qualSeuDesejo == 1 :
        indiceGeral = soup.find_all('span',{'class':'toctext'})
        indicesRegex = re.compile(r'\>\w*\<' ) 
        indices = re.findall(indicesRegex , str(indiceGeral))
        indicesSemSimbolos = re.sub('[<>]', '', str(indices))
        print(indicesSemSimbolos)

if qualSeuDesejo == 2 :
       artigo = soup.find_all('a',  {"class":"mw-redirect"}) 
       linkRegex = re.compile(r'\/wiki\/\S*' ) 
       link = re.findall(linkRegex , str(artigo))
       linksemAspas = re.sub('["]', '', str(link))
       linkSemRepeticao =  list(set(linksemAspas))
       print(linkSemRepeticao)
             
if qualSeuDesejo == 3 :
       artigo = soup.find_all('div',  {"id": "bodyContent"}) 
       imgRegex = re.compile(r'\w+\.jpg|\:\w+\.png|\w+\.svg' ) 
       imagem = re.findall(imgRegex , str(artigo))
       imagensSemRepeticao =  list(set(imagem))
       print(imagensSemRepeticao)
