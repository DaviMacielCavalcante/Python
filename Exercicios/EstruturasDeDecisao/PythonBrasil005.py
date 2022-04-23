n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
if m == 10 :
    print('Aprovado com distinção')
elif m < 7 :
    print('Reprovado')
elif m >= 7 :
    print('Aprovado')

