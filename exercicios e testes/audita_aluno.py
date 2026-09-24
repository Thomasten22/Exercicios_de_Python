alunos_magia = {
    "Harry": {"Expelliarmus", "Expecto Patronum", "Lumos"},
    "Hermione": {"Expelliarmus", "Expecto Patronum", "Lumos", "Alohomora", "Wingardium Leviosa"},
    "Rony": {"Lumos", "Expelliarmus"}
}

grade_obrigatoria = {"Expelliarmus", "Expecto Patronum", "Lumos", "Alohomora"}

def auditar_alunos(dicionario_alunos, obrigatorios):
    todos_os_feitcos = set()
    alunos_nota10 = ''
    
    for alunos, magias in dicionario_alunos.items():
        todos_os_feitcos.update(magias)
        
        if obrigatorios <= magias  :
            alunos_nota10 = alunos
    
    feitico_intermediario = todos_os_feitcos - obrigatorios
        
    print(f'fetiço que so a {alunos_nota10} apreendeu fora da grade basica da escola: {feitico_intermediario}')
    print()
    print(f' {alunos_nota10} é nosso(a) melhor aluno(a) !')
    
    
auditar_alunos(alunos_magia,grade_obrigatoria)