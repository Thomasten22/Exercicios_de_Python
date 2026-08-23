'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

            CODIGO DO PROFESSOR 
            
entrada = input('Digite um número: ')
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
    
    
'''
num = input('digite um numero: ')

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print('o numero informado é par')
    else:
        print('o numero informado é impar')
except:
    print('Numero informado não é um numero inteiro')


'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

             CODIGO DO PROFESSOR 
             
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
    
'''

hora = int(input('me diga a hora: '))
bom_dia = hora >= 0 and hora <= 11
boa_tarde = hora >= 12 and hora <= 17
boa_noite = hora >= 18 and hora <= 23

if bom_dia:
        print('Bom dia!!')
elif boa_tarde:
        print('Boa tarde!!')
elif boa_noite:
        print('Boa noite!!')
else:
    print('hora informada invalida!')
    
'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

                 CODIGO DO PROFESSOR 
                 
 nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')                


'''

nome = input('me fale seu nome: ')

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")