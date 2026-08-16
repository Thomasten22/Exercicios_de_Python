"""
Clicar na linha e apertar Ctrl + c copia a linha e cola Ctrl + v cola a linha para baixo
\r\n-> CRLF (carry return line feed)quebra de linha baseada no win se tiver em outro ambiente como mac ou linux
(sistema unix) pode ser so \n -> LF que line feed quebra de linha (o termo \n tambem funciona em windows)
A FUNCAO PASSADA A CIMA CRLF JA VEM COMO PADRAO NA FUNCAO end SE QUISERMOS QUE NAO QUEBRE A LINHA DEVEMOS 
COLOCAR ALGO PARA CONTINUAR TUDO NA MEMSMA LINHA COMO ESTA NO EXEMPLO ABAIXO 

 a funcao sep serve para separar os valores que
 serao impressos no print, por padrao o separador
 e um espaco em branco
"""
print(12, 34, sep="-", end="-")
print(56, 78,sep='-', end="-")
print(9, 10,sep='-', end="")


