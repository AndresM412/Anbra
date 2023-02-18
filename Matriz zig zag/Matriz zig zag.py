filas = int(input('ingrese el número de filas'))# 1
columnas = int(input('ingrese el número de columnas')) # 1
for col in range(columnas): # O(n)
    start = 0 # n
    step = 1 # n
    stop = filas # n
    if (col % 2) != 0: # O(n^2)
        start = filas-1 # n^2
        step = -1 # n^2
        stop = -1 # n^2
    for i in range(start, stop, step): #O(n^2)
        print('[' + str(i) + ',' + str(col) + ']', end='') #O(n^2)
    print()