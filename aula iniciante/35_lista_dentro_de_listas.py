'''
Listas de listas e seus indices
'''
salas = [   #inicio da lista mãe
    #   0         1    aqui sao os indices da lista 0 representados para a melhor visualização
    ['Thomas','Leticia',],  #0                representa a lista indice 0
    
    #   0         aqui sao os indices da lista 1 representados para a melhor visualização
    ['Maria',], # 1             representa a lista indice 1
    
    #     0          1          2         aqui sao os indices da lista 2 representados para a melhor visualização
    ['Veronica', 'Genival', 'Guilherme',],# 2             representa a lista indice 2   
    # ['Veronica', 'Genival', 'Guilherme',(0, 10, 20, 30, 40)] # exemplo com a tupla
]#fim da lista mãe

print(salas[0]) # estamos chamado a lista do indice 0
print(salas[1]) # estamos chamado a lista do indice 1
print(salas[2]) # estamos chamado a lista do indice 2
print(salas) # estamos chamando todas as listas de salas
print(*salas, sep='\n') # metoodo de desempacotamento de chamadas desse modo vai trazer todas as listas desempacotadas mais facil de visualizarmos

print(salas[0][0]) # estamos chamado a lista do indice 0 e seu indice interno (Thomas)
#print(salas[2][3][4]) exemplo com metodo tupla buscando o numero 40 dentro da lista do indice 2

for sala in salas: # esse for esta pegando as lista e dividindo elas
    for aluno in sala: # esse segundo for dentro do laco do primeiro esta dividindo os nomes que estavam nas listas dentro das lista
        print(aluno) # esta retornando somente os nomes como lista

