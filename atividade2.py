s = 1
while s == 1:


    a=2
    b=6
    c=4
    d=5
    e=1

    n_num =[a,b,c,d,e]
    n = len(n_num)
    n_num.sort ()

if n % 2 == 0:
        median1 = n_num [n//2]
        median2 = n_num [n//2]
        median = (median1 + median)/2
else:
    median = n_num [n//2]
    print("mediana é: "+ str(median)) 

    y = input("Se quiser sair digite 1: ")
    if y == 1:
        s = 0

