# Reto No. 8 : Bucles 2.
# "Repito y repita se fueron a nadar repito se ahogó y ¿quién quedó?": acertijo infantil.

Colecciones de rango y cliclos for.
Para cada punto cree un programa individual asimismo cree un notebook con la solución a todos los problemas. 
Nota: Todo el código de aquí en adelante debe ir debidamente documentado.

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
  range(1,101)            # Coleccion Rango con intervalo de 0 hasta 101
  for i in range(1,101):  # Bucle for con la colección range
    print("El número " + str(i) + " elevado al cuadrado es " + str(i**2)) # Imprimir resultados
```

2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
Pares=[]                # Crear una lista vacia para los números pares
Impares=[]              # Crear una lista vacia para los números impares
for i in range(1,1001): # Bucle for con la colección range
    if i%2==0:          # Si el resíduo de la división es cero es par
        Pares.append(i) # Agregar el número par a la lista
    else:               # Sino, es impar
        Impares.append(i) # Agregar el número impar a la lista
print("Los números pares desde 0 hasta 1000 son: " + str(Pares))        # Imprimir pares 
print("\nLos números impares desde 0 hasta 1000 son: " + str(Impares))  # Imprimir impares 
```

3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
n=int(input("Ingrese un número entero (mayor o igual que 2): "))  # Ingreso del usuario
def pares_hasta_n(n):         # Definir unas función para ir hasta n 
    pares = []                # Crear lista vacia 
    for i in range(1,n+1):    # Bucle for con la colección range
        if i % 2 == 0:        # Si el resíduo es igual a cero es par, se inserta a la lista 
            pares.insert(0,i) # Inserta a la lista vacía el número par i. La posición en la que se inserta el elemento es el índice 0, al principio de la lista.
    return pares 
print("Los números pares decrecientes de " + str(n) + " hasta 2 son: "+ str(pares_hasta_n(n)))  # Imprimir resultado
```

4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

```python
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
```

5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
n = int(input("Introduce un número entero (la potencia para 2): ")) # Ingreso del usuario
respuesta = 1      # Inicializa

for i in range(n): # Bucle for con la colección range
    respuesta *= 2 # En cada iteración, multiplicamos respuesta por 2 y lo asignamos a respuesta

print(" 2 elevado a la " + str(n)+ " es igual a " + str(respuesta)) # Imprimir resultado
```

6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

```python
base = float(input("Ingrese un número real (base): "))         # Ingrese el usuario la base 
potencia = int(input("Ingrese un número entero (potencia): ")) # Ingrese el usuario la potencia

respuesta = 1             # Inicializa

for i in range(potencia): # Se multiplica x, n veces
    respuesta *= base

print(" El resultado de " + str(base) + " elevado a la " + str(potencia) + " es " + str(respuesta) ) # Imprimir resultado
```

7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```python
for i in range(1, 10):     # Bucle for con la colección range del 1 al 9
    print(f"\nLa Tabla del {i} :") 
    for j in range(1, 11): # Bucle for con la colección range del 1 al 10
        print(f"{i} x {j} = {i*j}") # Imprimir resultado
```

8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

![image](https://github.com/jeriosv/reto_8/assets/142249529/1b7416ab-77e1-4c90-bb33-304acb058a50)


```python
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
```

9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

![image](https://github.com/jeriosv/reto_8/assets/142249529/7c1f1675-3930-45ec-a0c9-b0077c389232)


```python
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
    print(f"Porcentaje de error: {porcentaje_error:.6f} %")  # Imprime la diferencia entre ambos

    if porcentaje_error <= 0.1:   # Si el porcentaje de error es menor o mayor a 0.1%, imprimir
        print (f"El porcentaje de error es menor a 0.1%: es de {porcentaje_error:.6f} %") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: es de {porcentaje_error:.6f} %") 

x = float(input("Ingrese un número real x: ")) # Ingreso del usuario de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin a aproximar: "))  # Ingreso del usario de n términos

aproximacion_seno(x, n) # Llamar a la función
```

10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

![image](https://github.com/jeriosv/reto_8/assets/142249529/a338c70e-b117-4f29-9498-1e2a94706400)
 
Disclaimer: Para las aproximaciones de series determine con que valor n se obtiene menos del 0.1% de error.

```python
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
```
