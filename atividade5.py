import os

mi = 0
val = 0
alt = 0
s = 0
menu2 = 0

#MENU INICIAL
while mi == 0:
    print("Menu Inicial\n")
    print("1- Valores \n2- Sair")
    x = int(input("Selecione: "))


    #VALORES
    if x == 1:
        mi = 1
        val = 1

    #SAIR
    if x == 2:
        mi = 1
        s = 1
#VALORES
    while val == 1:
        print("Valores\n")
        saltos = []
        soma = 0
        for i in range(5):
            x  = int(input("Digite um número: "))        

    soma = saltos[0] + saltos[1] + saltos[2] + saltos[3] + saltos[4]
    resultado = (soma/5)
    print(f"A média é {resultado}")
    val = 0
    menu2 = 1

    #ALTERAR

    while menu2 == 1:
        print("1- Alterar \n2- Voltar \n3- Sair")

        z = int(input("Selecione: "))


        if z == 1:
            print("Alterar\n")
            y = int(input("Altere a média: "))

            print(f"Agora a média é {y}")

        if z == 2:
            s = 0

        os.system("pause")