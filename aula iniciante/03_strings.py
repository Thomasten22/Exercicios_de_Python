"""
srt-> string -> texto 
strings sao textos, e podem ser representados por aspas simples ou duplas
estando dentro 

"""
#Aspas simples
#aspas duplas podem ser bons caminhos para fazer as funcoes de r e escape, mas nao e muito comum, 
#pois as aspas simples sao mais comuns e mais utilizadas
print('thomas victor',sep=' ', end='\n')
print(1, "'santos de jesus'", sep=', ')

#Aspas duplas
#aspas simples pode ser bons caminhos para fazer as funcoes de r e escape, mas nao e muito comum, 
# pois as aspas duplas sao mais comuns e mais utilizadas
print("santos de jesus")
print(1, '"santos de jesus"', sep=', ')

#escape usado para enfase no que foi colocado a frente da barra invertida,
# como por exemplo a barra invertida e usada para mostrar as aspas duplas dentro da string
print("thomas \"victor")

#r usado para mostrar a string exatamente como ela foi escrita, sem interpretar os caracteres de escape
print(r"thomas \"victor")

#escape e r nao sao muito ultilizado por pessoas mais experientes com Python, 
#mas sao muito importantes para pessoas que estao aprendendo a linguagem, 
#pois eles ajudam a entender como o Python interpreta as strings e como ele lida com os caracteres de escape