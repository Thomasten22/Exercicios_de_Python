''' 
Validador de Entrada e Processador de Notas
Objetivo: Praticar while, try/except, tratamento de exceções e manipulação de listas.

Enunciado: Crie um programa que permita cadastrar notas de alunos (de 0 a 10).

O programa deve pedir a nota no terminal dentro de um laço contínuo.

Se o usuário digitar um valor que não seja número ou um valor fora do intervalo de 0 a 10, exiba uma mensagem de erro com try/except e peça a entrada novamente.

O laço encerra quando o usuário digitar 'fim'.

Ao final, exiba:

A quantidade total de notas válidas inseridas.

A média das notas (com duas casas decimais).

A maior e a menor nota digitada.

Caso nenhuma nota válida tenha sido inserida, exiba um aviso.'''

notas = []


while True:
    nota = input('Digite a nota:').lower()
    
    try:
        if nota == 'sair':
            quit = input('voce deseja sair?').lower()
            if quit == 'sim':
                break
            else:
                continue
        elif float(nota) >= 0 and float(nota) <= 10:
            notas.append(float(nota))
        else:
            print('Digite numero de 0 a 10')
            continue
    except ValueError:
        print('digite apenas Numeros')
        continue
    
if len(notas) > 0:
    notas_formatadas = [f'{nota:.2f}' for nota in notas]
    notas_totais = sum(notas)
    cal_media = notas_totais / len(notas)
    print('As notas inseridas foram:', *notas_formatadas)
    print(f'A media das notas e: {cal_media:.2f}')
    print(f'A maior nota inserida foi: {max(notas):.2f}')
    print(f'A menor nota inserida foi: {min(notas):.2f}')
else:
    print('voce nao inseriu nenhuma nota valida')