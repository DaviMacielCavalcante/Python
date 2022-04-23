n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
if n1 < n2:
    print('{} é o maior número'.format(n2))
elif n1 > n2:
    print('{} é o maior número'.format(n1))
else:
    print('Os valores {} e {} são iguais'.format(n1, n2))
