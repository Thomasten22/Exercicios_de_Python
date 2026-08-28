'''calculadora com while'''
while True:
    
    num1 = input(" digite um numero: " )
    num2 = input(" digite um numero: " )
    conta = input('qual a conta desejada(+, -, /, *): ')
    
    num_validos = None
    try:
        num1 = int(num1)
        num2 = int(num2)
        num_validos = True
    except:
       # num_validos = None
    #if num_validos is None:
        print('um ou os dois numeros estão digitados errados!')
        continue
    
    conta_permitidas = '+-*/'

    if conta not in conta_permitidas:
            print('o operador de conta digitado está incorreto!')
            continue
        
    if len(conta) >1:
            print('digitou operadores demais')
            continue
       
    if conta == '+':
            print('o valor da soma é :', num1 + num2)
    elif conta == '-':
            print('o valor da subtração é :', num1 - num2) 
    elif conta == '/':
            print('o valor da divisão é :', num1 // num2)
    elif conta == '*':
            print('o valor da multiplicação é :', num1 * num2)  

    sair = input('Quer sair?[s]im: ').lower().startswith('s')
    if sair is True:
        print('Saiu')
        break
