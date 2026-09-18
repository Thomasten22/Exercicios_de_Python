'''
for usamos para variaveis que sabemos que vai ter fim, exemplo a string com nome no exemplo abaixo 
conseguimos identificar que o a palavra python tem 6 letras e com isso o for percorre com uma variavel
criada por nos mesmos para conseguimos percorrer ela '''




text = 'Python' # variavel criada e declarada

for letra in text:  # for sendo usado com o boa pratica de codigo clean e variavel letra criada dentro dele para armazenar o valor
    print(letra) # mostra a variavel de text uma letra de baixo da outra sem a dependencia do contador enorme do while
    
    
novo_texto = ""

for letra in text:
    novo_texto += f'*{letra}'
    
print(novo_texto)