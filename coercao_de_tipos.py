'''
conversao de tipos, coercao de tipos, cast
type converttion, typecasting, type coercion
e um  ato de converter um tipo de dado em outro tipo de dado, 
EXEMPLO:
converter um int em float, ou um float em int, ou um str em int, ou um str em float, etc.

TIPOS IMUTAVEIS E PRIMITIVOS:
str, int, float, bool

o sinal de + serve para concatenar strings, ou somar numeros, dependendo do tipo de dado que esta sendo usado.

EXEMPLO:
print('1' + '1') #str + str = str -> 11 (ele ve que foi passado como str e junta os dois valores, sem somar)
print(1 + 1) #int + int = int -> 2
print(float('1') + float('1')) #float + float = float -> 2.0
'''
print('1' + '1')  #str + str = str -> 11 (ele ve que foi passado como str e junta os dois valores, sem somar)

print(1+1) #int + int -> ele soma os valores e da o resultado somado
'''
 codigos como:
print('1' + 1) explodiria o erro na cara porque ele diria que esta com erro de tipo pois nao e possivel concatenar um srt com uma int
 
 porem podemos fazer de uma maneira que conseguimos alterar o seu modo 
 EXEMPLO:
 '''
print(int('1') + 1) #dessa maneira conseguimos converter o tipo para inteiro e assim conseguimos receber respostas em string e converter para int, float e vice e versa
print(type(float('1')+1))
print(bool(' '))
print(str('thomas gatao'))