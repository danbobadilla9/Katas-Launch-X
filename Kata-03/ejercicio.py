velocidad = int(input('Ingresa la velocidad del asteroide en km/s'))
#UNI AMBOS PROBLEMAS 1 y 2 EN UNO SOLO
if velocidad >= 25:
    print('Alerta!!!')
    if velocidad >= 20:
        print('Rayo de luz!')
    else:
        print('Sin rayo de luz')
else:
    print('No hay problema')

tam = int(input('Tamaño del asteroide'))

if tam > 25 and tam < 1000:
    print('Golpeo la Tierra')
else: 
    if velocidad >= 25 :
        print('Alerta!!!!!!!')
    elif velocidad >= 20:
        print('Rayo de luz')
    else:
        print('No hay peligro')
