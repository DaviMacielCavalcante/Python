a = input('Informe o primeiro valor: ')
b = input('Informe o segundo valor: ')
c = input('Informe o terceiro valor: ')

A = int(a)
B = int(b)
C = int(c)

maiorAB = (A + B + abs(A - B)) / 2
maiorABC = (maiorAB + C + abs(maiorAB - C)) / 2


print(f'{maiorABC:.0f} é o maior')