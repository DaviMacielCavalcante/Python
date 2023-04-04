"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero_string = input('Digite um número inteiro: ')


if numero_string.isdigit():
    numero_inteiro = int(numero_string)
    if numero_inteiro % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
else:
    print('Este não é um número inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


hora = input('Informe a hora atual: ')
hora_int = int(hora)

bom_dia = hora_int >=0 and hora_int <=11
boa_tarde = hora_int >=12 and hora_int <=17
boa_noite = hora_int >=18 and hora_int <=23

if bom_dia:
    print('Bom dia')
elif boa_tarde:
    print('Boa tarde')
elif boa_noite:
    print('Boa noite')
else:
    print('Hora inválida')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"/ maior que 6 escreva "Seu nome é muito grande".
"""

primeiro_nome = input('Informe seu primeiro nome: ')
tamanho_nome = len(primeiro_nome)

print(tamanho_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é grande')
else:
    print('Digite mais uma letra')
