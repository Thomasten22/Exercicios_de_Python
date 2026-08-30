''' 
exiba o indice da lista
0 maria
1 joao
2 helena
'''

lista = ['thomas', 'joao', 'Leticia', 'Henry', 'Lucca', 'Camilo', 'Valeria' ]
contador = 0

while contador < len(lista):
    for nome in lista:
        print(contador, nome)
        contador += 1
        


