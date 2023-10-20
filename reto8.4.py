def factorial(n):           # Función para calcular el factorial de un número
    fact = 1
    for i in range(1, n+1): # Bucle for con la colección range
        fact *= i           # Multiplica fact por cada número del rango en cada iteración
    return fact             # Retorna el nuevo valor de fact

def imprimir_factorial(n):  # Función que imprime los números desde 1 hasta n, y su factorial 
    for i in range(1, n+1): # Bucle for con la colección range
        print(i, "! =", factorial(i)) # Imprimir resultado

n=int(input("Ingrese el número entero hasta el cual calcula el factorial: ")) # Ingreso del usuario
imprimir_factorial(n)