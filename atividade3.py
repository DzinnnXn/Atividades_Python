s = 1 
while s == 1:

    A = int(input("Digite o primeiro número"))
    B = int(input("Digite o segundo número"))
    C = int(input("Digite o terceiro número"))

    if A > B and A > C:
        max1 = A
        if B > C:
            print(f"A mediana é: {B}")
        else:
            print(f"A mediana é: {C}")

    if B > A and B > C:
        max1 = B
        if A > C:
            print(f"A mediana é: {A}")
        else:
            print(f"A mediana é: {C}")

    if C > A and C > B:
        max1 = C
        if A > B:
            print(f"A mediana é: {A}")
        else:
            print(f"A mediana é: {B}")

            y = input("Se quiser sair, digite 1: ")
            if y == 1:
                s = 0