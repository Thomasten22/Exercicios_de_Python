'''Formatação basica de strings
s - strings
d - int
f - float
.<número de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o numero a aparecer antes dos zeros
sinal - + ou - 
EX: 0>-100.f1
conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}') # uma formatação normal de f- strings
print(f'{variavel: >10}')# uma formatação mostrando a variavel 10 caracteres para a esquerda
print(f'{variavel: <10}.')# uma formatação mostrando a variavel 10 caracteres para a direita
print(f'{variavel: ^10}.')# formatação mostrando a variavel centralizada
print(f'{variavel:$^10}.')# formatação mostrando a variavel centralizada e preenchido os espaços vazios com $
print(f'{1000.8965654:,.1f}')# separa a milhar por virgulas
print(f'{1000.8965654:+,.1f}')# mostra que o numero é positivo
print(f'{1000.8965654:0=+10,.1f}')# adcionou o 0 10 casas porem antes dele colocou o sinal de positivo
print(f'O exadecimal de 1500 é {1500:08x}') # conta de exadecimal, adcionando 8 casas antes
print(f'{variavel!r}')# ainda vamos aprender 

