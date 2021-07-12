import re
acharPalavra = str(input("Qual palavra deseja encontrar: "))
string = "Expressões regulares em Python - Aprenda a utilizar expressões regulares em Python.Fala pessoal, tudo bem? Esse vídeo é uma seção bônus do meu curso de Python que resolvi disponibilizar aqui no Youtube também. São 14 vídeos em uma playlist com muito assunto sobre as expressões regulares (está super completo). Você pode acompanhar a playlist em ordem no link a seguir, todos os vídeos já estão disponíveis:"
pesquisa = re.compile(acharPalavra)
print(pesquisa.search(string))
print(pesquisa.findall(string))
substituir = str(input("para qual palavra você deseja substituir: "))
print(pesquisa.sub(substituir,string))