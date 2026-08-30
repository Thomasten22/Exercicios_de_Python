'''
Tipo tupla - uma lista Imutavel
'''
nomes = 'Thomas', 'Leticia', 'Carlos' #valor imutavel, e como a tupla ele nao consegue ser alterado >ISSO È UMA TUPLA<
print(nomes[0])
print(nomes)

'''alterando lista para tupla'''

nomes = ['Thomas', 'Leticia', 'Carlos' ] # esta formatado no tipo lista modo mutavel, conseguimos alterar itens dessa forma
nomes = tuple(nomes)#alterado para tupla e ficando imutavel e nao conseguimos alterar mais nada
print(nomes[0])
print(nomes)

'''alterando novamente para list'''
nomes = ['Thomas', 'Leticia', 'Carlos' ] # esta formatado no tipo lista modo mutavel, conseguimos alterar itens dessa forma
nomes = tuple(nomes)#alterado para tupla e ficando imutavel e nao conseguimos alterar mais nada
nomes - list(nomes) #alterei para modo lista novamente e podendo ser alterado
print(nomes[0])
print(nomes)
