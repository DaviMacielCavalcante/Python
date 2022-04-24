aP = 80000
bP = 200000
taxA = float(input('Informe a taxa de crescimento de A: '))
while taxA <= 0:
    taxA = float(input('Informe a taxa de crescimento de A: '))
taxB = float(input('Informe a taxa de crescimento de B: '))
while taxB <= 0:
    taxB = float(input('Informe a taxa de crescimento de B: '))
anos = 0
while bP >= aP:
    aP += (aP * taxA)
    bP += (bP * taxB)
    anos += 1
print('{} anos para que a população do país A supere a do país B'.format(anos))

