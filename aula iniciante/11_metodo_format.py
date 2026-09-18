'''
nesse metodo apredemos do modo format e que seu metodo de acesso e na sequencia passada para ele sempre da esqueda para a direita
no exemplo abaixo passei os nomes para as variaveis e quando passamos isso pelo .format(a,b,c) ele pega os valores nas chaves na
sequencia passada

no exemplo do d posso passar dentro dele como ele e um numero decimal posso passa o :.2f para ainda ter a casa decimal

conseguimos tambem repetir valores se dentro deles colocarmos seu numero de casa comecando sempre do zero

EXEMPLO = string = 'a={0} b={1} c={2} d={3:.2f}' assim passaria noormal
string ='a={0} a={0} a={0} b={1} c={2} d={3:.2f}' assim passaria o A 3 vezes ate pular para o B
'''
a = 'Thomas'
b = 'BRABAO'
c = 1.1
d = 2.1 #variavel passada para emplementar o :.2f e assim ter uma casa decimal adicional (2.10)

string = 'a={} b={} c={} d={:.2f}'#parametro passado entre chaves 
formato = string.format(a, b, c, d)#aqui esta o coracao, o metodo format com sua sequencia que e executada na sequencia da direita para a esquerda

print(formato)