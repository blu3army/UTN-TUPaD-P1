import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Spy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return round(radio**2 * math.pi, 2)

def calcular_perimetro_circulo(radio):
    return round(radio * 2 * math.pi, 2)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.
def segundos_a_horas(segundos):
    return round(segundos / 60 / 60, 2)


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero}x{i} = {numero*i}")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.
def operaciones_basicas(a,b):
    return ( (a+b), (a-b), (a*b), round((a/b), 2) )

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return round(peso / (altura**2), 2)



# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Main 

imprimir_hola_mundo()

saludar_usuario("Nikolai")

informacion_personal("Leonel", "Messi", 37, "Miami")

print(f"El area del circulo es: {calcular_area_circulo(10)}")
print(f"El perimetro del circulo es {calcular_perimetro_circulo(10)}")

print(f"Son {segundos_a_horas(44500)} horas")

tabla_multiplicar(5)

print(f"Operaciones básicas {operaciones_basicas(10 , 45)}")

print(f"Su IMC es {calcular_imc(90, 180)}")

print(f"Son {celsius_a_fahrenheit(25)} grados farenheit")

print(f"El promedio es {calcular_promedio(10, 20, 15)}")