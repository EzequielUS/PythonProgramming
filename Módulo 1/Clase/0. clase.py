variable_entera = int(10)
print(type(variable_entera))

variable_flotante = float(10.1)
print(type(variable_flotante))

variable_booleana = bool(True)
print(type(variable_booleana))

variable_cadena = str("Tipo de dato cadena")
print(type(variable_cadena))

variable_nula = None
print(type(variable_nula))

variable_compleja = complex(10 + 8j)

# Ejercicio 1
ingreso = input("Ingrese un valor entero: ")

print(int(ingreso))
print(float(ingreso))
print(bool(ingreso))
print(complex(ingreso))

# Ejercicio 2
"""
Escribir un programa que pida al usuario dos números enteros y con ellos:
    - Imprimir en pantalla el resultado de sumar ambos valores
    - Imprimir en pantalla el resultado de restar ambos valores
    - Imprimir en pantalla el resultado de dividir ambos valores
    - Imprimir en pantalla el resultado de multiplicar ambos valores
    - Imprimir en pantalla el resultado de elevar cada valor a la potencia del otro
    - Imprimir en pantalla el resultado de la división entera entre ambos valores
"""

variable_0 = input("Ingresar un entero")
variable_1 = input("Ingresar otro entero")

print("Suma", int(variable_0) + int(variable_1))

print(f"Suma {int(variable_0) + int(variable_1)}")

print(f"Resta {int(variable_0) - int(variable_1)}")

# Estructuras complejas
listas = [1, "Ezequiel", True, int()]
listas[0] = 2
listas[1] = "Matias"
listas[2] = False

tuplas = (1, "Ezequiel", True, int())
elemento = tuplas[0]

diccionarios = {
    'valor': 1,
    'valor_2': 2,
}