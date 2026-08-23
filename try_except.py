'''
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu um erro ao tentar executar  

'''
numero = input('vou dobrar o numero que voce me passar: ') #se nao declararmos um a classe ele sempre captura a resposta como string

try: # ele tenta executar o codigo e se ele perceber que algo deu errado ele nao vai retornar erro, mas sim vai pular para o except
    print('string: ', numero) # aqui vai retornar a string recebida (sendo numero ou nao sera uma string)
    numero_float = float(numero) # aqui estamos mudando a tipagem de str para float (aonde conseguimos exemplificar que se colocarmos letra nao converterá)
    print('float: ', numero_float)# aqui o numero foi convertido de srt para float e retorna o numero 
    print(f'o dobro do {numero} é {numero_float * 2}') # aqui é a resposta passando o dobro e claro dando tudo certo
except: #se o try encontar erros no parametro passado no exemplo ele passa aqui para o except dando a resposta designada
    print('isso não é um numero!!')#resposta caso algo falhe no try