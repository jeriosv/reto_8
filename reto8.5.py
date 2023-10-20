n = int(input("Introduce un número entero (la potencia para 2): ")) # Ingreso del usuario
respuesta = 1      # Inicializa

for i in range(n): # Bucle for con la colección range
    respuesta *= 2 # En cada iteración, multiplicamos respuesta por 2 y lo asignamos a respuesta

print(" 2 elevado a la " + str(n)+ " es igual a " + str(respuesta)) # Imprimir resultado