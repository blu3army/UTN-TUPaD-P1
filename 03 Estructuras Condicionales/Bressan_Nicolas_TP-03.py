from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Escriba su edad "))
if edad >= 18:
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota = int(input("Cual fue la nota? "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un número "))
if numero % 2 == 0:
    print("Ha ingresado un número par ")
else:
    print("Por favor, ingrese un número par")




# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años
edad = int(input("Escriba su edad "))
if edad < 12:
    print("Es un niño/a")
elif edad >= 12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 30:
    print("Es un adulto/a joven")
else:
    print("Es un adulto/a")



# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.


password = input("Ingrese su contraseña: ")
pass_length = len(password)

if pass_length >= 8 and pass_length <= 14:
    print("Ha ingresado una constraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.
numeros_aletorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aletorios)
mediana = median(numeros_aletorios)
media = mean(numeros_aletorios)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
frase = input("Escribir frase o palabra: ")

if frase[-1] in ['a', 'e', 'i', 'o', 'u']:  
    print(frase[:-1] + "!")
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
print("Ingrese una opción: ")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")
opcion = int(input(""))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
else:
    print(nombre.title())



# 9)
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10)

hemisferio = input("Ingrese su hemisferio N o S ").lower()
mes = input("Ingrese el mes ").lower()
dia = int(input("Ingrese día "))

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

mes_index = meses.index(mes)

if mes in meses:

    if (mes_index == 11 and dia >= 21) or (mes_index >= 0 and mes_index <= 1) or (mes_index == 2 and dia <= 20):
       
        print("Verano") if hemisferio == "s" else print("Invierno")

    elif (mes_index == 2 and dia >= 21) or (mes_index >= 3 and mes_index <= 4) or (mes_index == 5 and dia <= 20):

        print("Otoño") if hemisferio == "s" else print("Primavera")

    elif (mes_index == 5 and dia >= 21) or (mes_index >= 6 and mes_index <= 7) or (mes_index == 8 and dia <= 20):
        
        print("Invierno") if hemisferio == "s" else print("Verano")
    
    else:

        print("Primavera") if hemisferio == "s" else print("Otoño")


else:
    print("El mes que ingresó no existe")