'''
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matematica
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são MUTAVEIS, porém aceitam apenas tipos IMUTAVEIS como valor interno.

set parecem dicionarios porque eles estao envolvidos em chaves, porem dicionario tem chave e valor e o set somente valor

dicionario(dict) -- chave e valor{'chave': 'valor'}
             set -- somente valor {'chave','valor'}

se tentarmos criar um set vazio ({}) iremos estar criando na verdade um dicionario

set vazio por sua vez é criado --> exemplo = set()

criar str no modo set como exemplo --> exemplo = set('Thomas') -- num eventual print ele interprepreta letra por letra e entrega
todo bagunçado ({'a', 's', 'o', 'T', 'm', 'h'}) entao ele basicamente é um interpretador de letra por letra no caso de strings

o modo set nao aceita valores imutaveis (lista e dict)
tupla pode porem ao final da tupla ( ela é mutavel) necessita de uma virgula no final -- {1,2,3,(123,)}

modo set tende a ser mais rapido em certas ações do que dict, list e tuple

criando um set 
set(itevavel) ou {1,2,3}'''


s3 = set('Thomas') # ele vai iterar sobre cada letra da palavra
s4 = {'thomas','ten', 22,27} # outra maneira de criar um set, dessa maneira ele vai iteirar normalmente porem a ordem pode vir bagunçada ({'ten', 27, 'thomas', 22})


'''
Sets são eficientes para remover valores duplicados de iteraveis
- eles não tem indexes;
- eles nao garatem ordem;
- eles sao iteraveis(for, in, not in)

nesse metodo de remover valores duplicaos, conseguimos pegar no exemplo uma lista com diversos valores duplicados
mudar ele pra set e depois volta para list
'''
# exemplo de correçâo de numeros repetidos
lista_com_valores_dup = [1,2,3,3,3,3,4,5,6] 
set_removendo_dup = set(lista_com_valores_dup)
voltando_pra_list = list(set_removendo_dup)
print(f'''          lista com valor duplicado
          {lista_com_valores_dup}
          -----------------------
          Lista corrigida depois da tratativa set
          {voltando_pra_list}''')


# dessa maneira so nao conseguimos garantir que a lista fique em ordem, pois o modo set nao garante ordem

'''
        METODOS UTEIS;

add, update, clear, discard
'''
s1 = set()# set vazio

#add -- adcionar itens no set
s1.add('Thomas')
s1.add(1)

#update - muito parecido com add ele adciona no set 
# se passar somente um valor iteravel como uma str, ele vai bagunçar a frase toda, para resolver pássar mais valores
s1.update(('teste')) # valor unico vai ficar bagunçado
s1.update(('ola mundo', 1,2,3,4)) # desse jeito nao fica bagunçado

#discard -- exclui um valor do set
s1.discard('teste') # estou excluindo o valor que ficou bagunçado


#clear --  ele limpa o set 
s1.clear()

print(s1)

'''
Operadores uteis:

uniao | uniao (union) - Une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simetrica ^ - itens que não estao em ambos
'''

set1 = {1, 2, 3}  # set para ser comparado no exemplo
set2 = {2, 3, 4}  # set para ser comparado no exemplo
uniao = set1 | set2    # operador de union  --- faz a união dos set (porem vai exlcuir os repetidos)
intersecção = set1 & set2    # operador de itersection  -- ele compara o que tem em ambas as lista {2, 3}
diferença = set2 - set1    # operador de diferença  -- ele compara o que so tem somente no set da esquerda e que nao tenha nas duas linhas {4}
diferença_simetrica = set1 ^ set2    # operador de diferença simetrica  -- ele compara o que nao esta duplicado {1, 4}

print(f'''      --UNIAO--
      {uniao}
      --INTERSECÇÃO--
      {intersecção}
      --DIFERENÇA--
      {diferença}
      --DIFERENÇA SIMETRICA--
      {diferença_simetrica}
      ''')