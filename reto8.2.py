Pares=[]                # Crear una lista vacia para los números pares
Impares=[]              # Crear una lista vacia para los números impares
for i in range(1,1001): # Bucle for con la colección range
    if i%2==0:          # Si el resíduo de la división es cero es par
        Pares.append(i) # Agregar el número par a la lista
    else:               # Sino, es impar
        Impares.append(i) # Agregar el número impar a la lista
print("Los números pares desde 0 hasta 1000 son: " + str(Pares))        # Imprimir pares 
print("\nLos números impares desde 0 hasta 1000 son: " + str(Impares))  # Imprimir impares 