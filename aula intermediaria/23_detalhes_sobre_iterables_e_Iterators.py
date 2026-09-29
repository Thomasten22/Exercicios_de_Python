# Generator expression, Iterables e Iterators em Python (Iteraveis e Iteradores)

#iterable serve para guardar coisas, igual o exemplo abaixo que esta guaradando 3 strings numa lista
iterable = ['Eu', 'Tenho', '__iter__']

 # o iterador ele serve exclusivamente para poder acessar o proximo item do iteravel (vai percorrendo do inicio ao fim da lista)
iterator = iterable.__iter__() # tem __iter__ e __next__
# o __iter__ ( ou iter(iterable)) serve para usar o __next__(ou next(iterable))

print(f'Lista com iteraveis{iterable}') # esse print passa todos os itens de uma vez
print()
print(next(iterator)) # esse print vai mostrar somente o primeiro item da lista de iteraveis que foi declarada == 'Eu'
print(next(iterator)) # esse print vai mostrar somente o segundo item da lista de iteraveis que foi declarada == 'Tenho'
print(next(iterator)) # esse print vai mostrar somente o terceiro item da lista de iteraveis que foi declarada == '__iter__'
# se passarmos um 4° print do mesmo jeito dos acima, vai ter um erro de stopIteration reclamando que nao tem mais nada na lista para ser iterado 
print()

# o for trabalha dessa mesma maneira enquanto estiver no escopo do for ( tendo itens na lista) ele devolve o valor, acabaou o valor ele sai do escopo