n1 = float(input('Informe o valor do primeiro produto: '))
n2 = float(input('Informe o valor do segundo produto: '))
n3 = float(input('Informe o valor do terceiro produto: '))

if n1 < n2 and n1 < n3:
    print('{} compre este'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} compre este'.format(n2))
elif n3 < n1 and n3 < n2:
    print('{} compre este'.format(n3))