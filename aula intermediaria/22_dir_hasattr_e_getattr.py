# dir, hasattr e getattr em Python
# dir -> vai mostrar todos os metodos que conseguimos ultilizar com a variavel (se usarmos o debbuger e depois debbuger console conseguimos dar um comando dir(string) ele mostra tudo que da pra usar)
#hasattr -> verifica se o metodo existe na variavel, podemos usar ele com o if e passar ele para verificar se a variavel contem o metodo
#getattr ->  ele consegue verificar se uma variavel criada é um metodo, igual o exemplo a baixo
string = 'thomas'

#exemplo do hasattr ( meu nome na string esta com o t minusculo propositalmente)

if hasattr(string, 'capitalize'): # capitalize é um metodo que coloca a primeira letra em maiusculo string.capitalize
    print('existe o metodo captalize na variavel')
    print(f'alterando para captalize: {string.capitalize()}') # printado com o T maiusculo

print()
#exemplo de getattr (foi passado um metodo que nao precisa de parametro dentro do seu escopo, tendo parametro tem que fazer com a logica dele)

metodo = 'upper' # upper deixa tods as letras em maiusuculo 

if hasattr(string, metodo ): # capitalize é um metodo que coloca a primeira letra em maiusculo string.capitalize
    print('existe o metodo(upper) na variavel')
    print(f'alterando para metodo(upper): {getattr(string, metodo)()}') # tem que ser passado dessa maneira com chamando a funcao e passando as variaveis no escopo do getattr e fora o parentes () para chamar o metodo