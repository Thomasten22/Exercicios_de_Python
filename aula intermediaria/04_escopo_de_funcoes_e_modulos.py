'''
Escopo de funções em Python
Escopo significa o local onde aquele codigo pode atingir
Existe escopo global e local
O escopo global é o escopo onde todo o codigo é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
podemos redefinir a variavel de dentro pra fora usando global (mas isso e má pratica de programação)

                    ATENÇÃO

AS FUNCOES SO CONSEGUEM COMUNICAR DE FORA PRA DENTRO, NAO DE DENTRO PRA FORA, NO EXEMPLO ABAIXO O ESCOPO DE DENTRO, CONSEGUE ACESSAR TUDO QUE ESTA FORA DELE 
POREM O ESCOPO DE FORA NAO ACESSA O QUE ESTA NO ESCOPO DE DENTRO, SE TENTARMOS ACESSAR O (y) COM O ESCOPO DE FORA ESTOURA UM ERRO QUE NAO FOI DEFINIDO O MESMO

 conseguimos redeclarar a variavel dentro do escopo sem trocar a variavel de fora
 
a palavra global faz uma variavel do escopo externo ser a mesma do escopo interno 
'''
x = 1 # essa variavel foi definida fora do escopo e consegue ser acessada por todos eles

def escopo_fora(): # esse escopo consegue acessar tudo que esta fora dele
    global x # estou dizendo que o valor de dentro do escopo local serve para o escopo global
    x = 10  # redefini somente dentro do escopo da função que x = 10 sem alterar o que esta fora
    
    def escopo_dentro(): # esse escopo acessa tudo que esta fora dele porem o que tem dentro dele (y) na consegue ser acessado pelo escopo de fora
        global x # estou dizendo que o valor de dentro do escopo local serve para o escopo global
        x = 11 # redefini novamente  o x para esse escopo e dentro dele x é 11 sem alterar novamente o que esta fora
        y = 4 # ele esta protegido dentro do escopo 2 e nao pode ser requisitado no escopo de fora, somente no escopo dois
        print(x, y)
        
    escopo_dentro()
    print(x)


print(x) # aqui vai mostrar o resultado de x que foi definido fora do escopo
escopo_fora() # traz a função mostrando tudo de dentro do seu corpo
print(x)# aqui ele vai executar o valor do x global que eu redefini dentro da função (x = 11)


'''aparentemente o Python quando damos print nas funcoes e variaveis ele interpreta assim:
1° - variavel definida fora do escopo 
2° - função definida
3° - variavel que foi alterada globalmente dentro da função

ele primeiro executa o que esta no escopo global (escopo do arquivo em si) e depois ele pula para o que definimos e quando ele ve que definimos o x para 11 dentro da função 
ele altera e o proximo print vira o que foi definido dentro do escopo local ( dentro da função)
'''