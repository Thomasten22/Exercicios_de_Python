'''
usar o formatador F conseguimos formatar frases na string e fazendo elas pegarem seus valores passados acima lemnbrando sempre de passar {}
para ativa a formatacao

colocando logo apos a altura (como no exemplo abaixo) vejo que para aparecer dois numeros apos a casa decimal por conta do :.2 os numeros
passados apos o ponto como de exemplo esta o 2 fala quantas casa serao passadas apos a casa decimal 

'''
nome = str('Thomas Victor')
altura = float(1.85)
peso = int(79.9)
imc = float(peso / (altura * altura))

linha_1 = f'{nome} tem {altura:.2f} de altura'#aqui esta a formatacao de srt vemos usar as variaveis que passamos entre chaves
linha_2 = f'pesa {peso} quilos e seu imc e {imc}'#aqui esta a formatacao de srt vemos usar as variaveis que passamos entre chaves

print(linha_1)
print(linha_2)

