'''
split e join com list e str

split -> divide uma string
com o split conseguimos dividir as palavras e as frase passando para ele o parametro que ele quer que ele divida
join -> une uma string
'''
#exemplo de split 

frase = 'Olha so que, coisa interessante' #variavel com a frase passada que sera divida
lista_palavras = frase.split() # desse jeito que esta passado o paramento ele vai dividir as plavras por espaços
print(lista_palavras)# vai exibir as frases fatiadas

lista_frases = frase.split(',')# aqui estamos dividindo na virgula retornando o que esta antes e depois dela
print(lista_frases)#para exibir na tela o print da palavra separada pela virgula 

for i, frasae in enumerate (lista_frases): # modo para deixar mais refinado no terminal o fatiamento das frases da str
    print(lista_frases[i].strip())# o metodo .strip() corta os espaços do inicio e do fim das frases
    
    
#metodo join

exe_nome = '-'.join('thomas') # metodo para juntas strings, nesse exemplo ele vai colocar apos cada letra do meu nome um - e vai retornar assim no print (t-h-o-m-a-s)
print(exe_nome)

frase_unidas = '_'.join(lista_palavras)# chamei a variavel la de cima para mostras que ela faz isso tambem com listas, a cada palavra ela vai adicionar uma _
print(frase_unidas)