'''       OPERADORES DE ATRIBUIÇÃO
        
= += -= *= /= //= **= %=

Conseguimos alterar algumas coisas no codigo com operadores de atribuição como por exemplo: 

contador += 1     vai fazer a conta da mesma maneira que se eu colocasse do metodo tradicional
contador = contador + 1         metodo antigo usado de exemplo aqui

esse metodo consegue ser usado para a concatenação de str também
'''

contador = 0

while contador < 10:
    contador += 1 # atribuido na pratica para ver que ele continuará somando o 1
    print(contador)
    
print('acabou')