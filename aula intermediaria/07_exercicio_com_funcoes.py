'''
        EXERCICIOS COM FUNÇÕES
        
crie uma função que multiplica todos os argumentos nao nomeados recebidos
retorne o total para uma variavel e mostre o valor da variavel
'''
def multiplica(*args):
    total = 1
    for numero in args: # enquanto tiver numeros em args(a tupla passada para a função como argumento)
            total *= numero # vai multiplicar no total os numeros
    print('resposta da função; ',total)

print('resposta correta e esperada: ',1*2*3*4*5*6*7*8*9) # teste se esta retornado a respota correnta 
multiplica(1,2,3,4,5,6,7,8,9)
'''
crie uma função fala se um numero é par ou impar 
retorne se o numero é par ou impar'''

def par_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é PAR!')
    else:
        print(f'O número {numero} é ÍMPAR!')
        
par_impar(5)
par_impar(4)
par_impar(7)
par_impar(6)

