"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - indíces e fatiamento
Métodos úteis: 
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido
        pop - Remove um item no índice escolhido
        del - Apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1  2   3 
lista = [10, 20, 30, 40]
lista.append('Davi')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista)