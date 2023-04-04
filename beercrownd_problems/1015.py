import math
x1 = input('Digite a coordenada X1: ')
y1 = input('Digite a coordenada Y1: ')
x2 = input('Digite a coordenada X2: ')
y2 = input('Digite a coordenada Y2: ')

X1 = float(x1)
X2 = float(x2)
Y1 = float(y1)
Y2 = float(y2)

DISTANCE = math.sqrt(pow(X2 - X1, 2) + pow(Y2 - Y1, 2))

print(f'{DISTANCE:.4f}')