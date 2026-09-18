'''Operadores in e not in
string sao iteráveis
 0 1 2 3 4 5
 O t á v i o
-6-5-4-3-2-1

explicação'''

nome = 'Thomas' #essa foi a variavel

print(nome[2]) #vai retornar 'o' porque esta posicionada na 3 letra do meu nome como é feito a contagem (T=0, H=1 ,O=2)
print(nome[-4]) #vai retornar 'o' porque esta posicionada na -4 letra do meu nome como é feito a contagem (S=-1, A=-2, M=-3, O=-4)
print('o' in nome) #retorna True porque o 'O' esta no meu nome
print('v' in nome) #retorna false porque o 'V' nao esta no meu nome
print('Tho' in nome)#retorna True porque o 'THO' esta no meu nome
print('zero' in nome) #retorna False porque o 'zero' nao esta no meu nome 
'''
basicamente ele faz contagens de letras nas strings e consegue retornar elas por meio de [] com o numero desiginado ou checagem de existencia das palavas
ou letras nas string e verifica se é True (que existe na palavra) ou False (pela ausencia na palavra)
'''
'''
basicamente o Operador 'not in' faz o contrario , se colocarmos not in 'Tho' ele vai retornar false porque no meu nome existe essas 3 letras
'''
print('Tho' not in nome)#retorna False porque o 'THO' esta no meu nome
print('zero' not in nome) #retorna True porque o 'zero' nao esta no meu nome 

'''
    CODIGO ESCRITO PELO PROFESSOR NA AULA:
    
nome = input('DIgite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} está em {nome}')
'''
'''
teste da aula 44
numero = 10

if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')'''