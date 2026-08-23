'''
CONSTANTE = "variaveis" que nao vao mudar! 
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade(ruim)
    
BASICAMENTE -> CONSTANTE sao variaveis em escritas em letras maiusculas pois assim mostramos para nos mesmo e outros devs que sao variaveis que nao
pode ser mudadas ao longo do codigo e o exemplo abaixo explica isso com clareza pois os que estao em letras maiusculas sao:
localização do radar == que nao pode ser mudada 
velocidade do radar == que nao pode ser mudada
distancia que o radar atua == nao pode ser mudado tambem 

porque sao coisas que tendem a ficar estaticos porque estao parados no mesmo lugar 
#barra invertida(\) é usado para podermos indicar que o codigo vai continuar na linha de baixo 
'''
velocidade = 61 #velocidade atual do carro
local_carro = 101 #local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega

vel_carro_pass_radar1 = velocidade > RADAR_1 # consigo passar parametros e encurtar eles para quando forem requisitado no codigo ficar mais legivel e limpo
carro_multado_radar1 = local_carro>= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar1:
     print('Carro passou do radar 1')
     
if carro_multado_radar1 and vel_carro_pass_radar1:
        print('carro foi multado no radar 1')
        
         