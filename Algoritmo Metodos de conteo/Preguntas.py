class Preguntas:
    Question1= "¿En su problema importa el orden?"
    Question2= "¿Intervienen todos los elementos?"
    Question3= "¿Se repiten los elementos?"
    while True:
        entrada = input("Hola bienvenido para ingresar al algoritmo pulse la tecla Enter, sí desea salir del programa escriba 'Salir'")
        if entrada == "":
            break
        elif entrada.lower() == "salir":
            break
        else:
            print("Entrada no válida")
    
    while True:
        answer=input(Question1)
        if answer.lower()=="si":
            answer=input(Question2)
            if answer.lower()=="si":
                answer=input(Question3)
                if answer.lower()=="si":
                   print("Permutaciones con repeticion")
                   break
                elif answer.lower()=="ni":
                    print("Permutaciones ordinarias")
                    break
                else:
                    print("Por favor ingrese una respuesta")
            elif answer.lower()=="no":
                answer=input(Question3)
                if answer.lower()=="si":
                    print("Variaciones con repeticion")
                    break
                elif answer.lower()=="no":
                    print("Variaciones Ordinarias")
                    break
                else:
                    print("Por favor ingrese una respuesta")
            else:
                print("Por favor ingrese una respuesta")
        elif answer.lower()=="no":
            answer=input(Question2)
            if answer.lower()=="no":
                answer=input(Question3)
                if answer.lower()== "si":
                    print("Combinaciones con repeticion")
                    break
                elif answer.lower()== "no":
                    print("Combinaciones ordinarias")
                    break
                else:
                    print("Por favor ingrese una respuesta")
            else:
                print("Por favor ingrese una respuesta")
        else:
            print("Por favor ingrese una respuesta")
        
            
   

    
        



