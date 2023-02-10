import random

def llenar_matriz_aleatoria(filas, columnas):
    return [[random.randint(0, 100) for _ in range(columnas)] for _ in range(filas)]

def imprimir_matriz(matriz):
    print(*(" ".join(map(str, fila)) for fila in matriz), sep="\n")

def sumar_elementos(matriz):
    return sum(sum(fila) for fila in matriz)

mi_matriz = llenar_matriz_aleatoria(3, 4)
imprimir_matriz(mi_matriz)
print(f"\nLa suma es: {sumar_elementos(mi_matriz)}\n")
