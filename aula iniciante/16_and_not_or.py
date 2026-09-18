'''OPERADORES LOGICOS
and(e) or(ou) not(não)
and - todas as condições precisam ser verdadeiras.
se qualquer valor for considerado falso, a expressão será invalidada naquele valor
São considerados falsy (que voce ja viu)
0 0.0 '' False
Também existe o tipo de None que é usado para representar um não valor
EXEMPLO

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = '123456'
#if == True :  
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
    
AVALIAÇÃO DE CURTO CIRCUITO
PRINT(True and False and True)
ele irá retornar falso pois ele verificou que na segunda casa está como False e assim ele nao realiza a checagem da terceira casa,
ele entende que ja deu um false e nao precisa da checagem

EXERCICIOS and

if 1 and 1:
    print(True and 1 and False)
    
vai retornar false pois a checagem para nele, 
True == True
1 == True
False != True (por conta desse resultado ele retorna o False que foi o que ele checou por ultimo )


if 0 and 1:
    print(True and 1) 
    
retorna nada pois o 0 (false ) é diferente de 1 (true ) sendo assim nao tem como ele avançar apos isso 
    
    
    PARTE DE or
    
    entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = '123456'
 
 (aqui vemos que o or serve para verificar se uma nao atendida se a outra vai ser para poder liberar o acesso)
 
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
    
    CURTO CIRCUITO
PRINT(True or False or 0 or 'abc') vai retornar o valor verdadeiro ou o True, nesse exemplo ele retorna 'abc' porque é uma str preenchida e isso é um valor true

    OUTRO EXEMPLO
    
senha = input('digite a senha: ') or 'sem senha'
    
print(senha) 
    
se escrevermos a senha ele retorna ela, se nao escrevermos nada ( deixar em branco) ele retorna sem senha,
porque ele avalia que o valor vazio é false entao ele passa a outra opção que é True
    
    
    
    PARTE DE NOT
    
operador logico "not"
Usado para inverter expressões
not True = False
not False = True

print( not False ) ele retrona true porque inverteu a expressão 
print(not True) retrona False porque inverteu a expressao 

normalmente ele inverte a expressão e porque descomplicar algumas base de codigos 


senha = input('digite a senha: ')

if not senha:
    print('o campo esta vazio ')
    '''
    
    

