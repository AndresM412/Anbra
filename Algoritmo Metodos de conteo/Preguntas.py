import Formulas

class Preguntas:
    Question1 = "¿En su problema importa el orden?"
    Question2 = "¿Intervienen todos los elementos?"
    Question3 = "¿Se repiten los elementos?"
    
    while True:
        entrada = input("Hola, bienvenido para ingresar al algoritmo pulse la tecla Enter, sí desea salir del programa escriba 'Salir'")
        if entrada.lower() in ["", "salir"]:
            break
        else:
            print("Entrada no válida")

    while True:
        answer1 = input(Question1).lower()
        answer2 = input(Question2).lower()
        answer3 = input(Question3).lower()
        
        if answer1 == "si" and answer2 == "si" and answer3 == "si":
            print("Permutaciones con repeticion")
            w = str(input("Ingrese valor de w: "))
            break
            
        elif answer1 == "si" and answer2 == "si" and answer3 == "no":
            print("Permutaciones ordinarias\n")
            m = int(input("Ingrese el valor de m: "))
            Formulas.formulas.permutacion_ordinaria(m)
            break
            
        elif answer1 == "si" and answer2 == "no" and answer3 == "si":
            print("Variaciones con repeticion")
            m = int(input("Ingrese el valor de m: "))
            n = int(input("Ingrese el valor de n: "))
            Formulas.formulas.variacion_repite(m, n)
            break
            
        elif answer1 == "si" and answer2 == "no" and answer3 == "no":
            print("Variaciones Ordinarias")
            m = int(input("Ingrese el valor de m: "))
            n = int(input("Ingrese el valor de n: "))
            Formulas.formulas.variacion_ordinaria(m, n)
            break
            
        elif answer1 == "no" and answer2 == "no" and answer3 == "si":
            print("Combinaciones con repeticion")
            m = int(input("Ingrese el valor de m: "))
            n = int(input("Ingrese el valor de n: "))
            Formulas.formulas.combinacion_repite(m, n)
            break
            
        elif answer1 == "no" and answer2 == "no" and answer3 == "no":
            print("Combinaciones ordinarias")
            m = int(input("Ingrese el valor de m: "))
            n = int(input("Ingrese el valor de n: "))
            Formulas.formulas.combinacion_ordinaria(m, n)
            break
            
        else:
            print("Por favor ingrese una respuesta válida")
        
            
   

    
        



