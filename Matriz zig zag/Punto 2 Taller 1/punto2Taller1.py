from Posicion import Posicion


def MovimientoHaciaArriba(posicion, cantidadFilas):

    puedemoverse = posicion.ValidarMovimientoHaciaArriba(cantidadFilas)

    if puedemoverse is False:
        print('[' + str(posicion.posicionX) + ',' + str(posicion.posicionY) + ']', end='')
        return posicion

    posicion.MoverseHaciaArriba()

    print('[' + str(posicion.posicionX) + ',' + str(posicion.posicionY) + ']', end='')
    MovimientoHaciaArriba(posicion, cantidadFilas)


def MovimientoHaciaAbajo(posicion, cantidadColumnas):

    puedemoverse = posicion.ValidarMovimientoHaciaAbajo(cantidadColumnas)

    if puedemoverse is False:
        print('[' + str(posicion.posicionX) + ',' + str(posicion.posicionY) + ']', end='')
        return posicion

    posicion.MoverseHaciaAbajo()

    print('[' + str(posicion.posicionX) + ',' + str(posicion.posicionY) + ']', end='')
    MovimientoHaciaAbajo(posicion, cantidadColumnas)


filas = 0
columnas = 0

while filas == 0 or filas != columnas:
    print('-- Ingrese valores iguales y diferentes de 0 --')
    filas = int(input('Ingrese el número de filas: '))
    columnas = int(input('Ingrese el número de columnas: '))

posicion_inicial = Posicion(0, 0)

for i in range((filas + filas - 2)):
    if (i % 2) == 0:
        MovimientoHaciaArriba(posicion_inicial, columnas)
    else:
        MovimientoHaciaAbajo(posicion_inicial, filas)
