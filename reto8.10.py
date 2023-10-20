import math

def aproximacion_arctan(x, n): # Definir la función
    if x < -1 or x > 1: # Asegurarse que el valor de x está en el rango [-1, 1]
        print("Error: el valor de x debe estar en el rango [-1, 1].")
        return

    aprox = 0         # Inicializa 
    for i in range(n): # Bucle for con la colección range que suma los primeros n términos de la serie de Maclaurin
        term = ((-1)**i * x**(2*i + 1)) / (2*i + 1) # Calcula cada término de la serie de Maclaurin 
        aprox += term # Suma el término actual a la aproximación acumulada

    real = math.atan(x)            # Calcula el valor real
    error = abs(real - aprox)      # Calcula el error absoluto entre la aproximación y el valor real 
    porcentaje_error = error / real * 100 # Calcula el porcentaje de error

    print(f"Aproximación: {aprox:.6f}")       # Imprimir la aproximación
    print(f"Valor real:   {real:.6f}")        # Imprimir el valor real
    print(f"Diferencia:   {error:.6f}")       # Imprimir el error absoluto
    print(f"Porcentaje de error: {porcentaje_error:.2f} %")  # Imprimir el porcentaje de error

    if porcentaje_error <= 0.1:   # Si el porcentaje de error es menor o mayor a 0.1%, imprimir
        print (f"El porcentaje de error es menor a 0.1%: es de {porcentaje_error:.6f} %") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: es de {porcentaje_error:.6f} %") 

x = float(input("Ingrese un número real x: ")) # Ingreso del usuario de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin a aproximar: "))  # Ingreso del usario de n términos

aproximacion_arctan(x, n) # Llamar a la función 