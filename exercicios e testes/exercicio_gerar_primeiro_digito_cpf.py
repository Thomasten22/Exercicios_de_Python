

cpf = '746.824.890-70' #variavel recebida
traco_cpf = cpf.split('-') # removido o traço do CPF separando o digito dos 9 digitos
del traco_cpf[1] #deletei o digito do CPF que ja tinha sido separado antes
pontos_cpf = traco_cpf[0] # declarei uma variavel que armazena o indice zero da lista traco_cpf ( so tem esse indice )
cpf_sem_pontos = pontos_cpf.split('.') # removi os pontos do cpf e agora consigo juntar eles em numeros
cpf_unido = ''.join(cpf_sem_pontos) # juntei todos os numeros do cpf
guarda_conta = []# armazena os numeros que serao multiplicados nos for abaixo

contagem = 10 #contagem declarada para fazer as multiplicações do cpf e vamos fazer um metodo para diminuir nele mesmo
for num in cpf_unido: # contador que enquanto tiver numero em cpf unido ele vai percorrer esse laço
    guarda_conta.append(int(num) * contagem) # metodo append pega a conta que esta sendo feita e adciona na lista ja passando o numero como int
    contagem -= 1 # diminui 1 na contagem
    
soma = sum(guarda_conta) # esse metodo esta somando os numeros armazenados na lista de guarda_conta
multiplicação = soma * 10 # multiplica por 10 o valor da soma
resto = multiplicação % 11 # faz a conta do resto da multiplicação por 11

digito1 = f'{resto}' if resto <= 9  else 0  # aqui é um identificador se o numero é maior que 9 ou nao se for maior retorna 0 e se nao for retorna o numero

contador = 11 #redeclarei o contador para poder multiplicar o segundo numero 
str_prim_digito = str(digito1) # transformei o primeiro digito em string pra juntar ele no nos 9 primeiro numeros do cpf que estao em string tambem
cpf_novo_unido = cpf_unido + str_prim_digito # juntei os numeros para poder passar ele no metodo for 

novo_guarda_conta =[] # declarei uma nova lista vazia para poder armazenar os resultados das somas em lista
for number in cpf_novo_unido: # vai percorrer o cpf unido
    novo_guarda_conta.append(int(number) * contador) # metodo append para adicionar a multiplicação no novo guarda conta
    contador -= 1 # diminui no contador 1 

nova_soma = sum(novo_guarda_conta) # soma o itens da lista e retorna o valor 
multi = nova_soma * 10 # multipica o valor de nova soma por 10
novo_resto = multi % 11 # faz a conta de resto com a multipicação 

digito2 = f'{novo_resto}' if novo_resto <= 9  else 0 

if str(digito1) == cpf[-2] and str(digito2) == cpf[-1]: # validador se o cpf esta correto
    print('CPF valido!')
else:
    print('CPF invalido!')
    
    
    """
        CALCULO SEGUNDO DIGITO
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

        CALCULO DO SEGUNDO DIGITO 
        
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""