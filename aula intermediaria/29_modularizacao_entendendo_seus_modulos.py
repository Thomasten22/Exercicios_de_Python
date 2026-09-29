# Entendendo seus proprios modulos Python
# O primeiro modulo executado chama-se __main__
# Voce pode importar outro modulo inteiro ou parte do modulo
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não conhece pastas e módulos acima do __main_- por padrão
# O python conhece todos os modulos e pacotes presentes no caminhos de sys.path

import sys
sys.path.append('c:/Users/thoma/OneDrive') #indiquei ao sys tambem buscar se tem algo na pasta home 

import testePython # estou importando da pasta que eu adicionei via append ('c:/Users/thoma/OneDrive')


import ExtencaoAulaModulo_29 # como se importa de um arquivo para o outro e dessa forma conseguimos trazer coisas especificas de la

print('Este modulo se chama', __name__) # aqui vai da retornar o arquivo da estenção e tambem o do modulo, vai dar o nome da extenção e depois o da main (a padrao)

print(*sys.path, sep='\n') # esta procurando no meu computador aonde tem arquivos de modulos de python