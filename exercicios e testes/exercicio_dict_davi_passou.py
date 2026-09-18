'''
Crie um gerenciador de tarefas em Python que rode no terminal. 
Permita adicioná, removê, listá e marcá tarefas como concluídas. 
Cada tarefa deve ter um ID, título, status e data de criação. 
Implemente também filtros por status e ordenação por data de criação. 
Não é necessário salvá em arquivo, pode ficá só em memória.
'''
import os
from datetime import datetime

organiza_tarefas = {}

while True:
    
    print("""===== GERENCIADOR DE TAREFAS =====
    1 - Adicionar tarefa
    2 - Remover tarefa
    3 - Listar tarefas
    4 - Marcar como concluída
    5 - Filtrar tarefas
    6 - Ordenar por data
    0 - Sair
    """)
    
    escolha_do_usuario = input('Escolha uma opção:')
    
    try:
        if escolha_do_usuario in ['0', '1', '2', '3', '4', '5', '6']:
            escolha_do_usuario = int(escolha_do_usuario)
            
        else:
            os.system('cls')
            print('voce nao digitou um numero valido')
            
            continue
    
    except ValueError:
        os.system('cls')
        print('voce digitou uma letra')
        continue
        
    if int(escolha_do_usuario )== 0:
        print('você escolheu SAIR')
        break
    
    if escolha_do_usuario == 1:
        os.system('cls')
        titulo = input("Qual o título da tarefa? ")
        data_digitada = input("Qual a data de criação (DD/MM/AAAA)? ")
        data_oficial = datetime.strptime(data_digitada, "%d/%m/%Y")
        
        if len(organiza_tarefas) == 0:
            novo_id = 1
        else:
            novo_id = max(organiza_tarefas.keys()) + 1
            
        nova_tarefa = {
            'id': novo_id,
            "titulo": titulo, 
            "status": "Pendente",
            "data_criacao": data_oficial,
        }
        
        organiza_tarefas[novo_id] = nova_tarefa
        
        
    elif escolha_do_usuario == 2:
        os.system('cls')
        if len(organiza_tarefas) > 0:
            
            for id_tarefa, dados_da_tarefa in organiza_tarefas.items():
                print(id_tarefa,':',dados_da_tarefa)
                
            print('coloque apenas o ID')
            
            apagar_id = input('qual tarefa você deseja apagar?')
            apagar_id = int(apagar_id)
            
            if apagar_id in organiza_tarefas:
                del organiza_tarefas[apagar_id]
                os.system('cls')
            else:
                os.system('cls')
                print('ID não existe')

                continue
        else:
            os.system('cls')
            print('sem listas para apagar!')

            continue
            

    elif escolha_do_usuario == 3:
        
        os.system('cls')
        for id_tarefa, dados in organiza_tarefas.items():
            data_formatada = dados["data_criacao"].strftime("%d/%m/%Y")
            print(f"ID: {id_tarefa} | Tarefa: {dados['titulo']} | Status: {dados['status']} | Criado em: {data_formatada}")
            
        input("\nPressione ENTER para voltar ao início...")
        os.system('cls')
        continue
    
    elif escolha_do_usuario == 4:
        os.system('cls')
        if len(organiza_tarefas) > 0:
            
            for id_tarefa, dados_da_tarefa in organiza_tarefas.items():
                print(id_tarefa,':',dados_da_tarefa)
                
            print('coloque apenas o ID')
            
            alterar_status = input('qual tarefa você deseja alterar o status?')
            alterar_status = int(alterar_status)
            
            if alterar_status in organiza_tarefas:
                organiza_tarefas[alterar_status]['status'] = 'Concluída'
                os.system('cls')
            else:
                os.system('cls')
                print('ID não existe')
                
                continue
        else:
            os.system('cls')
            print('sem listas para alterar!')
            
            continue
                
    elif escolha_do_usuario == 5:
        os.system('cls')
        filtro = input('''o que vc deseja filtrar?
            1 - ID
            2 - titulo
            3 - status
            4 - data de criação
            escolha uma opção:''') 
        
        try:
            if filtro in ['1', '2', '3', '4']:
                filtro = int(filtro)
            
            else:
                os.system('cls')
                print('voce nao digitou um numero valido')
            
                continue
    
        except ValueError:
            os.system('cls')
            print('voce digitou uma letra')
            continue
        
        if len(organiza_tarefas) > 0:
        
            if filtro == 1:
                
                os.system('cls')
                busca_id = int(input("Qual ID você quer buscar? "))
                if busca_id in organiza_tarefas:
                    tarefa = organiza_tarefas[busca_id]
                    data_formatada = tarefa["data_criacao"].strftime("%d/%m/%Y")
                    
                    print("\n--- TAREFA ENCONTRADA ---")
                    print(
                        f"ID: {busca_id} | "
                        f"Título: {tarefa['titulo']} | "
                        f"Status: {tarefa['status']} | "
                        f"Data: {data_formatada}"
                    )
                    
                    input('\nPressione ENTER para voltar ao início...')
                    os.system('cls')
                    continue
                else:
                    print("ID não encontrado.")
                    input('\nPressione ENTER para voltar ao início...')
                    continue
                    
            elif filtro == 2:
                
                os.system('cls')
                busca_titulo = input("Qual titulo você quer buscar? ")
                encontrou = False
                
                for id_tarefa, dados in organiza_tarefas.items():
                    
                    if dados["titulo"].lower() == busca_titulo.lower():
                        print(id_tarefa, ':', dados)
                        encontrou = True
                        input("\nPressione ENTER para voltar ao início...")
                        continue
                        
                    if not encontrou:
                        os.system('cls')
                        print("Nenhuma titulo com esse nome.")
                        continue
                    
            elif filtro == 3:
                
                os.system('cls')
                busca_status = input("Qual status você quer buscar (Pendente/Concluída)? ")
                encontrou = False
                for id_tarefa, dados in organiza_tarefas.items():
                    
                    if dados["status"].lower() == busca_status.lower():
                        print(id_tarefa, ':', dados)
                        encontrou = True
                        input("\nPressione ENTER para voltar ao início...")
                        os.system('cls')
                        continue
                        
                    if not encontrou:
                        os.system('cls')
                        print("Nenhuma tarefa com esse status.")
                        continue
                        
            elif filtro == 4:
                os.system('cls')
                busca_data_str = input("Qual data você quer buscar (DD/MM/AAAA)? ")
                encontrou = False
                
                try:
                    # Transforma o texto digitado em uma data oficial para comparar certo
                    busca_data_obj = datetime.strptime(busca_data_str, "%d/%m/%Y")
                    
                    for id_tarefa, dados in organiza_tarefas.items():
                        if dados["data_criacao"] == busca_data_obj:
                            print(id_tarefa, ':', dados)
                            encontrou = True
                            input("\nPressione ENTER para voltar ao início...")
                            os.system('cls')
                            continue
                            
                    if not encontrou:
                        os.system('cls')
                        print("Nenhuma data correspondente.")
                        
                except ValueError:
                    os.system('cls')
                    print("Formato de data inválido.")
                
                continue
        
        else:
            os.system('cls')
            print('sem tarefas para serem filtradas')
            
            
    elif escolha_do_usuario == 6:
        #os.system('clear')
        if len(organiza_tarefas) > 0:
            lista_para_ordenar = list(organiza_tarefas.values())
            lista_para_ordenar.sort(key=lambda tarefa: tarefa["data_criacao"])
            
            print("\n--- TAREFAS ORDENADAS POR DATA ---")
            for tarefa in lista_para_ordenar:
                print(
                    f"ID: {tarefa['id']} | "
                    f"Título: {tarefa['titulo']} | "
                    f"Status: {tarefa['status']} | "
                    f"Data: {tarefa['data_criacao'].strftime('%d/%m/%Y')}"
                )
            input("\nPressione ENTER para voltar ao início...")
            os.system('cls')
            continue
        else:
            os.system('cls')
            print('Sem tarefas para ordenar!')
            input("\nPressione ENTER para voltar ao início...")
            continue