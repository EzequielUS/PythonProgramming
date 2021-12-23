"""
Crear un programa que:
En matemática, se conoce a la “sucesión de Fibonacci” como una sucesión infinita de números naturales en la que cada término está determinado por la suma de los dos términos anteriores. Por ejemplo, empezando con el 0 y el 1, los primeros 20 términos son los siguientes:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181 

Crear una función en Python que tome como argumento un entero que indique la cantidad de términos (verificarlo) y retorne una lista como la anterior. 
Por ejemplo: 
>>> fib(10) 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

La función debe, además, chequear que el argumento pasado sea mayor a 2. En caso de ser menor, debe mostrar un mensaje en pantalla y no retornar nada. >>> fib(1) La cantidad debe ser mayor a 2.
"""
def fib(cantidad):
    if cantidad < 2:
        print("Cantidad ingresada incorrecta")
        return None

    fibonacci = [0, 1]

    while len(fibonacci) < cantidad:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    return fibonacci


lista = fib(2)
print(f"Fibonacci de 2: {lista}")

lista = fib(5)
print(f"Fibonacci de 5: {lista}")

lista = fib(10)
print(f"Fibonacci de 10: {lista}")

"""
Crear un programa que:

Contenga una función que se llame “promedio_variable”. 
Esta función debe tomar un número arbitrario de argumentos numéricos y devolver el promedio.
"""
# Si se desea para hacer la suma se puede usar la funcion built-in sum() 
# de esa manera evitas el uso del for 

def promedio_variable(*args):
    suma = 0
    for n in args:
        suma += n
    promedio = suma / len(args)
    return promedio


#############################
print(promedio_variable(10,8,9))
print(promedio_variable(6,6,9,9))

"""
Construir una función que debe tomar una cantidad arbitraria de argumentos posicionales (*args) los cuales deben ser nombres de personas, además la función debe tener un keyword argument (argumento por defecto) llamado grupo.

Por defecto grupo = 2. 

Nuestra función debe devolver una lista, con listas en su interior con 2 nombres por cada una, si grupo queda por defecto. 
Si el argumento “grupo” recibe un valor, debemos asegurarnos de que sea mayor que 2, si no lo es, forzar para que el valor quede en 2.  Crearemos los grupos según el número pasado por argumento a “grupo”. 

Por ejemplo: 
equipo("Juan","Tamara","Lautaro","Gabriel" "Agustin","Susana",grupo=3) 
>>> [['Juan', 'Tamara', 'Lautaro'], ['Gabriel', 'Agustín', 'Susana']]

Si no se pasa el valor de grupo o se pasa un valor menor a 2: 
[['Juan', 'Tamara'], ['Lautaro', 'Gabriel'], ['Agustín', 'Susana']] 

Y si se pasa un número no múltiplo, los participantes que sobran formarán el último grupo. Como a continuación:
grupo = 4 
[['Juan', 'Tamara', 'Lautaro', 'Gabriel'], ['Agustín', 'Susana']]
"""

def equipo(*participantes,grupo=2):
    equipos = []

    if grupo < 2:
        grupo = 2

    for n in range(grupo,len(participantes)+1,grupo):
        equipos.append(list(participantes[n-grupo:n]))

    if n < len(participantes):
        equipos.append(list(participantes[n:]))

    print(equipos)

equipo("Juan","Tamara","Lautaro","Gabriel","Agustin","Susana",grupo=4)

"""
Crear las funciones max() y min() , las cuales reciban una lista o tupla de valores enteros como argumento  y devuelven el valor más alto y más bajo de dicha estructura. La idea es resolver el algoritmo de esta función sin usar las funciones max() y min()  incorporadas del lenguaje. 
"""
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


"""
Crear la función sum(), la cual reciba una lista o tupla de valores enteros como argumento  y devuelva la suma de los valores pertenecientes a dicha estructura. La idea es resolver el algoritmo de esta función sin usar la función sum() incorporada del lenguaje. 
"""
def suma(coleccion):
    acumulador = 0
    for elemento in coleccion:
        acumulador = acumulador + elemento
    return acumulador

print(suma((1,5,9,4,6)))

"""
Crear una función que me permita obtener las raíces de un polinomio de grado 2. 
Resultados esperados:  raices(1, 1, -6) ->  (2.0, -3.0)
"""
from math import sqrt
def f(a, b, c):
    resultado_raiz = sqrt(b*b - 4*a*c)
    r1 = (-b + resultado_raiz) / 2*a
    r2 = (-b - resultado_raiz) / 2*a
    return (r1, r2)

"""
Escribir un programa que cree un diccionario vacío y lo vaya llenando con personas. Donde el nombre(str) será la clave(el key) y el valor(value) la edad(int). El programa debe estar acompañado de un menú: 

Menú: 
A) Agregar. 
B) Mostrar el más chico. 
C) Mostrar el más grande. 
D) Salir. 

La opción de agregar inserta a una persona. Mostrar el más chico, nos debería mostrar el nombre de la persona más chica, y viceversa el de mostrar el más grande. Con la opción 4 deberíamos salir del programa.
"""

def menu():
    print("Menú:")
    print("A) Agregar.") 
    print("B) Mostrar el más chico. ") 
    print("C) Mostrar el más grande. ") 
    print("D) Salir.") 

    opcion = input("Opcion: ")
    return opcion
    
def verificar(texto):
    while texto == "":
        print("Error")
        texto = input("Ingrese nuevamente: ")
    return texto

def convertir(dato):
    while not dato.isdecimal():
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