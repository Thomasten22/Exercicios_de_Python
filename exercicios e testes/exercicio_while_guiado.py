'''crie um metodo while que repasse letra por letra do nome ate acabar
'''

nome = input('qual seu nome? ')
qtd_letra = len(nome)
contador = 0

while contador < qtd_letra :
    print('*', nome[contador],'*')
    contador += 1

print('acabou')


'''codigo do professor 

nome = input('qual seu nome? ')  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
'''


