'''Interpolação basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF012345679)
'''

nome = 'Thomas'
preco = 1000.695897643
#variavel = 'Thomas, o preço total foi de R$: 1000.95' dessa maneira poderiamos ter passado tudo so que temos a maneira a baixo
variavel = '%s, o preço total foi de R$:%.2f' % (nome, preco)#dessa maneira conseguimos encurtar as digitações e a % ajuda a podermos informa os parametros(quando vamos informar somente um parametro nao precisa de parenteses) conseguimos indexar o valor do float colocando .2 e depois o f
print(variavel)
print('O hexadecimal de %d é %04x' % (15,15))# esse é um exemplo do Hexadecimal  o 04 sao para preencher casas do exadecimal, se caso for um numero que tenha mais letras elas irao aparecer, se nao for sera completado por 0
