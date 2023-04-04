"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))

condicao = False

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça algo')

print(passou_no_if)