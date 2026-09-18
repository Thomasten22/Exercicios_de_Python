'''
Argumentos nomeados e nao nomeados em funções Python
Argumento nomeado tem nome com sinal de igual =
argumento nao nomeado recebe apenas o argumento (valor)
'''
def soma (x, y, z):
    # Definição da função
    print(f'{x=}, y={y}, {z=} ', '|', 'x + y + z = ', x + y + z)
    
soma(1, 2, 3) # forma de argumentos nao nomeados, pois ele so segue a sequencia na ordem e executa, se invertemos os argumentos nao vamos inverter a ordem
soma(x=1, y=2, z=3) # dessa forma sao argumentos nomeados, pois estou definindo o que cada argumento faz, ai nao importa a ordem desde que sejam nomeados 
soma(1, 2, z=3) # podemos fazer como esse exemplo, nomear o ultimo e nao nomear os primeiros
#soma(1, y=2, 3) # dessa maneira temos erro de sintaxe (SyntaxError) dizendo que nao nomeamos o 3, porque a partir do momento que nomeamos o proximo deverá ser nomeado tambem
 
