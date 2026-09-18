'''
Introdução ao desempacotamento + tuples(tuplas)

conseguimos desempacotar valores passando variaveis seguidas de virgulas( assim como o exemplo a baixo) e eles se alto denominam os valores da lita
nao podemos passar uma lista com ex 3 valores para 2 variaveis criadas nem vice e verso porque isso da valueError de quantidade erradas

para desempacotar com quantidade faltante e nao dar error podemos criar a variavel e com a quantidade que precisamos e depois passamos a variavel *resto que ela reempacota tudo 
'''

lista = ['Thomas', 'Leticia', 'Vicente'] # metodo 1 de desempacotamento de str, lista criada com 3 valores 
nome1, nome2, nome3 = lista #3 variaveis seguidas recebendo a lista

print(nome1,nome3,nome2)


nom, *resto = ['Thomas', 'Leticia', 'Vicente'] # metodo 2 de lista pegando primeiro nome e passando o nomes que sobraram para a variavel resto
# para pegar o nome2 ou 3 seria assim 
#resto, nom, *resto = .... # seria para acessar o segundo nome da variavel e ele entenderia que estamos esquecendo o numero da primeira variavel
#resto, resto, nom, *resto = .... # seria para acessar o tercerio nome da variavel e ele entenderia que estamos esquecendo o numero da primeira e segunda variavel

print(nom)

