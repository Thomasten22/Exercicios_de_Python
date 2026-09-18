'''fatiamento de strings
012345678
Ola mundo
-987654321
fatiamento [i:f:p][::]

OBS: a função len retorna a qtd
de caracteres da str
os : sao quem indica que é para ser fatiado'''

variavel = 'Olá mundo'
print(variavel[4:])#dessa maneira foi fatiado somente a parte 'MUNDO'
print(variavel[4:8])#dessa maneira foi fatiado somente a parte 'MUND'
print(variavel[0:5])#dessa maneira foi fatiado somente a parte 'Ola M'
print(variavel[:5])#dessa maneira foi fatiado somente a parte 'Ola M' dessa maneira conseguimos omitir o final
print(variavel[-8:-2])#mesmo conceito com numero negativo
print(len(variavel))#metodo len faz contagem de caracteres, dessa maneira ele consegue enxergar que existem 9 caracteres na str
print(variavel[0:len(variavel):1])# essa é o teste da função P - passo que determina de quantos em quantos caracteres ela vai pular, ela ja vem como padrao de 1 e dessa maneira vai retornar ( Ola mundo) normalmente
print(variavel[0:9:2])# vai ficar todo estranho porque vai printrar 1 e pular 1 caracterer e vai ficar assim (Oámno)
print(variavel[::-1])# dessa maneira ele vai inverter a palavra 




