aP = 80000
bP = 200000
anos = 0
while bP >= aP:
    aP += (aP * 0.03)
    bP += (bP * 0.015)
    anos += 1
print('{} anos para que a população do país A supere a do país B'.format(anos))

