nome = input('Nome: ')
if len(nome) < 3:
    invalid = True
    while invalid:
        nome = input('Nome: ')
        if len(nome) > 3:
            invalid = False
idade = int(input('Idade: '))
if idade <= 0 or idade >= 150:
    invalid = True
    while invalid:
        idade = int(input('Idade: '))
        if 0 <= idade <= 150:
            invalid = False
sal = float(input('Salário: '))
if sal <= 0:
    invalid = True
    while invalid:
        sal = float(input('Salário: '))
        if sal > 0:
            invalid = False
sexo = input('Sexo: ')
if sexo != 'm' or sexo != 'f':
    invalid = True
    while invalid:
        sexo = input('Sexo: ')
        if sexo == 'm' or sexo == 'f':
            invalid = False
ec = input('Estado Civil: ')
if ec != 's' or ec != 'c' or ec != 'v' or ec != 'd':
    invalid = True
    while invalid:
        ec = input('Estado Civil: ')
        if ec == 's' or ec == 'c' or ec == 'v' or ec == 'd':
            invalid = False
