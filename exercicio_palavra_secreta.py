secreta = 'thomas' # palavra secreta (em minúsculo para facilitar)
letras_acertadas = '' # variavel que armazena as letras acertadas
numero_tentativas = 0 # contador de tentativas 

print('Jogo da palavra secreta!')

while True:
    letra_digitada = input('Digite uma letra: ').lower() # aqui recebemos a letra escolhida e convertemos para minúsculo
    numero_tentativas += 1 # aumenta o numero de tentativas assim que o codigo recebe a primeira letra do usuario 

    # Validação da entrada (apenas 1 letra)
    if len(letra_digitada) > 1: # aqui é um verificador se o usuario digitou apenas 1 letras se nao digitou ele responde que digitou letras demais e volta para digitar letra novamente
        print('Digite apenas uma letra.')
        continue # aqui continua o laço voltando ele para o inicio 

    # Guarda a letra se ela existir na palavra secreta
    if letra_digitada in secreta: # ele verifica se a letra digitada esta na palavra secreta, isso é um verificador 
        letras_acertadas += letra_digitada  # aqui ele alimenta a letra acertada com a letra digitada fora do laço while

    # Monta a exibição da palavra atual (_ ou letra)
    palavra_formada = ''  # nova variavel vazia criada para receber os (_) colocando aonde nao tem as letras acertadas.
    for letra_secreta in secreta: # outro verificador vendo se tem a letra escolhida na palavra secreta 
        if letra_secreta in letras_acertadas: #  se a letra secreta estiver na letra acertada ele alimenta a palavra formada com a letra 
            palavra_formada += letra_secreta # aqui ele esta alimentando o palavra formada com a letra secreta
        else: # aqui ele verifica que nao acertou a palavra secreta e adiciona a _ nas palavras acertadas 
            palavra_formada += '_' # aqui ele esta adicionando a _ na palavra formada 

    print('Palavra formatada:', palavra_formada) # <- ATENÇÃO AQUI: alinhado com o 'for' (fora dele)

    # Verifica se o usuário adivinhou todas as letras
    if palavra_formada == secreta: # aqui vemos que acertamos todas as letras e recebemos o premio por isso
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', secreta)
        print('Tentativas:', numero_tentativas)
        break