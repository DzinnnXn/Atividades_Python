import os

nome1 = input("Informe seu nome Aluno 01")
idade1 = input(f"Informe sua idade {nome1}: ")

nome2 = input("Informe seu nome Aluno 02")
idade2 = input(f"Informe sua idade {nome2}: ")

if idade1 > idade2:
    print(f"O aluno {nome1} tem {idade1} anos, e o aluno {nome2} tem {idade2} anos.{nome2} é mais velho")
else:
    print(f"O aluno {nome1} tem {idade1} anos, e o aluno {nome2} tem {idade2} anos.{nome1} é mais velho")
    
x = int(idade1) + int(idade2)
print(f"A idade da soma dos alunos é {x}")


os.system("pause")
