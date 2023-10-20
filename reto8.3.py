n=int(input("Ingrese un número entero (mayor o igual que 2): "))  # Ingreso del usuario
def pares_hasta_n(n):         # Definir unas función para ir hasta n 
    pares = []                # Crear lista vacia 
    for i in range(1,n+1):    # Bucle for con la colección range
        if i % 2 == 0:        # Si el resíduo es igual a cero es par, se inserta a la lista 
            pares.insert(0,i) # Inserta a la lista vacía el número par i. La posición en la que se inserta el elemento es el índice 0, al principio de la lista.
    return pares 
print("Los números pares decrecientes de " + str(n) + " hasta 2 son: "+ str(pares_hasta_n(n)))  # Imprimir resultado