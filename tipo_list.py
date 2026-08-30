'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i](CRUD)

Metodos uteis: 
    append - adciona um item ao final da lista
    insert - adciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas 

'''
#       01234
#      -54321
string = 'ABCDE' # 5 caracteres
lista = ['Thomas', 27, 1.85 , True] 
# exemplo de list é passado dentro de conchetes e conseguimos passar varios tipo de variaveis de varios tipos str, int, bool e float conseguimos criar lista dentro de outra lista 
"""TESTE COM A VARAIVEL VAZIA DO TIPO LIST
lista = [] 
lista.append (input('diga seu nome: ')) # para adcionarmos itens numa variavel vazia tipo list usamos a .append e nao precisamos colocar o sinal de igual (sinal que recebe algo) so passr o input entre parenteses
lista.append (int(input('diga sua idade: ')))
lista.append (float(input('diga sua altura: ')))
"""
del lista[3] # modo de apagar o indice da lista que é o True

lista.append(valor) # adiciona um item ao final da lista 

lista.pop() # remove o ultimo item da lista 

print(f'meu nome é {lista[0]}, minha idade é {lista[1]}, '\
    f'tenho {lista[2]:.2f} de altura.')
'''aqui vemos que no print a cima estamos acesando as variaveis do da variavel list, acessando elas pelo conchetes e o numero do que foi declarado

        CUIDADOS COM DADOS MUTAVEIS
    = - copiado o valor (imutaveis)
    = - aponta o mesmo valor na memoria (mutavel)
    
    for funciona com listas normalmente 
'''