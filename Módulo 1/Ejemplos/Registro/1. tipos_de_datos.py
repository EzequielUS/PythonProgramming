# Entero
numero_1 = int(1)
numero_2 = 2

# Flotante
flotante_1 = float(2)
flotante_2 = 2.0

# Booleano
verdadero = True
falso = False

# String
cadena_1 = "Cadena de texto"
cadena_2 = 'Cadena de texto'
cadena_3 = """Cadena de texto"""

# Complex
complejo_1 = 1 + 4j
complejo_1 = complex(83)

"""
Escribir un programa que pida al usuario un valor entero y muestre por pantalla:
Su valor entero.
Su valor convertido en flotante.
Su valor convertido en booleano.
Su valor convertido en un número complejo.
"""

valor = input("Ingrese un valor entero: ")
print(f"Valor entero: {int(valor)}")
print(f"Valor flotante: {float(valor)}")
print(f"Valor booleano: {bool(valor)}")
print(f"Valor complex: {complex(valor)}")