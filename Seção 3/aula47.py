import os

palavraRevelada = False;
palavraSecreta = 'sebastian';
letras_acertadas = '';
numero_tentativas = 0;

while (palavraRevelada != True):    
    letra = input('Digite uma letra: ')
    numero_tentativas += 1;

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra in palavraSecreta:
        letras_acertadas += letra
    
    palavra_formada = '';
    for letra_secreta in palavraSecreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta;
        else:
            palavra_formada += '*';
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavraSecreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra era: ', palavraSecreta)
        print('Tentativas: ', numero_tentativas)
        palavraRevelada = True;