posicionX = 0
posicionY = 0

def Movimiento(x,y,end):
    print('[' + str(x) + ',' + str(y) + ']', end='')
    if x == 0 and y+1 < end:
        y += 1
        return

    if y+1 > end - 1:
        x += 1
        return

    x -= 1
    y += 1
    print('[' + str(x) + ',' + str(y) + ']', end='')
    Movimiento(x,y)


filas = int(input('ingrese el número de filas'))
columnas = int(input('ingrese el número de columnas'))



for i in range((filas + filas - 2)):
    if (i % 2) == 0:
        Movimiento(posicionX,posicionY,columnas)
    else:
        Movimiento(posicionY,posicionX,filas)
