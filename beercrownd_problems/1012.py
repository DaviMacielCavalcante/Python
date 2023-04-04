a = input('Informe o primeiro valor: ')
b = input('Informe o segundo valor: ')
c = input('Informe o terceiro valor: ')

A = float(a)
B = float(b)
C = float(c)

areaTriangulo = (A * C) / 2
areaCirculo = 3.14159 * (C ** 2)
areaTrapezio = ((A + B) * C) / 2
areaQuadrado = B ** 2
areaRetangulo = A * B

print(f'TRIANGULO: {areaTriangulo:.3f}')
print(f'CÍRCULO: {areaCirculo:.3f}')
print(f'TRAPÉZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETÂNGULO: {areaRetangulo:.3f}')