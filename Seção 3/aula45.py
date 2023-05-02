"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = 'Luiz' #iterável
iterador = iter(texto) # iterador

while True:
    try :
        print(next(iterador))
    except StopIteration:
        break

