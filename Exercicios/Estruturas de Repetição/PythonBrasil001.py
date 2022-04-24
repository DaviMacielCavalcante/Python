nota = float(input('Informe uma nota: '))
if nota < 0 or nota > 10:
    invalid = True
    while invalid:
        nota = float(input('Informe uma nota: '))
        if 0 <= nota <= 10:
            invalid = False
