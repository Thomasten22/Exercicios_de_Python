'''
Introdução as funções (def) em Python
Funções sao trechos de codigo usados para 
replicar determinada ação ao longo do seu codigo
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
Por padrão, funções em Python retornam None(nada)

dentro da função def conseguimos passar ate parametros de if else, in e not in, while entre outros
'''
def Print(): #dessa maneira eu defini que Print com P maiusculo consiga replicar o que esta dentro do seu escopo
    print('teste')

Print()

# EXEMPLO DE DEFINIÇÃO DE FUNÇÃO COM PARAMETROS PASSADOS

def imprimir(a,b,c): #dessa maneira eu passei parametros para essa função, Parâmetro é o nome da "variável" dentro dos parênteses
    print(a,b,c)

imprimir(1,2,3)# dessa maneira eu defini argumentos para os parametros, argumento é o valor passado para o parâmetro no momento da execução da função.
imprimir(4,5,6)

#exemplo basico

def bomdia (nome): # defini o parametro da função receber nomes
    print(f'Bom dia, {nome}') # isso é o que a função vai executar ao longo do codigo (ela vai dar bom dia com o nome passado)

#bomdia() desse jeito estouraria um erro no console porque o argumento para preencher o parametro nao foi passado !!!!!!!
bomdia('Thomas') #nesse momento vemos que precisamos passar o argumento (nesse exemplo o nome da pessoa) para que o codigo nao de erro
bomdia('leticia') #exemplo mostrando que posso passar varios nomes que ele da varios prints diferentes
bomdia('Gostosa') 

def boanoite (nome = 'sem nick'): #exemplo mostrando como nao faz para estourar o erro na tela
    print(f'Boa noite, {nome}') 

boanoite('Thomas') 
boanoite('leticia') 
boanoite() # vai retornar o argumento na definição

#exemplo passado no teste seus conhecimentos
def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)