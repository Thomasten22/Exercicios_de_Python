ingredientes_coletados = {
    "Arthur": {"Raiz de Mandrágora", "Olho de Dragão", "Pó de Fada"},
    "Merlin": {"Pó de Fada", "Essência Estelar", "Raiz de Mandrágora"},
    "Lancelot": {"Olho de Dragão", "Escama de Serpente"}
}

receitas_pocoes = {
    "Poção de Cura": {"Raiz de Mandrágora", "Pó de Fada"},
    "Poção de Invisibilidade": {"Olho de Dragão", "Essência Estelar"},
    "Poção da Imortalidade": {"Raiz de Mandrágora", "Olho de Dragão", "Essência Estelar", "Lágrima de Fênix"}
}

def verificar_pocoes(ingredientes,receitas):
    todos_ingredientes = set()
    
    for mago, ingrediente in ingredientes.items():
        todos_ingredientes.update(ingrediente)
        
    poces_possiveis = []
    for nome_pocao, igrediente_necessario in receitas.items():
        if igrediente_necessario <= todos_ingredientes:
            poces_possiveis.append(nome_pocao)
        
    print(f'Todos os ingredientes disponiveis na Guilda: {todos_ingredientes}')
    print()
    print(f'Poções disponiveis para a confecção: {poces_possiveis}')
    
    


verificar_pocoes(ingredientes_coletados,receitas_pocoes)