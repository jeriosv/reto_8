import math

def aproximacion_seno(x, n):   # Función 
    aprox = 0                  # Inicializa
    for i in range(n):         # Bucle for con la colección range que suma los primeros n términos de la serie de Maclaurin
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)# Calcula el término actual de la serie de Maclaurin y lo suma a aprox
        aprox += term         # Sumamos el término actual a la aproximación acumulada
    real = math.sin(x)
    error = abs(real - aprox) # Calcular el error absoluto entre la aproximación y el valor real 
    porcentaje_error = error / real * 100  # Calcula el porcentaje del error
    
    print(f"Aproximación: {aprox:.6f}")  # Imprimir la aproximación
    print(f"Valor real:   {real:.6f}")    # Imprimir el valor real 
    print(f"Diferencia:   {error:.6f}")   # Imprimir el error 
    print(f"Porcentaje de error: {porcentaje_error:.6f} %")  # Imprimir el porcentaje de error

    if porcentaje_error <= 0.1:   # Si el porcentaje de error es menor o mayor a 0.1%, imprimir
        print (f"El porcentaje de error es menor a 0.1%: es de {porcentaje_error:.6f} %") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: es de {porcentaje_error:.6f} %") 

x = float(input("Ingrese un número real x: ")) # Ingreso del usuario de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin a aproximar: "))  # Ingreso del usario de n términos

aproximacion_seno(x, n) # Llamar a la función