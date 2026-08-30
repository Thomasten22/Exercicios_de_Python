'''explicação de enumarate - inumera iteraveis (indices)'''

lista = ['thomas', 'joao', 'Leticia', 'Henry', 'Lucca', 'Camilo', 'Valeria' ]
lista.append('Henrique')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)