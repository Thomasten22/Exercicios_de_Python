'''
List comprehension em Python
List comprehension é uma forma rapida para criar lista a partir de iteraveis.
'''
''' JEITO QUE SABIAMOS PARA CRIAR UMA LISTA COM NUMEROS'''
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []

for numero in range(10):
    lista.append(numero)

print(f'Jeito antigo de criar uma lista rapida: {lista}')

# NOVA MANEIRA SIMPLIFICADA PARA CRIAR UMA LISTA RAPIDA COM LIST COMPREHENSION

lista1 = [numero for numero in range(11)] # dessa maneira criei o for do exemplo acima em uma linha o numero antes do for é a variavel declarada dentro da propria 
#da pra fazer contas dentro desse metodo passado a cima (lista1 = [numero * 2 for numero in range(11)]) dessa maneira pegariamos o numero e multiplica ele por 2
print(f'novo metodo de fazer listas rapidas: {lista1}')

# MAPEAMENTO DE DADOS EM LIST COMPREHENSION
# na esquerda do for é o local que devemos colocar o mapeamento

produtos = [
    {'nome': 'arroz','preco': 30,},
    {'nome': 'feijao','preco': 10,},
    {'nome': 'batata','preco': 12.9,},
]

novos_produtos = [produto for produto in produtos]

produtos_preco_atualizado = [
    {**produto, 'preco': produto['preco'] * 1.20}# maneira de acessar uma chave e alterar o valor no exemplo estou alterando o valor dos precos para 20% a mais 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos]

print(novos_produtos, sep='\n')
print()
print(produtos_preco_atualizado)

# FILTRO DE DADOS EM LIST COMPREHENSION
# na direita do for é o local que devemos colocar o filtro

# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)