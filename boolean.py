'''
tipo Boolean -> booleano -> valores logicos, verdadeiro ou falso
EXEMPLO: sim(True), não(False)
existem varios operadores logicos que podem ser utilizados para comparar valores booleanos, como:
== (igual) que e um operador logico que compara dois valores e retorna True se eles forem iguais,
caso contrario retorna False
exemplo:
'''
print(10 == 10.0)  # True(sim) nesse exemplo o valor 10 e igual a 10.0, mesmo sendo tipos diferentes, int e float
print(9 == 11)  # False(não)
print(21 == 21)  # True(sim)
print('21' == 21)  # False(não) nesse exemplo o valor '21' e diferente de 21, mesmo sendo o mesmo numero, pois um e string e outro e int
print(type(21) == type(21.0))  # False(não) nesse exemplo o valor 21 e do tipo int e 21.0 e do tipo float



