import re
from pprint import pprint
texto = """<p>Frase 1</p> 
<p>Frase 2</p>
 <p>Frase 3</p> 
 <div>Frase 4</div>
"""
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto)) #forma gulosa
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto)) 
print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>',texto)) 
tags = print(re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)',texto)) 
pprint(tags)