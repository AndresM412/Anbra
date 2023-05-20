# importa los módulos necesarios
import random
import pygame
import palabras
pygame.init()

# crea la pantalla, fuentes, colores y variables del juego
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
amarillo = (255, 255, 0)
gris = (128, 128, 128)
rojo = (255, 0, 0)
ANCHO = 500
ALTO = 700
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption('Wordle Knockoff')
turno = 0
tablero = [[" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "]]

fps = 60
temporizador = pygame.time.Clock()
fuente_grande = pygame.font.Font('freesansbold.ttf', 56)
palabra_secreta = palabras.PALABRAS[random.randint(0, len(palabras.PALABRAS) - 1)]
print(palabra_secreta)
fin_del_juego = False
letras = 0
turno_activo = True

# crea la función para dibujar el tablero

def dibujar_tablero():
    global turno
    global tablero
    for col in range(0, 5):
        for fila in range(0, 6):
            pygame.draw.rect(pantalla, blanco, [col * 100 + 12, fila * 100 + 12, 75, 75], 3, 5)
            texto_pieza = fuente_grande.render(tablero[fila][col], True, gris)
            pantalla.blit(texto_pieza, (col * 100 + 30, fila * 100 + 25))
    pygame.draw.rect(pantalla, verde, [5, turno * 100 + 5, ANCHO - 10, 90], 3, 5)

# crea la función para verificar las letras

def verificar_palabras():
    global turno
    global tablero
    global palabra_secreta
    for col in range(0, 5):
        for fila in range(0, 6):
            if palabra_secreta[col] == tablero[fila][col] and turno > fila:
                pygame.draw.rect(pantalla, verde, [col * 100 + 12, fila * 100 + 12, 75, 75], 0, 5)
            elif tablero[fila][col] in palabra_secreta and turno > fila:
                pygame.draw.rect(pantalla, amarillo, [col * 100 + 12, fila * 100 + 12, 75, 75], 0, 5)


# configura el ciclo principal del juego

corriendo = True
while corriendo:
    temporizador.tick(fps)
    pantalla.fill(negro)
    verificar_palabras()
    dibujar_tablero()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # añade controles del jugador para ingresar letras, borrar letras, verificar adivinanzas y reiniciar

        if evento.type == pygame.TEXTINPUT and turno_activo and not fin_del_juego:
            entrada = evento.__getattribute__('text')
            if entrada != " ":
                entrada = entrada.lower()
                tablero[turno][letras] = entrada
                letras += 1
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE and letras > 0:
                tablero[turno][letras - 1] = ' '
                letras -= 1
            if evento.key == pygame.K_SPACE and not fin_del_juego:
                turno += 1
                letras = 0
            if evento.key == pygame.K_SPACE and fin_del_juego:
                turno = 0
                letras = 0
                fin_del_juego = False
                palabra_secreta = palabras.PALABRAS[random.randint(0, len(palabras.PALABRAS) - 1)]
                tablero = [[" ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " "]]

        # controla si el turno está activo basado en las letras
        if letras == 5:
            turno_activo = False
        if letras < 5:
            turno_activo = True

        # verifica si la adivinanza es correcta y agrega condiciones de fin del juego

        for fila in range(0, 6):
            adivinanza = tablero[fila][0] + tablero[fila][1] + tablero[fila][2] + tablero[fila][3] + tablero[fila][4]
            if adivinanza == palabra_secreta and fila < turno:
                fin_del_juego = True

        if turno == 6:
            fin_del_juego = True
            texto_perdedor = fuente_grande.render('¡Perdiste!', True, rojo)
            pantalla.blit(texto_perdedor, (40, 610))

        if fin_del_juego and turno < 6:
            texto_ganador = fuente_grande.render('¡Ganaste!', True, verde)
            pantalla.blit(texto_ganador, (40, 610))

    pygame.display.flip()

pygame.quit()
