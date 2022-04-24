login = input('Informe o login: ')
senha = input('Informe a senha: ')
if login == senha:
    invalid = True
    while invalid:
        login = input('Informe o login: ')
        senha = input('Informe a senha: ')
        if login != senha:
            invalid = False
