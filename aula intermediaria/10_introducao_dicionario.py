'''Dicionarios em Python (tipo dict)
Dicionarios são estruturas de dados do tipo par de "chave" e "valor".
CHAVES podem ser consideradas como "indice" que vimos na lista e podem ser de tipos imutaveis
COMO: str, int, float, bool, tuple, etc...

VALOR pode ser qualquer tipo, incluindo outro dicionario

usamos chaves - {} - ou a classe dict para criar dicionarios.

Imutaveis: str, int, float, bool, tuple

Mutavel: dict, list
'''
# maneira correta de escrever um dicionario
pessoa = {
    'nome': 'Thomas',
    'sobrenome': 'Victor',
    'idade': 27,
    'altura': 1.85,
    'endereços': [
        {'rua': 'Rua josé joaquim rodrigues','numero': 577},
        {'rua': 'Rua Vereador Carlos Canedo','numero': 161},
    ],
}
print(pessoa,type(pessoa)) #estamos chamando a dict pessoa e o tipo dela

#meio de acessar os indices de dentro da dict pessoa 
print(pessoa['idade'])

# usando for para acessar os indices da lista e chamando dinamicamente a chave 
for chave in pessoa:
    print(chave, pessoa[chave]) # estamos acessando a chave eo que foi preenchido nos indices
    


