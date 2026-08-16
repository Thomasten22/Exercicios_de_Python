import random

counter = 5
aleatoric_number = random.randint(0, 100)

while counter > 0:
    try:
        escolha = int(input("escolha um número inteiro de 0 a 100: "))

        if escolha > 100 and escolha < 0:
            print("o número deve ser de 0 a 100!")
            counter += 1
        elif escolha > aleatoric_number:
            print("seu número é maior do que o número aleatório!")
        elif escolha < aleatoric_number:
            print("seu número é menor do que o número aleatório")
        else:
            print(f"Número correto!")
            break

        counter -= 1
        print(f"{counter} tentativas restantes")
    except:
        print("entrada inválida")

print(f"o número aleatório era {aleatoric_number}!")
