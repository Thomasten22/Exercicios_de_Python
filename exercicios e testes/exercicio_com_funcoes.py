# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplicado(numero):
    return numero * 2
def triplicado(numero):
    return numero * 3
def quadruplicado(numero):
    return numero * 4

num = int(input('diga me um numero: '))

resultado = duplicado(num)
resultado2 = triplicado(num)
resultado3 = quadruplicado(num)

print(f'numero duplicado: {resultado}, numero triplicado: {resultado2}, numero quadruplicado: {resultado3}')
