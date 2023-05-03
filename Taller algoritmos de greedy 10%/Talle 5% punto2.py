def min_suma_diferencias(a, b):
    # Ordenar ambos arreglos en orden ascendente
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    # Inicializar la suma de las diferencias en 0
    suma_diferencias = 0

    # Emparejar los elementos correspondientes de ambos arreglos
    for i in range(len(a)):
        suma_diferencias += abs(a_sorted[i] - b_sorted[i])

    # Devolver la suma de las diferencias absolutas
    return suma_diferencias


a = [4,1,2]
b = [2,4,1]

# Llamamos a la función y guardamos el resultado en una variable
min_suma = min_suma_diferencias(a, b)

# Imprimimos el resultado
print("La mínima suma de diferencias es:", min_suma)
