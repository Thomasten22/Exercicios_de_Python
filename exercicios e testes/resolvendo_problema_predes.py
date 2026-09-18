palavra_secreta = "predes" # palavra secreta 
tentativas = 0
letra_acertada = ""


while True:
    letra = input("escolhar sua letra: ") # pede o valor
    tentativas += 1 # adciona mais 1 em tentativas
    
    if len(letra) > 1: # compara se o usuario colocou mais de uma letra
        print("vc so pode escolher uma letra")
        continue # retorna o laço para o inicio
    
    if letra in palavra_secreta: # aqui verifica se a letra esta na plavra secreta 
        letra += letra_acertada # ele adciona a letra na variavel letra_acertada
        
    palavra_formada = '' # aqui é a palavra completa
    for letra_secreta in palavra_secreta: # verificando se a letra esta na palavra (o for cria uma variavel)
        if letra_secreta in letra_acertada: # verifcador se letra secreta esta na letra acertada
            palavra_formada += letra_secreta #adciona a letra na palavra formada
        else:
            palavra_formada += "*" 
            print('palavra secreta: ',palavra_formada)
    if palavra_formada == palavra_secreta: # aqui vemos que acertamos todas as letras e recebemos o premio por isso
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era:', palavra_secreta)
            print('Tentativas:', tentativas)
            break
            
