'''Higher Order Functions
Funções de primeria classe (tradução)

explicação que podemos passar argumentos dentro de outras funções, fazendo que ela faça a requisição dentro da função
'''

def saudacao(msg, nome): # defini um função que recebe mensagens e nomes quando for requisitada no codigo
    return f'{msg}, {nome}'# quando ela for requisitada ela vai retornar os parametros passados a ela 

def executa(funcao, *args): # aqui defini uma função que vai executa a função e criei um *args para tudo que vir passado virar uma tupla
    return funcao(*args) # nessa linha vai desempacotar a tupla trazendo ela para variavel novamente 

print(executa(saudacao, 'Boa noite', 'Leticia')) # aqui estamos requisitando a função executa passando a ela função saudação e com isso se nao tivesse o metodo de *args o codigo quebraria que estariamos passando mais argumentos do que foi pedido
print(executa(saudacao, 'Bom dia ', 'Thomas')) # aqui estamos requisitando a função executa passando a ela função saudação e com isso se nao tivesse o metodo de *args o codigo quebraria que estariamos passando mais argumentos do que foi pedido
#E quando ela puxa saudacao ele vai pegar os argumetos que foram passados com ele para preencher os parametros passados la na definição e retornar a mensagem perfeitamente
 
 
'''        Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.'''