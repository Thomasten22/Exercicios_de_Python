''' Introdução à função lambda (função anônima de uma linha)
 A função lambda é uma função como qualquer
 outra em Python. Porém, são funções anônimas
 que contém apenas uma linha. Ou seja, tudo
 deve ser contido dentro de uma única
 expressão.
 
 quando o python tenta organizar uma lista de nomes ele se refere pela tabela UNICODE e vai depender de como esta na lista
 https://www.charset.org/utf-8
 lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]
 lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
 lista.sort() # essa função .sort ela ordena uma lista, 
 lista.sort(reverse=True) #o reverse=True ordena em ordem decresente
 sorted(lista) # sorted () organina a partir da variavel '''
 
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
] # dicionario com dicionarios declarados dentro dele


def exibir(lista): # função para separar o dicionario de dicionarios esse é um jeito de fazer a ordenação 
    for item in lista:
        print(item)
    print() # esse print solto no pagode é para pular uma linha kkk


l1 = sorted(lista, key=lambda item: item['nome']) # essa função lambda serve para organizar o dicionario pelo que a gente defini e aqui esta por nome 
l2 = sorted(lista, key=lambda item: item['sobrenome']) # definida para organizar por sobrenome 

exibir(l1)
exibir(l2)

def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)