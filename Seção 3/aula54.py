"""
Exercício 
Exiba os índices da lista
"""
# Minha solução
# lista = ['Maria', 'Helena', 'Luiz']
# i = 0
# for nome in lista:
#     print(i, nome, type(nome))
#     i+= 1

#Solução do prof
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))