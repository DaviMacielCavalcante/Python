numero = input('Informe o seu número: ')
horasTrabalhadas = input('Informe a quantidade de horas trabalhadas: ')
valorHoras = input('Informe o valor recebido por hora: ')

NUMBER = int(numero)
WORKED_HOURS = int(horasTrabalhadas)
HOUR_VALUE = float(valorHoras)
salario = WORKED_HOURS * HOUR_VALUE

print(f'{NUMBER  = }')
print(f'U$ {salario:.2f}')