supernovas = [
    ("Kidd", 3000, "Ativo"),
    ("Killer", 200, "Capturado"),
    ("Zoro", 1111, "Ativo"),
    ("Bege", 350, "Ativo"),
    ("Hawkins", 320, "Capturado"),
    ("Luffy", 3000, "Ativo")
]

tripulacoes_totais = []
for tripulacoes in supernovas:
    tripulacoes_totais.append(tripulacoes)

tripulacoes_totais = tuple(tripulacoes_totais)

ativos = list(filter(lambda x: x[2] == 'Ativo', tripulacoes_totais))
print(f'piratas que ainda precisam ser capturados: {ativos}')
print()

#como passei uma lista com varias tuplas temos que identificar-las com () e passando os argumentos dentro dos parenteses
aliancas = list(map(lambda x: (x[0], x[1] * 1.2, x[2]), ativos))
print(f'valores alterados devido aliancas piratas: {aliancas}')
print()

ordem_valores = sorted(aliancas, key=lambda x: x[1], reverse=True)
print(f'piratas por ordem do mais valioso: {ordem_valores}')
