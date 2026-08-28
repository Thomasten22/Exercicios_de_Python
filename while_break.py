"""
Repetições 
    while (enquanto)
Executa uma ação enquanto uma condição for verdadeira (True)
Loop infinito -> quando o codigo nao tem fim, quando criamos metodos que ficará dando while pra sempre sem termos a opção de parar de executar o codigo 

condicao = True

while condicao: # aqui ele esta chegando a variavel condicao e esta vendo que ela recebe true e executa o codigo a baixo infinitamente

    nome = input('Qual é o seu nome? ')
    print(f'seu nome é {nome}') 
    
    if nome == 'sair':
        break #comando para podermos parar o loop
        
    
CONTINUE == essa função conseguimos que ela ignore algo que passamos para ela pulando para o while de novo, fazendo assim que ela nao execute a função desejada


usar um while dentro de outro while ele basicamente terminar a sequencia do while interno para terminar a do de fora:

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas: #esse while so começa a contar apartir do momento que o while que esta na parte de dentro termina a contagem
    coluna = 1
    while coluna <=qtd_colunas:  # esse while comanda as ações pois ele conta primeiro para sairmos da ação dele e comecar a contar o de fora 
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')

"""

contador = 0

while contador < 100:
    contador += 1 # atribuido na pratica para ver que ele continuará somando o 1
    
    if contador == 20: # aqui determinei que quando o contador fosse 20 ele volte para o while para contar pulando o numero 20 e a contagem ficaria (18,19,21,22)
        continue
    
    print(contador)
   
    
print('acabou')