a = float(input("insira um numero: "))
b = float(input("insira outro numero: "))
c = input("insira qual conta(+,-,/,*): ")

if c == "+":
    print("o resultado da soma: ",a + b)

if c == "-":
      if a >= b:
            print("o resultado da subtração é: ", a - b)
      else:
            print("o resultado da subtração é: ", b - a)

if c == "/":
    print("o resultado da divisão é : ",a / b)

if c == "*":
    print("o resultado da multiplicação é: ",a * b)