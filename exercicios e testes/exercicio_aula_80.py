"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
    
    ACHEI MUITO DIFICIL, POREM A PARTIR DO MOMENTO QUE EU COMETEI TUDO ACHEI MAIS TRANQUILO
    
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def listas_duplicadas(matriz): #função definida tendo que passar a matriz
    for lista in matriz: # quando declaro variavel lista que vai ser separada da matriz que é passada ( matriz essa que ja esta pre moldada)
        duplicados_vistos = set()  # Reinicia o set para cada lista individual (lista com set idividual)(em set nao pode Haver numero duplicado)
        primeiro_duplicado = -1 # foi declarado para se caso nao ouver repetidos devera retornar esse valor

        for numero in lista: # numero é uma nova vavriavel daclarada para pegar os valores da variavel lista que foi declarada no for acima
            if numero in duplicados_vistos: # o if serve para verificar se tem o numero nos numeros ja vistos 
                primeiro_duplicado = numero # se ele verificar que ja tem ele entra e pega o numero e salva no primerio duplicado
                break  # Encontrou a 2ª ocorrência, para de procurar nesta lista
            duplicados_vistos.add(numero) # essa função esta salvando os numeros na variavel set ( TEM QUE SER DEPOIS DO IF, SE NAO ELE ADICIONA E O DUPLICADO SOME)
            
        print(f"{lista} -> {primeiro_duplicado}")
        

listas_duplicadas(lista_de_listas_de_inteiros)
