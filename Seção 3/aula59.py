"""
Imprecisão de ponto flutuante
"""
# Trabalhando com o módulo decimal
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
# Retorna uma string
print(f'{numero_3:.2f}')

#Retorna um float
print(round(numero_3, 2))