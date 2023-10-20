base = float(input("Ingrese un número real (base): "))         # Ingrese el usuario la base 
potencia = int(input("Ingrese un número entero (potencia): ")) # Ingrese el usuario la potencia

respuesta = 1             # Inicializa

for i in range(potencia): # Se multiplica x, n veces
    respuesta *= base

print(" El resultado de " + str(base) + " elevado a la " + str(potencia) + " es " + str(respuesta) ) # Imprimir resultado