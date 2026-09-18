"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} -- FEITO
        Seu nome invertido é {nome invertido} -- FEITO
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras -- FEITO
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
contagem = len(nome)

if nome and idade: # nao precisamos passar parametros desse jeito ele ja verifica se temos ou nao coisas salva nas variaveis
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome: # primeiro o que devemos procurar depois a variavel que devemos buscar
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f' Seu nome tem {contagem} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
        
    
else:
    print('Desculpe, você deixou campos vazios')