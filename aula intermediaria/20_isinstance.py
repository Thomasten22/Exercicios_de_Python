#  isinstence - para saber se o objeto é de determinado tipo 
# isinstence -> é instancia dê
#verifica se o item passado ou percorrido é instancia de algo que passamos a ele

lista = [
    'Thomas', 27, 1.85, True, [0, 1, 2], (1, 2),
         {0, 1}, {'nome': 'Leticia'},
]

for item in lista: # fez o for para percorrer a lista completa
    if  isinstance(item, str): # so vai cair aqui o que é String
        print(f'Somente o que é String: {item}')
        print()
        
    elif isinstance(item, bool):# so vai cair aqui o que é Boleano
        print(f'Somente o que é Boleano: {item}')
        print()
        
    elif isinstance(item, float):# so vai cair aqui o que é Float
        print(f'Somente o que é Float: {item}')
        print()
        
    elif isinstance(item, int):# so vai cair aqui o que é Inteiro
        print(f'Somente o que é Inteiro: {item}')
        print()
        
    elif isinstance(item, list):# so vai cair aqui o que é Lista
        print(f'Somente o que é Lista: {item}')
        print()
        
    elif isinstance(item, tuple):# so vai cair aqui o que é Tupla
        print(f'Somente o que é Tupla: {item}')
        print()
        
    elif isinstance(item, set):# so vai cair aqui o que é Set
        print(f'Somente o que é Set: {item}')
        print()
        
    elif isinstance(item, dict):# so vai cair aqui o que é Dict
        print(f'Somente o que é Dicionario: {item}')
        
    
    #print(item, isinstance(item, set)) # nesse print esta pedindo para imprimir cada coisa na tela e verificando o que é um set nesse for