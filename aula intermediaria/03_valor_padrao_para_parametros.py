'''
Valores padrão para parametros
Ao definir uma função, os parametros podem
ter valores padrão. Caso o valor não seja
enviado para o parametro, o valor padrão será
usado.
Refatorar: editar o seu codigo.
'''

#metodo para nao necessariamente precisar passar os 3 argumentos, e dessa forma ele vai ver mesmo que nos mandemos 0 ( que é um valor false)
#A MESMA REGRA DE ARGUMENTOS REPETE AQUI EM PARAMETROS, SE O ULTIMO VALOR FOR DECLARADO, O QUE VIER APOS, DEVERÁ SER DECLARADO TAMBEM
def soma (x, y, z=None): 
    if z is not None: # comparador se z for diferente de None (valor vazio), vai enviar o print com o z
        print(f'{x=}, y={y}, {z=} ', '|', 'x + y + z = ', x + y + z)
    else: # se for z vazio vai mandar esse print sem o z
        print(f'{x=}, y={y}', '|', 'x + y = ', x + y )

#exemplos mostando na pratica
soma(1, 2) 
soma(x=4, y=5) 
soma(1, 2, z=1)
