#introdução as Generetor functions em Python
#generator == (n for n in range(1000000))
# quando definimos uma função temos um comando que ele pode pausar a função (yield) e pode tambem ser despausado
# toda função que tem o yield é uma função geradora 
# e quando é chamada normalmente se passa junto do next

#           EXEMPLO CLARO DE YIELD

# def generator(n=0):
#     yield 1     # aqui é pause da função, quando charmarmos ela mais a baixo veremos que ela esta pausada na função
#     return 'acabou ' # return como ja vimos ele termina o codigo como se fosse um end ( final )

# gen = generator(n=0)
# print(next(gen)) # desse jeito vc vai ver que so vai retornar o 1 e ficara pausado aqui 

def gerador(n=1,maximun=10): # função definida com valores padrao para inicio e fim, inicio ->(n=0)  fim ->(maximun=10)
    
    while True: # laço repetitivo que seria infinito ate termos alguma condição que para ele 
        yield n # pausa do codigo (metodo que estamos aprendendo) ele esta retornando o primeiro valor
        n += 1 # contador basico para fazer o sistema contar de 1 a 10
        
        if n >= maximun:  # verificador que olha o codigo e ve se o n ( numero que esta sendo aumentado conforme rola o while) é maior ou igual que o valor maximo definido
            return # se o n for maior que o maximum ele entra no escopo e quebra o laço
        
gen = gerador(maximun=1000000) # declarei o valor de maximum para esse contador e o de n nao precisa porque ele ja foi declarado na função 
for n in gen: # classico contador que vai imprimir ate chegar no maximun 
    print(n)