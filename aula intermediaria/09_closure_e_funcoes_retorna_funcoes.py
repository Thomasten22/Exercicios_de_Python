'''
Closure e funções que retornam outras funções

aprendemos a definir uma função dentro de outra e so passar um ou mais argumentos somente na hora da execução do codigo assim salvamos menos coisas
na memoria ram, dessa maneira o metodo de falar bom dia ficou um pouco descomplicado pois ja esta salvo na memoria o bom dia e o boa noite
quando chamaos a variavel criada so precissamos passar  nome que o bom dia ou o boa noite ja esta pre carregado 

'''

def criar_saudacao(saudacao): # estamos definindo uma função que o argumento dela pede qual a saudação que iremos fazer!!
    def nome(nome): # definimos outra função dentro da primeira função que recebe o parametro de nome
        return f'{saudacao}, {nome}!' # aqui dentro devolvemos a saudação passada e o nome ( lembrando que conseguimos pegar arquivos fora da função porem nao conseguimos passar os dados internos sem chamar a função dela)
    return nome # estamos retornando nome porem sem passar os parenteses com o parametro, somente requisitando a função

falar_bom_dia = criar_saudacao('Bom dia') # aqui vem a magica, estamos somente passando o primeiro argumento aqui que é a saudação
falar_boa_noite = criar_saudacao('Boa noite') # aqui vem a magica, estamos somente passando o primeiro argumento aqui que é a saudação

print(falar_boa_noite('Leticia')) # chamamos a variavel e colocamos o parenteses aqui para podermos passar o segundo parametro, que assim o codigo so salva um argumento e quando passamos o segundo argumento ele so executa
print(falar_bom_dia('Thomas'))

'''Extra - Mais sobre escopo, namespace e closures (2025 / 2026)
Costumo criar MUITOS vídeos gratuitos explicando alguns recursos da linguagem. Para escopo, namespace e closures no Python, criei três vídeos sobre isso nos mínimos detalhes.

Considere isso como um extra que você está ganhando neste curso (não faz parte da carga horária, é apenas um presente).

Quando eu digo "nos mínimos detalhes", é REALMENTE nos mínimos detalhes. Isso pode deixar esses vídeos um pouco mais complexos do que o que você veio assistindo até aqui. Posso falar de coisas que você ainda nem aprendeu nas aulas anteriores. Mesmo assim, vou deixar esses links para você, já que é sobre o mesmo assunto (funções, closures, escopo e namespace).

Se sentir dificuldades assistindo a esses vídeos, não se preocupe, alguns assuntos serão mencionados no futuro ao longo das aulas posteriores.

Sem mais... Seguem os links:

Escopo e Namespace - Parte 1 (https://www.youtube.com/watch?v=GkgbSIYSHUg)

LEGB, Global, Nonlocal, Enclosing e Call Stack - Parte 2 (https://www.youtube.com/watch?v=U8oF5WWpEGk)

Closures em Python: guia DEFINITIVO (https://www.youtube.com/watch?v=8-H-G2t295A)''' 