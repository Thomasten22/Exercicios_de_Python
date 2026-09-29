#PROGAMADORES GOSTAM DE ERROS QUE POR ELES CONSEGUIMOS NOS GUIAR PARA RESOLVER ELES 
# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d): # FUNÇÃO DECLARADA PARA TRATAR O ERRO QUE ALGUM NUMERO É IGUAL A 0
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') # RESPONSALVEL POR VERIFICAR E RETORNAR COM UMA MENSAGEM
    return True# ESTA RETORNANDO TRUE PORQUE ELE ATENDE OS PARAMETROS DE NAO SER IGUAL A ZERO


def deve_ser_int_ou_float(n): # VERIFICA SE O PARAMETRO PASSADO É UMA VARIAVEL INT OU FLOAT
    tipo_n = type(n)
    if not isinstance(n, (float, int)): # O ISINSTANCE VERIFICA SE O PARAMETRO SE ENCAIXA COMO FLOAT OU INT E SE NAO FOR ELE JA PULA PRO RAISE
        raise TypeError(  # RESPONSAVEL POR ENTREGAR  O ERRO E DIZER O QUE ACONTECEU
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True # ESTA RETORNANDO TRUE PORQUE ELE ATENDE OS PARAMETROS DE INT OU FLOAT


def divide(n, d):  # FUNÇÃO QUE DIVIDE OS NUMEROS
    deve_ser_int_ou_float(n) # AQUI VERIFICA SE O PRIMEIRO NUMERO PASSADO É INT OU FLOAT 
    deve_ser_int_ou_float(d) # AQUI VERIFICA SE O SEGUNDO NUMERO PASSADO É INT OU FLOAT 
    nao_aceito_zero(n) # AQUI VERIFICA SE O PRIMEIRO NUMERO É IGUAL A ZERO 
    nao_aceito_zero(d) # AQUI VERIFICA SE O SEGUNDO NUMERO É IGUAL A ZERO 
    return n / d # SE TODOS OS PARAMETROS FORAM ATENDIDOS ELE RETORNA O RESULTADO DA CONTA


print(divide(8, '0')) 