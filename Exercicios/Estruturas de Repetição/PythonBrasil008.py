cont = 1
maior = 0
soma = 0
while cont <= 5:
    n = float(input('Informe um número:'))
    if n > maior:
        maior = n
    soma += n
    cont += 1
print(maior)
med = soma / 5
print(soma)
print(med)
