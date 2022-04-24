cont = 1
maior = 0
while cont <= 5:
    n = float(input('Informe um número:'))
    if n > maior:
        maior = n
    cont += 1
print(maior)