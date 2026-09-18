# Exercício - sistema de perguntas e respostas


perguntas = [{

        'Pergunta': 'Quanto é 2+2?',

        'Opções': ['1', '3', '4', '5'],

        'Resposta': '4',

    },
    {
        'Pergunta': 'Quanto é 5*5?',

        'Opções': ['25', '55', '10', '51'],

        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',

        'Opções': ['4', '5', '2', '1'],

        'Resposta': '5',
    },
]

print('--- JOGO DE PERGUNTA E RESPOSTAS ---')

contador = 1

certo = 0

for listas in perguntas:

    print(f'{contador}° pergunta!')

    contador += 1
    
    print (listas['Pergunta'])
    
    res = input(f'Opções: {listas['Opções']}: ')
    
    if res == listas['Resposta']:
        print ('Acertou em cheio!')
        certo += 1
    else:
        print('Você errou feio')
        print(f'A resposta correta é: {listas['Resposta']}')

if certo == 0:
    
    print(f'voce errou tudo, estude mais')
    
elif certo > 0 and certo <= 2:
    
    print(f'voce acertou {certo} perguntas, da para melhorar!')
    
else:
    
    print(f'voce acertou {certo} perguntas, você é o melhor!')