estoque_pirata = {
    "Luffy": {"Banana", "Maçã", "Gomu Gomu no Mi"},
    "Law": {"Maçã", "Laranja", "Ope Ope no Mi"},
    "Kid": {"Banana", "Laranja", "Jiki Jiki no Mi"},
    "Boa Hancock": {"Banana", "Maçã", "Mero Mero no Mi"}
}

def verificador_frutas(estoque):
    frutas_totais = []
    frutas_duplicadas = set()
    frutas_vistas = set()
    
    for tripulante, fruta in estoque.items():
        frutas_totais.append(fruta)
        for item in fruta:
            if item in frutas_vistas:
                frutas_duplicadas.add(item)
            else:
                frutas_vistas.add(item)
    
    print(f'frutas que foram vistas em outros navios: {frutas_duplicadas}')
    
    
verificador_frutas(estoque_pirata)
    