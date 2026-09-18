'''
Faça uma lista de compras com listas
O usuario deve ter a posibilidade de inserir, apagar e lista valores da lista
Não permita que o programa quebre com erros de indices inexistentes na lista'''

compras = [] #lista de compras

while True:
    
    print('Selecione uma Opção: ')
    opcoes = input('[l]istar [a]pagar [i]nserir: ').lower() # valor que determina o que devemos fazer com a lista
    
    opcoes_permitidas = 'lai' # verificador se as escolhas estao certas, e se foi escolhido apenas 1 opção
    if opcoes not in opcoes_permitidas:
                print('Opção escolhida está errada!')
                continue # retorna o laço do inicio
            
    
    if opcoes == 'l': # verificador de escolha da letra 'l'
        if len(compras) == 0:  # verifica quantas coisas tem na lista e se for 0 retorna nada a listar
            print('Nada para listar')
            
        else:       # se tem itens na lista ele retorna o indice e o item da lista
            for indice, compra in enumerate(compras):  # aqui cria um indice e compra e numera eles
                print(indice, compra)   # printa a lita na tela
                
                
    if opcoes  == 'a': # escolha de apagar itens da lista
        if len(compras) == 0:
            print('lista vazia')
        for indice, compra in enumerate(compras): # aqui fiz um indice e compra para poder numerar as contas para o usuario poder escolher
            print('lista de material atual') 
            print(indice, compra) # lista de material atual para escolher qual apagar
            try:
                num = int(input('qual numero voce deseja apagar?')) # aqui capturamos o numero que usaremos para apagar o indice
                del compras[num]
            except:
                print(f'o numero {num} não existe ')
                
                
    if opcoes  == 'i': # veficicador de escolha se foi escolhido 'i' de inserir
        compras.append(input('o que voce deseja inserir: ')) # .append modo de inserir itens a lista
'''
                CODIGO DO PROFESSOR
    (ELE USOU IMPORT OS PARA CONSEGUIR LIMPAR O TERMINAL E DEIXAR MAIS CLEAN O TERMINAL)
                
        import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')        
'''
