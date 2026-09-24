# EXEMPLO DE USO DE SETS

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 't' in letras:
        print('PARABÉNS')
        break
    
    print(letras)
