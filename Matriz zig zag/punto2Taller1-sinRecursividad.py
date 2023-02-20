posicionX = 0
posicionY = 0

def MovimientoHaciaArriba():
    global posicionX
    global posicionY

    while True:
        if posicionX == 0 and posicionY+1 < columnas:
            posicionY += 1
            return

        if posicionY+1 > columnas - 1:
            posicionX += 1
            return

        posicionX -= 1
        posicionY += 1
        print('[' + str(posicionX) + ',' + str(posicionY) + ']', end='')


def MovimientoHaciaAbajo():
    global posicionX
    global posicionY

    while True:
        if posicionY == 0 and posicionX + 1 < filas:
            posicionX += 1
            return

        if posicionX + 1 > filas - 1:
            posicionY += 1
            return

        posicionX += 1
        posicionY -= 1
        print('[' + str(posicionX) + ',' + str(posicionY) + ']', end='')

filas = int(input('ingrese el número de filas'))
columnas = int(input('ingrese el número de columnas'))



for i in range((filas + filas - 1)):
    step = 1
    print('[' + str(posicionX) + ',' + str(posicionY) + ']', end='')
    if (i % 2) == 0:
        MovimientoHaciaArriba()
    else:
        MovimientoHaciaAbajo()
