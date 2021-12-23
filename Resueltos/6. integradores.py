"""
Hacer una función de orden superior que reciba como argumento una frase y una función lambda. Este
conjunto debe detectar si existe alguna palabra capicúa (palíndromo) en el texto pasado. Si existe,
debe almacenar, y luego devolver una lista con las coincidencias.
"""

def aplicar(funcion,frase):
    palabras = frase.split()
    seleccionadas = []
    for n in palabras:
        if funcion(n):
            seleccionadas.append(n)
    return seleccionadas



####################################################

texto = """
Juan tenia su ojo en el radar, cuando de repente vio desde el helicoptero las minas 
de oro abandonadas al costado del rio. 
Se habian desviado, Neuquen quedaba en direccion opuesta. Ya no habia tiempo, el reloj
marcaba la una en punto.
"""

print(aplicar(lambda x: x.lower() ==x[::-1].lower(),texto))

"""
Hacer un programa con un menú muy sencillo:
Menú:
    1. Ingreso de empleado
    2. Egreso de empleado
    3. Salir del sistema


Este sistema es básico, lo utiliza el personal de seguridad que registra el nombre de la persona
que ingresa (opción 1), y que egresa del edificio (opción 2). 
Además, es necesario registrar el horario de los eventos se podría usar el módulo time, y la función asctime() que devuelve un
str con fecha y hora.

Cuando se quiere salir del programa se usa laopción 3.

Tanto el ingreso y el egreso se registra en un archivo txt. Cada renglón representa un registro.
"""

import time

def comprobar(dato):
    while dato == "":
        print("Error. ¡No debe dejar vacio este campo!")
        dato = input("Ingrese dato nuevamente: ")
    return dato

def guardar(persona,tipo):
    fecha = time.asctime()
    datos = f"{fecha} - {persona} - {tipo} \n"
    f = open("registro.txt","a")
    f.write(datos)
    f.close()
    

while True:
    print("""
    Menú
    1 - Ingreso de empleado
    2 - Egreso de empleado
    3 - Salir del sistema
    """)
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Nombre del empleado que ingresa: ")
        nombre = comprobar(nombre)
        guardar(nombre,"Ingreso")
    elif opcion == "2":
        nombre = input("Nombre del empleado que egresa: ")
        nombre = comprobar(nombre)
        guardar(nombre,"Egreso")
    elif opcion == "3":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("Error de opcion")
    print("\n\n")
    input("Toque ENTER para continuar...")