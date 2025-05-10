import random

# Aquí trabajaremos en el TP 04
# Ejercicio 1

for i in range(0, 11):
    print(i)

# ejercicio 2
num = int(input("Ingrese un número: "))
dig = 0
while num > 0:
    num = int(num / 10)
    dig += 1

print("La cantidad de dígitos es: ", dig)

# ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num_a = min(num1, num2)
num_b = max(num1, num2)
suma = 0

for i in range(num_a + 1, num_b):
    suma += i

print(suma)

# ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
num = 0
suma = 0
while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num != 0:
        suma += num
    else:
        print("La suma total es: ", suma)
        break


# ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

secret_num = random.randint(0, 9)
intentos = 0

while True:
    num = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if num == secret_num:
        print("Acertaste el número en", intentos, "intentos...")
        break

# ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)


# ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

while True:
    num = int(input("Ingrese un número entero positivo: "))
    if num > 0:
        
        suma = 0
        for i in range(0, num + 1):
            suma += i

        print("La suma de los números entre 0 y", num, "es:", suma)
        break
    else:
        print("El número debe ser positivo.")


# ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0
cantidad = 10

for i in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)


# ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)

sumatoria = 0
cantidad = 10
for i in range(cantidad):
    num = int(input("Ingrese un número: "))
    sumatoria += num

print("La media de los números ingresados es:", sumatoria / cantidad)

# ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
inverso = ""
while num > 0:
    digito = num % 10
    inverso += str(digito)
    num = int(num / 10)

print("El número invertido es:", inverso)