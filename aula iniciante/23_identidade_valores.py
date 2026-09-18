'''
FLag (bandeira) - marcar um local
None - Não valor
is e is not - é ou nao é (tipo, valor, identidade)
id - identidade

v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))
'''
condicao = False
passo_no_if = None # o None esta passando uma que nao tem valor

if condicao:
    passo_no_if = True # aqui redefinimos a variavel para true pois ela passou no if
    print('Faça algo')
else:
    print('nao faça algo')
'''
print (passou_no_if, passou_no_if is None) #a variavel sera retornada se passou no if ou nao se passou (True) e se nao passou (False) e o is esta como um confirmador (é) e se nao passou ele vai retornar true se nao, False
print (passou_no_if, passou_no_if is not None)# aqui a variavel is not (não é) ele faz o inverso do is(é)'''

if passo_no_if is None: # aqui vemos que n se o passo_no_if for iqual a None ele retorna nao passou
    print('não passou no if')
if passo_no_if is not None:# aqui vemos que n se o passo_no_if não for iqual a None ele retorna que passou
    print('passou no if')