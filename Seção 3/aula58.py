"""
Faça uma lista de compras com listas
O usuário deve ter a possbilidade de inserir, apagar e listar os valoreas da lista.
Não permite que o programa quebre com erros de índices inexistentes na lista.
"""

# Minha solução:

import os;

lista = ['Pão', 'Queijo', 'Presunto']

while True:
    try:
        print('Selecione uma opção')
        opcao = input('[i]nserir [a]pagar [l]istar: ')
        if opcao == 'i':
            os.system('cls')
            item = input('Item: ')
            lista.append(item)
        elif opcao == 'a':
            indice = input('Indice: ')
            lista.pop(int(indice))
        elif opcao == 'l':
            os.system('cls')

            # Acrescentei a checagem do tamanho da lista depois de ver o código do prof
            if len(lista) == 0:
                print('Nada para listar')

            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print('Operação Inválida!')
    # Acrescentei a o tratamento de execeções específicas após ver a solução do prof
    except IndexError:
        print('Índice inexistente. Digite um valor válido!')
    except ValueError:
        print('Por favor digite um número inteiro')
    except Exception:
        print('Erro Desconhecido')

# Solução do prof:

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try: 
            indice = int(indice_str)
            del lista[indice]
        except IndexError:
            print('Índice inexistente. Digite um valor válido!')
        except ValueError:
            print('Por favor digite um número inteiro')
        except Exception:
            print('Erro Desconhecido')
    elif opcao == 'l':
        os.system('clear')
    
        if len(lista) ==0:
            print('Nada para listar')

            for i,valor in enumerate(lista):
                print(i, valor)
    else:
        print('Por favor, escolha i, a ou l')