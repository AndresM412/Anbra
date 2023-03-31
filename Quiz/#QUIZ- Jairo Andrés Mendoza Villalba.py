#QUIZ- Jairo Andrés Mendoza Villalba

# Funcion recursiva que determina el numero mayor de un array de numeros 
l1=[6, 3, 8, -9, 7, -100,100]
def maximo(l1):
  if len(l1) == 0:
    return 0
  elif len(l1) == 1:
    return l1[0]
  else:
    m = maximo(l1[1:])
    if m > l1[0]:
      return m
    else:
      return l1[0]

print("El mayor de la lista l1, es:",maximo(l1))

## Funcion No recursiva que determina el numero mayor de un array de numeros, con notacion Big O

l2=[1,2,3,4,5,6] # 1
def encontrar_mayor(l2):# O(n^2)
    mayor = l2[0] # 1
    for i in range(1, len(l2)):# O(n)
        if l2[i] > mayor: # O(n^2)
            mayor = l2[i] # O(n^2)
    return mayor

print("El mayor de la lista l2, es:",encontrar_mayor(l2))
