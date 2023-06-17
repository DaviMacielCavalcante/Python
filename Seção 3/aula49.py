"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - indíces e fatiamento
Métodos úteis: 
        append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#         0   1  2   3    4  5 
lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(70);
lista.pop();
lista.append(80);
lista.append(90);
ultimoValor = lista.pop();
ultimoValor = lista.pop(3);
print(lista, 'Removido: ', ultimoValor)