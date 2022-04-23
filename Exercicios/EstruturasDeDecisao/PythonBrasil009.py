n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
n3 = float(input('Informe o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)

if (n1 > n2 > n3) or (n3 < n2 < n1) or (n1 < n2 < n3):
    print(n2)
elif (n2 < n1 < n3) or (n2 > n1 > n3):
    print(n1)
elif (n1 < n3 < n2) or (n1 > n3 > n2):
    print(n3)

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
elif n3 < n1 and n3 < n2:
    print(n3)

