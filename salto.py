import os

s = 0
while s == 0:

    print("Menu Inicial")
    print("\n1- Registrar \n2- Sair")

    x = int(input("Selecione: "))

    if x == 1:
        nome = int(input("Selecione o nome do participante: "))

        print("Saltos")

        a = float(input("Informe um número: "))
        b = float(input("Informe um número: "))
        c = float(input("Informe um número: "))
        d = float(input("Informe um número: "))
        e = float(input("Informe um número: "))

        saltos = (a + b + c + d + e)
        
        resposta = (saltos/5)
        print(f"\nA media dos saltos é {resposta}")

        print("1- Alterar \n2- Listar \n3- Sair")
        q = int(input("Selecione: "))

        if q == 1:
            z = int(input("\nQual o valor que você deseja colocar: "))
        print(f"A nova média é {z}")

        if q == 2:
            print(f"Participante:\n{nome}")
            print(f"Saltos: \n{a}, {b}, {c}, {d}, {e}")

    if x == 2:
        s = 1


os.system("pause")