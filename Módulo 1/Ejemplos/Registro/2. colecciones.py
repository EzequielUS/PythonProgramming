# Listas
nombres = ["Pablo", "Tomas", "Ricardo"]
nombres.insert(2, "Mailen")
nombres.append("Sarah")

contador = 0
while contador != len(nombres):
    print(f"Nombre: {nombres[contador]}")
    contador += 1

# Tuplas

# Pedir a un usuario que ingrese manualmente un valor entero positivo, y obtener los divisores de dicho valor hasta el 1, 
# los mismos se almacenarán en una tupla (concatenarlos). Al finalizar se debe preguntar si alguno de los siguientes valores se encuentran 
# contenidos dentro de la tupla.

valores_posibles = [2, 3, 5, 7, 14]
valor_entero = int(input("Ingrese un valor entero: "))
tupla = ()

for valor in range(1, valor_entero + 1):
    if valor_entero % valor == 0:
        tupla = tupla + (valor,)

for valor in valores_posibles:
    if valor in tupla:
        print(f"El valor {valor} pertenece a la tupla")


# Una agencia inmobiliaria nos contrató para que la ayudemos a organizar la información dentro de su plataforma.
# Nos brindaron la siguiente información:

domicilio = ["Corrientes 2300", "Carabobo 1202", "Estados Unidos 1392", "Monasterio 55", "Luis Maria Campos 500"]
estructura = ["Casa", "Departamento", "PH", "Casa", "Loft"]


# Se debe, almacenar en una lista de tuplas, los pares (Estructura, Domicilio).
# Siendo el primer elemento de domicilio el correspondiente par de estructura y así con el resto.

lista_resultante = []

for indice in range(0, len(domicilio)):
    tupla = (estructura[indice], domicilio[indice])
    lista_resultante.append(tupla)

print(lista_resultante)

## Esto se puede simplificar utilizando la función zip()
resultado = list(zip(estructura, domicilio))
print(resultado)