'''
args - argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
'''
# Lembre-te de desempacotamento

def soma(*args): # aqui vemos funcionando o metodo *args salvando os numeros em tuplas
    total = 0 # total definido para fazer um contador somando os numeros passados
    for numero in args: # enquanto tiver numeros em args(a tupla passada para a função como argumento)
        total += numero # vai somar no total os numeros
    return total # so retorna o total da operação

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10  # tupla
outra_soma = soma(*numeros) # esse asterisco desempacota a tupla para virar uma tupla para somar dentro da função (é estranho mas é isso mesmo kkkkkkkk)
print(outra_soma)

print(sum(numeros)) # aqui é uma função do proprio python para somar numeros e soma tambem em tupla sem a necessidade de criar uma função soma
