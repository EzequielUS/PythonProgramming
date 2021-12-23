"""
Crear un programa que:
La función input() solicita al usuario que ingrese un dato a través de la consola y lo retorna como una cadena. Por ejemplo: 
edad = input("Ingresa tu edad: ") 
print(edad) 

Crear un script que solicite al usuario el código de un país e imprima su nombre, de acuerdo con el siguiente diccionario: 
# Diccionario código: país. 
paises = { "ar": "Argentina", "es": "España", "us": "Estados Unidos", "fr": "Francia" } 
Si el código ingresado no se encuentra en el diccionario, debe imprimir un mensaje en pantalla y volver a preguntar. Si el usuario escribe “salir”, el programa debe terminar.
"""
paises = {
    "ar": "Argentina",
    "es": "España",
    "us": "Estados Unidos",
    "fr": "Francia"
}

while True:
    codigo = input("Ingrese un codigo: ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El código es invalido, vuelve a intentarlo.")

"""
Solicite dos números en consola e imprima el resultado de las cuatro operaciones aritméticas aplicadas sobre ellos. 

Escribe un número: 7 
Escribe otro número: 5 

a + b: 12 
a - b: 2 
a * b: 35 
a / b: 1.4 

---
Tener en cuenta lo siguiente: 
Si el usuario ingresa cualquier otra cosa que no sea un número, debe volver a preguntar, en ambos casos. 
Contemplar que el segundo número puede ser cero y, por ende, llegado el momento de la división el programa debe imprimir “No se puede dividir por cero”. 
Como restricción, no se pueden usar condicionales (if).
"""

def solicitar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            pass
        else:
            break

a = solicitar_numero("Escribe un número: ")
b = solicitar_numero("Escribe otro número: ")

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
try:
    print("a / b:", a / b)
except ZeroDivisionError:
    print("No se puede dividir por cero.")

