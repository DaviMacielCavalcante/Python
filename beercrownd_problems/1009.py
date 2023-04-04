nome = input('Informe o seu nome: ')
salario = input('Informe o seu salário: ')
vendaTotal = input('Informe o valor adquirido com as vendas: ')

SALARIO = float(salario)
VENDAS_TOTAIS = float(vendaTotal)

salarioFinal = SALARIO + (VENDAS_TOTAIS * 0.15)

print(f'TOTAL = R$ {salarioFinal:.2f}')