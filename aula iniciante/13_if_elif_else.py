'''
if / elif / else (se, se nao se, se nao) sao metodos de checagem para conseguirmos executar certos comando apos a checagem e saber o que te responder
LEMBRAR DE SEMPRE COLOCAR : APOS O IF ELIF E ELSE E TAMBEM DE SE FOR RECBER SRT LEMBRA DE PASSAR ASPAS SIMPLES
'''

entrada = input('voce quer "entrar" ou "sair"?')

if entrada == 'entrar':  #se digitar entrar voce recebe o print dessa operacao
    print('voce entrou no sistema')
elif entrada == 'sair':  #se digitar sair voce recebe esse print
    print('voce saiu no sistema')
else:                    #se vc nao digitar corretamente vc recebe mensagem errada  
    print('voce digitou errado!')
    
print('Bem vindo Thomas') # esse codigo esta fora do bloco de checagem ele vai aparecer independemente de da checagem do if/ elif / else

