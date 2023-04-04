codigoProduto1 = input('Informe o código do produto: ')
quantidade1 = input('Informe o número de unidades: ')
preco1 = input('Informe o valor do produto: ')

codigoProduto2 = input('Informe o código do produto: ')
quantidade2 = input('Informe o número de unidades: ')
preco2 = input('Informe o valor do produto: ')

QUANTIDADE_1 = int(quantidade1)
QUANTIDADE_2 = int(quantidade2)
VALOR_1 = float(preco1)
VALOR_2 = float(preco2)

TOTAL = QUANTIDADE_1 * VALOR_1 + QUANTIDADE_2 * VALOR_2

print(f'VALOR A PAGAR: r$ {TOTAL:.2f}')