import os

s = 1
while s == 1:

    x = float(input("informe um número: "))

    if x < 0:
        print("O seu número é negativo")
    elif x == 0:
        print("O seu número é zero")
    else:
        print("O seu número é positivo")

        y = input("Se quiser sair, digite 1: ")
        if y == 1:
            s = 0

    