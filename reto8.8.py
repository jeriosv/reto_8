import math 

def aproximacion_exp(x, n):
    aprox = 0.0        # Inicializa 
    for i in range(n):  # Bucle for con la colección range que suma los primeros n términos de la serie de Maclaurin
        aprox += x**i / math.factorial(i) # Calcula el término actual de la serie de Maclaurin y lo suma a aprox
    real = math.exp(x)                    # Calcula el valor real de la función exponencial en x
    error = abs(real - aprox)             # Calcula el error absoluto entre la aproximación y el valor real
    porcentaje_error = error / real * 100 # Calcula el porcentaje del error

    print(f"Aproximación: {aprox:.6f}") # Imprime la aproximación
    print(f"Valor real:   {real:.6f}")    # Imprime el valor real 
    print(f"Diferencia:   {error:.6f}")   # Imprime la diferencia entre ambos
    print(f"Porcentaje de error: {porcentaje_error:.2f} %")  # Imprime el porcentaje del error

    if porcentaje_error <= 0.1:   # Si el porcentaje de error es menor o mayor a 0.1%, imprimir
        print (f"El porcentaje de error es menor a 0.1%: es de {porcentaje_error:.2f} %") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: es de {porcentaje_error:.2f} %") 

x = float(input("Ingrese un número real x: ")) # Ingreso del usuario de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin a aproximar: "))  # Ingreso del usario de n términos

aproximacion_exp(x, n) # Llamar a la función 