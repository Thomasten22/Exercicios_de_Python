'''
Manipulando chaves e valores em dicionarios

'''
pessoa = {}


chave = 'nome'  #declarando uma variavel para a chave

pessoa[chave] = 'Thomas' # indice nome declarado na varaiavel passando o parametro nome e o nome da pessoa

pessoa['sobrenome'] = 'neves' #declarei a chave sobrenome passando paramentro 

del pessoa['sobrenome'] # estou excluindo a chave sobrenome

'''a partir daqui eu deletei sobrenome e se caso algo requisitar ele vai dar o erro chamado KeyError
para resolver isso usamos a função .get'''

print(pessoa.get('sobrenome', None)) # o none serve para ele devolver none, na falta da chave no dict

print(pessoa)#mostrando a o indice que foi declarado para a variavel

print(pessoa[chave])# mostrando dinamicamente
