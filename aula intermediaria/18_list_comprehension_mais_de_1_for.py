'''EXPLICAÇÃO PARA GRUDAR MAIS SOBRE O LIST COMPREHENSION, 
ESSA VEZ ELE ESTA MOSTRANDO QUE CONSEGUIMOS CRIAR UMA LISTA COM 2 PARAMETROS PASSADOS'''
import pprint

def p(y):
    pprint.pprint(y, sort_dicts=False, width=40)
#       METODO ANTIGO 
lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))
        
print('lista com os metodos antigos')
p(lista)
print()
#       METODO ANTIGO 

lista1 = [
    (x, y) # passando os parametros para a criação da tupla (antes do for é mapeamento, o que vai ser salvo na lista)
    for x in range(3)
    for y in range(3)
]

print('lista com os metodos novos')
p(lista1)