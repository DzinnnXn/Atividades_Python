import os

x = int(input("Informe a sua idade?: "))

if x <= 5:
    print("Você está na categoria Infantil A")
elif x <= 10:
    print("Você está na categoria Infantil B")
elif x <= 15:
    print("Você está na categoria Juvenil A")
elif x <= 17:
    print("Você está na categoria Juvenil B")
else:
    print("Você está na categoria Adulto")

os.system("pause")
