"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        continue

    if contador >= 10 and contador <= 27:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')