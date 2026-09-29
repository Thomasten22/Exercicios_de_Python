'''Modulos padrão do Python (import, from, as e *)
https://docs.python.org/3/py-modindex.html  <-- biblioteca de imports do python
inteiros - import nome_modulo
vantagens: voce tem o namespace do modulo
desvantagens: nomes grandes'''

# import sys      # importando o modulo inteiro da biblioteca pelo pelo namespace

# plataform = 'variavel criada com o nome do modulo armazenando algo totalmente difente'

# print(sys.platform)         # normalmente vem acompanhada do comando que queremos exemplo sys.plataform (estamos colocando o nome do modulo e depois pedindo para executar algo)
# print(plataform)        # vai executar o que esta dentro da variavel pois nao esta acompanhado do sys

'''
partes - from nome_modulo import objeto1, objeto2
vantagens: nomes pequenos
desvantagens: sem o namespace do modulo'''

# from sys import platform, exit  # dessa maneira conseguimos importar apenas pedaços do modulo, como no exemplo so trouxemos plataform e exit 

# print(platform)

# dessa maneira podemos sobrescrever o nome do modulo e ele acaba pegando o que passamos para a variavel !!!!!!!!!! 


'''alias 1 - import nome_modulo as apelido'''
# mostrando que podemos alterar o nome do modulo por com o AS 

# import sys as s     #definimos que o nome do modulo é s

# sys = "variavel que pegou o nome do modulo " # variavel criada de exemplo para mostra que nao é o modulo 

# print(sys) 
# print(s.platform) # o modulo com apelido fazendo a função do sys

# NÃO É BOA PRATICA DE PROGRAMAÇÃO

'''alias 2 - from nome modulo import objeto as apelido
vantagens: voce pode reservar nomes para seu codigo
desvantagens: pode ficar fora do padrao da linguagem'''

#ESSE MEDOTO É COMUM ULTILIZAR EM NOMES MUITOS ESTENÇOS DE MODULOS
# from sys import exit as ex, plataform as pf     # Renomeei 2 modulos no mesmo import

# print (pf)      # esta requisitando o plataform pelo apelido pf

'''má pratica - from nome_modulo import * 
vantagens: importa tudo de um modulo 
desvantagens: importa tudo de um modulo
'''

# MÁ PRATICA DE PROGRAMAÇÃO !!!!!!!!!

# from sys import * # foi importados tudo do modulo e assim pode causar bagunça porque nao sabemos o que foi importado (podemos acabar reescrevendo algum comando / deixa o codigo obscuro)

# print(platform)