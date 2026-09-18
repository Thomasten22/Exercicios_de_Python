'''
Metodos uteis dos dicionarios em Python:

len - quantas chaves 
key - iteravel com as chaves
values - iteravel com valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave 
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro

'''
pessoa = {
    'nome': 'Thomas',
    'sobrenome': 'Victor',
    'idade': 25,
    'altura': 1.85,
    'numeros': [1,2,3,4],
    'letra': 't'
}

#metodo len (. com  2 __ metodo e 2__ )

print(pessoa.__len__())

# metodo keys (retorna as chaves do dicionario como por exemplo o nome, sobrenome, idade e altura)(conseguimos alterar ele para list, tuple e entre outros)

print (pessoa.keys())

# forma de chamar as chaves com for 

for chave in pessoa:
    print(chave)

# values - iteravel com valores (retorna as valores do dicionario como por exemplo o nome, sobrenome, idade e altura)(conseguimos alterar ele para list, tuple e entre outros)

print(pessoa.values())

#for para chamar os valores 

for valores in pessoa.values():
    print(valores)

# items - iteravel com chaves e valores (chama os dois valores)

print(pessoa.items())

#for para chamar os valores 

for chave, valor in pessoa.items():
    print(chave,':', valor)

# setdefault - adiciona valor se a chave não existe

print(pessoa.setdefault('endereço', 'sem endereço'))

# copy - retorna uma copia rasa (shallow copy) (basicamente faz uma copia do dicionario, somente de valores mutaveis, ele nao acessa lista dentro de listas)
# conseguimos copiar de verdade importando a biblioteca (import copy) e passando a função como copy.deepcopy(pessoa) (copia profunda)

pessoa2 = pessoa.copy()

pessoa2['idade'] = 27   #resolve o problema de que se alterarmos algo do dicionario que recebeu a copia, o dicionario tambem é alterado

print('------ EXEMPLO .COPY() ------ ')
print('------ alterei o valor mutavel e alterou somente na 2 ------ ')
print(pessoa)
print(pessoa2)

# valores imutaveis sao alterados em ambas as listas

pessoa2['numeros'][2] = 500

print('------ alterei o valor imutavel e alterou nas duas ------ ')
print(pessoa)
print(pessoa2)

# get - obtem uma chave (altera caso nao exista a função passada para none)

print(pessoa.get('endereço1', None))
print(pessoa.get('nome'))

# pop - apaga um item com a chave especificada (del) (apaga um item com a chave e podemos fazer assim e colocar em outras variaveis)

num = pessoa.pop('numeros')

print(num)
print(pessoa)

# popitem - apaga o ultimo item adicionado ( apaga o ultima chave com item da lista)

ultima_chave = pessoa.popitem()
print(pessoa)

# update - atualiza um dicionario com outro

pessoa.update({
    'nome': 'Leticia',
    'sobrenome': 'Neves',
    'idade': 21,
    'altura': 1.68
})
#atualizou itens da lista trazendo novos parametros para as chaves

print(pessoa)

#podemos fazer dessa maneira
pessoa.update(letra= 'L')

print(pessoa)

#ou dessa maneira

tupla = ('letra', 'Thomas e Leticia'),
pessoa.update(tupla)

for chave, valor in pessoa.items():
    print(chave,'-', valor)