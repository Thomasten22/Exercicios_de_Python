mercado = [
    ("Espada Wado Ichimonji", 1200, 1),
    ("Den Den Mushi", 300, 5),
    ("Fruta do Diabo Artificial", 5000, 2),
    ("Mapa do Novo Mundo", 150, 10),
    ("Casaco de Peles", 450, 4)
]

mais_caros = list(filter(lambda x: x[1] >= 400, mercado))

#estamos aplicando o desconto porem o python joga fora os outros itens da tupla entao temos que estanciar todos x[0], x[1] e x[2]
com_desconto = list(map(lambda x: (x[0], x[1] * 0.9, x[2]), mais_caros))

ordem_decrescente = sorted(com_desconto, key=lambda x: x[1], reverse=True)


print(ordem_decrescente)