def obtener_combinaciones(D1, D2, D3, n, combinacion_actual, indice):
    if indice == 3:
        suma = sum(combinacion_actual)
        if suma > n:
            return [combinacion_actual]
        else:
            return []
    
    combinaciones = []
    for i in range(len(D1)):
        nuevo_combinacion_actual = combinacion_actual.copy()
        nuevo_combinacion_actual.append(D1[i])
        nuevas_combinaciones = obtener_combinaciones(D1, D2, D3, n, nuevo_combinacion_actual, indice + 1)
        combinaciones.extend(nuevas_combinaciones)
    
    return combinaciones

D1 = [1, 2, 3, 4, 5, 6]
D2 = [1, 2, 3, 4, 5, 6]
D3 = [1, 2, 3, 4, 5, 6]

n = int(input("Ingrese el valor de n: "))

combinaciones = obtener_combinaciones(D1, D2, D3, n, [], 0)

print("Las combinaciones de suma que superan", n, "son:")
for combinacion in combinaciones:
    print(combinacion)

            