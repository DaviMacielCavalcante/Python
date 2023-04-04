distancia = input('Distância percorrida: ')
litrosConsumidos = input('Litros Consumidos: ')

DISTANCIA = int(distancia)
LITROS_CONSUMIDOS = float(litrosConsumidos)
MEDIA_CONSUMO = DISTANCIA / LITROS_CONSUMIDOS

print(f'{MEDIA_CONSUMO:.3f} km/l')