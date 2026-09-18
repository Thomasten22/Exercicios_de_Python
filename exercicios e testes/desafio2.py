'''Analisador de Frequência de Palavras
Objetivo: Praticar manipulação de strings, listas, for e fatiamento.

Enunciado: Crie um script que receba uma frase ou texto pequeno do usuário e faça uma análise básica:

Remova espaços extras nas pontas e converta todo o texto para minúsculas.

Separe o texto em uma lista de palavras.

Crie uma nova lista que contenha apenas as palavras que possuem mais de 3 letras.

Imprima na tela:

A frase tratada.

A lista final com palavras que têm mais de 3 letras.

A quantidade de palavras filtradas.'''

frase = input('digite uma frase: ').lower().strip()
frase_tratada= frase.split()

frase_corrigida = []

for palavra in frase_tratada:
    if len(palavra) > 3:
        frase_corrigida.append(palavra)
        
print(f'esse é o texo tratado: {frase}')
print(f'a lista com palavras com mais de 3 letras:{frase_corrigida}')
print('essa é quantidade de palvras que foram filtradas: ', len(frase_corrigida))