valor1 = input("Informe o primeiro valor: ")
valor2 = input("Informe o segundo valor: ")

numero1 = int(valor1)
numero2 = int(valor2)

if (numero1 == numero2) :
    print('Valores iguais')
elif (numero1 > numero2) :
    print(f'O {numero1=} é maior que {numero2=}')
else :
    print(f'O {numero2=} é maior que {numero1=}')