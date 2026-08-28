"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

secret = 'secreta'
letras_acertadas = ''
numero_tentativas = 0

print('Jogo da palavra secreta!')

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    # Validação da entrada (apenas 1 letra)
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # Guarda a letra se ela existir na palavra secreta
    if letra_digitada in secret:
        letras_acertadas += letra_digitada

    # Monta a exibição da palavra atual (* ou letra)
    palavra_formada = ''
    for letra_secreta in secret:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formatada:', palavra_formada)

    # Verifica se o usuário adivinhou todas as letras
    if palavra_formada == secret:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', secret)
        print('Tentativas:', numero_tentativas)
        break