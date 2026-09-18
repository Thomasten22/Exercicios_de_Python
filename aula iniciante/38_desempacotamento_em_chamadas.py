'''
Desempacotamento em chamadas de metodos e funções
colocar o *antes da variavel no print conseguimos desempacotar ele e ficar melhor o entendimento
'''
string = 'ABCD'
lista = ['Maria','João', 'Eduarda']
tupla = 'Python', 'é', 'FODA'

a, b, c = lista
#esse é o metodo de desempacotamento por chamada
print(*string)
print(*lista)
print(*tupla)