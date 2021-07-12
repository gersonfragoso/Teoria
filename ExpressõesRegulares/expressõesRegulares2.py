#META CARACTERES : . ^ $ * + ?  { } [ ] | \ ( )
# | == OU 
# . QUALQUER CARACTERE (COM EXCEÇÃO DA QUEBRA DE LINHA (LETRA)) b.....a
# [] == CONJUTO DE CARACTERES [a-zA-z]aria
#flags=re.ignorecase or re.I , para desconsiderar as letras maiusculas e minusculas.
#* 0 ou n == jo*ão Vai acha Jooooão Jooão jão
#  + 1 ou n == jo+ão Vai acha Jooooão Jooão 
# ? 0 ou 1 jo?ão Vai acha João Jão 
#  {min,max } jo{3}ão{1} Vai acha Joooão Jooão João
#  ( ) groups        \1
# ()()          \1 \2
# (( )) ( )        \1 \2 \3 



import re
texto = """Estou acomodado em algum desses brancos bancos, o dia está fresco e a maré, alta, a estrada engarrafada, 
o brilho do sol muito intenso, esse cheiro da água salgada me lembra o 
peixe-carapau e eu aqui sem objectivo, só escrevo... devia escrever sobre essas palmeiras, 
porque elas me lembram os meus cadernos, porque estão cheias de folhas, eu continuo sorrindo sem motivo nenhum,
 aqui às pessoas também só correm sem motivo nenhum, até o tempo passa sem motivo nenhum, mas eu sinto que vai 
 sempre faltar algo, sempre faltou algo, por isso desapego-me..."""

print(re.findall(r"pessoas|algum|bran..s",texto))