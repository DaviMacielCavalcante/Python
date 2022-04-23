t = input('Informe o seu turno [M-Matutino/V-Vespertino/N-Noturno] : ')

if t == 'M' or t == 'm':
    print('Bom dia!')
elif t == 'V' or t == 'v':
    print('Boa tarde!')
elif t == 'N' or t == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido!')

