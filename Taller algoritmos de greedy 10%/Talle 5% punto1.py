def min_operaciones(N):
    cola = [(0, 0)]  

    while cola:
        estado, num_operaciones = cola.pop(0)

        if estado == N:
            return num_operaciones
        
        cola.append((estado + 1, num_operaciones + 1))
        cola.append((estado * 2, num_operaciones + 1))

    return -1

N = 5
min_op = min_operaciones(N)
print(f"El numero minimo de operaciones para llegar a {N} es {min_op}")
