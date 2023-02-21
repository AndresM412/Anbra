class Posicion:
    def __init__(self, posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY

    def ValidarMovimientoHaciaArriba(self,cantidadFilas):
        if self.posicionX == 0 and self.posicionY + 1 < cantidadFilas:
            self.posicionY += 1
            return False

        if self.posicionY + 1 > cantidadFilas - 1:
            self.posicionX += 1
            return False

    def ValidarMovimientoHaciaAbajo(self,cantidadColumnas):
        if self.posicionY == 0 and self.posicionX + 1 < cantidadColumnas:
            self.posicionX += 1
            return False

        if self.posicionX + 1 > cantidadColumnas - 1:
            self.posicionY += 1
            return False

    def MoverseHaciaArriba(self):
        self.posicionX -= 1
        self.posicionY += 1

    def MoverseHaciaAbajo(self):
        self.posicionX += 1
        self.posicionY -= 1