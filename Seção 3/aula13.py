nome = 'Davi Cavalcante'
altura = 1.68
peso = 90
imc = peso / (altura ** 2)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'

print(linha_1)
print(linha_2)
print(f'{imc:.2f}')