"""
Introdução ao desempcotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# nome1, *_ = nomes
_, _, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nomes)
print(_)
print(nome2)
print(*_)