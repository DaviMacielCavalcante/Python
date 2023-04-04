"""Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é RS%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))