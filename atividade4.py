s = 1
while s == 1:

    x = int(input("Informe o produto que deseja: "))

    if (x == 1):
        print("O valor do produto é R$10,00")
    elif (x == 2):
        print("O valor do produto é R$20,00")
    elif (x == 3):
        print("O valor do produto é R$30,00")
    elif (x == 4):
        print("O valor do produto é R$40,00")
    elif (x == 5):
        print("O valor do produto é R$50,00")
    else:
        print("O produto não está disponivel")

    y = input("Se quiser sair, digite 1: ")

    if y == 1:
        s = 0 

  