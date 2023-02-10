import random

def llenar_matriz_aleatoria(filas, columnas):
    return [[random.randint(0, 100) for j in range(columnas)] for i in range(filas)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elem) for elem in fila))

def sumar_elementos(matriz):
    return sum(sum(fila) for fila in matriz)

mi_matriz = llenar_matriz_aleatoria(3, 4)
imprimir_matriz(mi_matriz)
print("\n")
resultado = sumar_elementos(mi_matriz)
print(f"La suma es: {resultado}")
print("\n")
print(mi_matriz)