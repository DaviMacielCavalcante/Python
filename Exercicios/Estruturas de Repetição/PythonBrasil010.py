n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
cont = 0
if n1 > n2:
    cont = n2
    while cont <= n1:
        print(cont, end=" ")
        cont += 1
elif n2 > n1:
    cont = n1
    while cont <= n2:
        print(cont, end=" ")
        cont += 1

