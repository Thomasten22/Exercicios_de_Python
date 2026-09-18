# Dica rápida: Em Python, é uma boa prática começar o nome da classe com letra maiúscula (Carro), 
# mas vamos manter minúsculo como você fez para não quebrar nada.
class carro: 
    
    # O __init__ é a porta de entrada. Ele roda sozinho toda vez que você "fabrica" um carro novo.
    def __init__(self, marca, modelo, ano, cor): 
        # O 'self' pega os parâmetros que chegaram e guarda DENTRO do objeto
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
       
    def dados(self):
        # Aqui o 'self' entra em ação para buscar as informações que o __init__ guardou
        print('--- Detalhes do Carro ---')
        print('marca:', self.marca)
        print('modelo:', self.modelo)
        print('ano:', self.ano)
        print('cor:', self.cor)
       
    def estado(self):
        # Novamente o 'self' consultando a propriedade "ano" do próprio carro
        if (self.ano > 2000):
            print('carro em bom estado')
            # Olha que interessante: o self também serve para chamar OUTRO método da mesma classe!
            self.dados()
        else:
            print(self.marca)
            print('o carro deve ser trocado')

# Fabricando os dois carros e passando as informações para o __init__
carro1 = carro('fiat', 'Marea', 1998, 'vermelho')
carro2 = carro('peugeot', '206', 2000, 'prata')

# ❌ Se fizer apenas print(carro1), o Python joga na tela o endereço de memória.

# ✅ O jeito certo usando o método que você construiu:
carro1.dados()



# Você também pode testar a sua lógica de ano chamando o estado:
carro1.estado()