from math import factorial
class formulas:
    
    m=input(int("Ingrese el valor de m"))
    n=input(int("Ingrese el valro de n"))
    
    #------------------COMBINACIONES--------------------------------------------
    def combinacion_repite(m,n):
        resultado =  factorial((m + n-1)) / factorial(n)*factorial((m-1))
        print(f"El resultado es {resultado}")
    
    def combinacion_ordinaria(m,n):
        resultado = factorial(m)/factorial(n)*factorial(m-n)
        print(f"El resultado es {resultado}")
    
    #------------------COMBINACIONES--------------------------------------------

    #------------------VARIACIONES----------------------------------------------
    
    def variacion_repite(m,n):
        resultado= m**n
        print(f"El resultado es {resultado}")
    
    def variacion_ordinaria(m,n):
        resultado= factorial(m)/factorial(m-n)
        print(f"El resultado es {resultado}")
        
    #------------------VARIACIONES----------------------------------------------
    
    #-----------------PERMUTACIONES----------------------------------------------
    def permutacion_repite(m,n):
        
        
    def permutacion_ordinaria(m,n):
        resultado= factorial(m)
        print(f"El resultado es {resultado}")