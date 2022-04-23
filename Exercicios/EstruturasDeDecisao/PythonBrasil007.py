n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
n3 = float(input('Informe o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
elif n3 > n1 and n3 > n2:
    print('{} é o maior número'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor número'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é o menor número'.format(n2))
elif n3 < n1 and n3 < n2:
    print('{} é o menor número'.format(n3))