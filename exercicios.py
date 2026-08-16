'''
>Faça um programa que verifique se uma letra digitada é vogal ou consoante.<


letra = input('Diga uma letra: ').lower()

if not letra.isalpha():
    print('Digite apenas uma letra!')
elif letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')
    
'''


'''
>Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:


F - Feminino
M - Masculino
Sexo Inválido.<


sexo = str(input('digite seu sexo: '))

if sexo == 'f' or sexo == 'F':
    print('Feminino')
elif sexo == 'm' or sexo == 'M':
    print('Masculino')
else:
    print('Sexo invalido!')
    
    
'''


'''
>Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.<


num = int(input('me informe um valor: '))

if num >= 0:
    print('Positivo')
else:
    print('Negativo')
'''
'''
>Faça um programa que peça dois números e imprima o maior deles<.


num1 = int(input('me diga um numero: '))
num2 = int(input('me diga um numero: '))

if num1 > num2:
    print(f'O numero {num1} é o numero maior')
else:
    print(f'O numero {num2} é o numero maior')
'''  
'''
>Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.<


nota1 = float(input('Me fale tua primeira nota: '))
nota2 = float(input('Me fale tua segunda nota: '))
nota3 = float(input('Me fale tua terceira nota: '))
media = ( nota1 + nota2 + nota3) / 3

print(f'sua media de nota é {media:.1f}')

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado, estude mais!')
'''
'''
>Faça um programa que leia três números e mostre o maior deles:<


num1 = int(input('diga-me um numero: '))
num2 = int(input('diga-me outro numero: '))
num3 = int(input('diga-me mais um numero: '))

maior = max(num1,num2,num3)

print(f'o maior numero é {maior}')
'''
'''
>Faça um programa que leia três números e mostre o maior e o menor deles:<


num1 = int(input('diga-me um numero: '))
num2 = int(input('diga-me outro numero: '))
num3 = int(input('diga-me mais um numero: '))

maior = max(num1,num2,num3)
menor = min(num1,num2,num3)

print(f'o maior numero é {maior} e o menor é {menor}')
'''

'''>Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:<

PRIMEIRA RESOLÇÂO FEITA POR MIM 

prod1 = float(input('qual o valor do primeiro produto: '))
prod2 = float(input('qual o valor do segundo produto: '))
prod3 = float(input('qual o valor do terceiro produto: '))

menor = min(prod1,prod2,prod3)

print(f'a melhor opção para compra é o produto {menor:.2f}')

SEGUNDA RESOLUÇÃO CRIADA PELO GEMINI PARA DIRECIONAR O NOME DO PRODUTO

prod1 = float(input('Qual o valor do primeiro produto: '))
prod2 = float(input('Qual o valor do segundo produto: '))
prod3 = float(input('Qual o valor do terceiro produto: '))

menor = min(prod1, prod2, prod3)

# Identifica qual produto tem esse menor valor
if menor == prod1:
    opcao = "primeiro"
elif menor == prod2:
    opcao = "segundo"
else:
    opcao = "terceiro"

print(f'A melhor opção é o {opcao} produto, custando R$ {menor:.2f}.')

'''