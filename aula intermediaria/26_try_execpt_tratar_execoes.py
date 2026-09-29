# Try, Except, else e finally


# explicação de try except, esta explicando que boa pratica de programação e o Zen of Python diz que nao devemos deixar passar erros silenciosamente
#por esse motivo devemos sempre definir o except com o erro que foi informado no codigo, os erros sao classes, e a maior deles é o (Exeption)
# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError: # esta tratando somente erro que se tentar dividir algo por 0 
    print('Dividiu por zero.')
    
except NameError: # esta tratando somente NameError (nesse exemplo seria se o B nao estivesse definido)
    print('Nome b não está definido')
    
# estamos mostando nesse exemplo tambem que podemos saber qual foi o erro que ocasionou esse except
except (TypeError, IndexError) as error: # Type error esta sendo tratado aqui, porem passei tambem um outro erro junto com ele
#isso significa que conseguimos passar duas classes de erro pro mesmo except (temos que passar como tupla quando sao dois erros no mesmo except (erro, erro ))
    print('TypeError + IndexError')
    print('Nome:', error.__class__.__name__) # vai mostrar o nome do erro (.__ckass__--> pega a classe)(.__name__ --> pega o nome do erro)
    print('MGS:', error) # vai mostrar a descrição do erro 
except Exception:  # Maior tier de classe de erros ele guarda todos os erros porem nao saberemos qual erro foi capturado por ele, dessa maneira seria erro silenciado ( má pratica de programação)
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
print()

# Finally e else:

try:
    print('ESTOU SENDO EXECUTADO NO TRY')
    8/0
    print()
except ZeroDivisionError:
    print('IDIOTA, tentando dividir zero')
    print()
    
else: # ele é executado quando o coodigo nao deu erro ??????(deixa o codigo redundante)
    print('Não deu erro')
    
    
finally: # sempre sera executado mesmo que tenha dado algum erro no processo do try
    print('FUI EXECUTADO DE QUALQUER FORMA')