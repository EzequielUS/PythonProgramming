"""
Con base al siguiente diccionario, filtrar a los alumnos que no sean mayores de edad y almacenarlos en un archivo de texto llamado, alumnos.txt.

diccionario = {“Javier”: 21, “Pablo”: 17, “Raul”: 17, “Esteban”: 16, “Milagros”: 19, “Santiago”: 20}
"""

diccionario = {"Javier": 21, "Pablo": 17, "Raul": 17, "Esteban": 16, "Milagros": 19, "Santiago": 20}

for nombre in diccionario:
    edad = diccionario[nombre]

    if  0 < edad <= 17: # Interval Comparison
        archivo = open("alumnos.txt", "a")
        archivo.write(f"{nombre}\n")
        archivo.write(f"{edad}\n")
        archivo.close

"""
Con base al archivo que acabamos de crear se nos pide que lo leamos y almacenemos el contenido en un diccionario con el mismo formato que utilizamos para crear “alumnos.txt”.
"""

diccionario = {}
nombres = []
edad = []

archivo = open("alumnos.txt", "r")

for line in archivo:
    line = line.replace("\n", "")

    if not line.isdecimal() and line != "":
        nombres.append(line)
    else:
        edad.append(line)

archivo.close()

for indice, nombre in enumerate(nombres):
    diccionario[nombre] = edad[indice]

print(diccionario)


"""
Crear un sistema para loggear información.

Se debera crear un menu que me permita realizar las siguientes operaciones:
1. Añadir información al LOG
2. Leer información del LOG
3. Consultar fecha
4. Salir

El LOG debe ser diario, por lo que su nombre se debe armar con la fecha del dia.
fecha = datetime.now()
fecha = fecha.strftime("%d-%m-%Y")
"""
from datetime import datetime

def menu():
    print("1. Añadir información al log")
    print("2. Leer información del log")
    print("3. Consultar fecha")
    print("4. Salir")

    opcion = int(input("Opcion: "))
    return opcion

while True:
    fecha = datetime.now()
    fecha = fecha.strftime("%d-%m-%Y")
    
    opcion = menu()

    if opcion == 1:
        archivo_log = open(fecha, "a")
        mensaje = input("Ingrese un mensaje: ")
        archivo_log.write(mensaje + "\n")
        archivo_log.close()

    elif opcion == 2:     
        archivo_log = open(fecha, "r")
        mensaje = archivo_log.read()
        archivo_log.close()
        print(mensaje)

    elif opcion == 3:
        print(fecha)

    elif opcion == 4:
        break