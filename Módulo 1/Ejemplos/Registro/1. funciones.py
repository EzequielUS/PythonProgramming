# Ejercicio 1
"""Crear una función rango(al estilo “range”) que reciba inicio, final e incremento como argumento. Que imprima en pantalla una lista con los parámetros pasados. La idea es resolver el algoritmo de esta función sin usar la función range incorporada del lenguaje."""  

def rango(inicio, final, incremento):
    contador = inicio
    while contador < final:
        print(contador)
        contador = contador + incremento
    
    return [inicio, final, incremento]

print(rango(1,10,3))

# Ejercicio 2
"""Crear las funciones max(), min() , las cuales reciban una lista o tupla de valores enteros como argumento  y devuelvan el valor mas alto y más bajo de dicha estructura. La idea es resolver el algoritmo de esta función sin usar las funciones max() y min()  incorporadas del lenguaje."""
def max(coleccion):
    maximo = coleccion[0]
    for elemento in coleccion:
        if elemento > maximo:
            maximo = elemento    
    return maximo

def min(coleccion):
    minimo = coleccion[0]
    for elemento in coleccion:
        if elemento < minimo:
            minimo = elemento    
    return minimo

print(max((1,5,9,4,6)))
print(min((1,5,9,4,6)))


# Ejercicio 3
"""Crear la funcion sum(), min() , las cuales reciban una lista o tupla de valores enteros como argumento  y devuelvan la suma de los valores pertenecientes a dicha estructura. La idea es resolver el algoritmo de esta función sin usar la función sum() incorporada del lenguaje."""
def suma(coleccion):
    acumulador = 0
    for elemento in coleccion:
        acumulador = acumulador + elemento
    return acumulador

print(suma((1,5,9,4,6)))


# Ejercicio 4
"""Crear una función que me permita obtener las raíces de un polinomio de grado 2. 
Resultados esperados:  raices(1, 1, -6) ->  (2.0, -3.0)"""

from math import sqrt
def f(a, b, c):
    resultado_raiz = sqrt(b*b - 4*a*c)
    r1 = (-b + resultado_raiz) / 2*a
    r2 = (-b - resultado_raiz) / 2*a
    return (r1, r2)

# Ejercicio 5
"""Escribir un programa que cree un diccionario vacío y lo vaya llenando con personas. Donde el nombre(str) será la clave(el key) y el valor(value) la edad(int). El programa debe estar acompañado de un menú: 
Menú: 
A) Agregar. 
B) Mostrar el más chico. 
C) Mostrar el más grande. 
D) Salir. 

La opción de agregar inserta a una persona. Mostrar el más chico, nos debería mostrar el nombre de la persona más chica, y viceversa el de mostrar el más grande. Con la opción 4 deberíamos salir del programa."""

def menu():
    print("Menú:")
    print("A) Agregar.") 
    print("B) Mostrar el más chico. ") 
    print("C) Mostrar el más grande. ") 
    print("D) Salir.") 

def verificar(texto):
    while texto == "":
        print("Error")
        texto = input("Ingrese nuevamente: ")
    return texto

def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)

def agregar_persona():
    nombre = input("Ingrese un nombre: ")
    nombre = verificar(nombre)
    edad = input("Ingrese una edad: ")
    edad = convertir(edad)
    personas[nombre] = edad
    print("¡Se agrego una persona!")

def mostrar_mas_chico():
    # El 'truco' consiste en poner el 200 para que arranque aux_edad con un número grande y siempre tome el primero del diccionario.
    aux_edad = 200 
    aux_nombre = ""
    for n in personas:
        if personas[n] < aux_edad:
            aux_edad = personas[n]
            aux_nombre = n
    print(aux_nombre + " es la persona más chica")

def mostrar_mas_grande():
    # El 'truco' consiste en poner el 0 para que arranque aux_edad con cero y siempre tome el primero del diccionario.
    aux_edad = 0
    # aux_nombre la dejamos vacio
    aux_nombre = ""
    for n in personas:
        if personas[n] > aux_edad:
            aux_edad = personas[n]
            aux_nombre = n
    print(aux_nombre +" es la persona más grande")
################################

personas = {}

while True:
    opcion = menu()

    if opcion == "1":
        agregar_persona()
    elif opcion == "2":
        mostrar_mas_chico()
    elif opcion == "3":
        mostrar_mas_grande()
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("¡Error de opción!")