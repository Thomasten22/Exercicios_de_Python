frase = 'aaaooo'

i = 0 # contador para dar continue no while 
qtd_apareceu_mais_vezes = 0 # variavel para contar quantas vezes a letra apareceu
letra_apareceu_mais_vezes = '' #variavel criada para armazenar a variavel que mais apareceu

while i < len(frase): # aqui temos o sistema de laço que conta ate a o (i) ficar maior que o a variavel
    letra_atual = frase[i] # armazena a letra do i temporariamente na memoria 

    if letra_atual == ' ': # esse if serve para verificar se tem algum espaço ' ' para nao contabilizar
        i += 1 # esse contador dentro desse if é oara nao criar loop infinito no terminal 
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual) # aqui é um contador que armazena dentro do while qual letra apareceu mais no momento

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual: # aqui é um verificador de qual letra foi a maior, se a letra atual apareceu mais que anterior ele substitui no contador que esta fora do while
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual # aqui armazena fora da do while a letra

    i += 1 # adiciona mais 1 ao contador

print(                                                  #print fora do while entregando o resultado da letra que apareceu mais vezes e quantas vezes foram 
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

