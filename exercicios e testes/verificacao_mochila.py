

# Dicionário com o nome de cada amigo e os itens na mochila deles
mochilas_amigos = {
    "Você": {"Barraca", "Lanterna", "Comida", "Água"},
    "Betin": {"Isqueiro", "Lanterna", "Saco de dormir", "Comida"},
    "Predes": {"Água", "Repelente", "Kit de Primeiros Socorros"},
    "Guilherme": {"Barraca", "Isqueiro", "Protetor solar"}
}

# Set com os itens que SÃO OBRIGATÓRIOS para a sobrevivência
itens_obrigatorios = {
    "Lanterna", 
    "Água", 
    "Barraca", 
    "Kit de Primeiros Socorros", 
    "Isqueiro", 
    "Apito" # Item de propósito que ninguém levou!
}

def revisar_mochilas(levando,obrigatorios):
    itens_mochilas = set()
    itens_duplicados = set()
    itens_vistos = set()
    
    for pessoa, mochila in levando.items():
        itens_mochilas.update(mochila)
        
        for item in mochila:
            if item in itens_vistos:
                itens_duplicados.add(item)
            else:
                itens_vistos.add(item)
        
        
    itens_faltantes = itens_obrigatorios - itens_mochilas
    
    print(f'itens que ficaram faltando levar: {itens_faltantes}')
    print()
    print(f'itens que esta sendo levado por mais de uma pessoa: {itens_duplicados}')
    

revisar_mochilas(mochilas_amigos,itens_obrigatorios)



