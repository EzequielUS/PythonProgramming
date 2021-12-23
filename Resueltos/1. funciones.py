"""
Crear un programa que:

Cree una función llamada “superior” que reciba por argumento una función y una lista. 
La función que se pasa por argumento a superior debe elevar al cubo un número y retornarlo, para que luego al aplicarla en la de orden superior, esa operación se realice miembro a miembro de la lista. 
Para finalizar la función “superior” debe de devolver una nueva lista.

"""

def superior(funcion,lista):
    nueva = []
    for n in lista:
        nueva.append(funcion(n))
    return nueva


######################################


print(superior(lambda x : x**3,[1,2,3]))


"""
1. Crear las funciones max() y min() , las cuales reciban una lista o tupla de valores enteros como argumento  y devuelven el valor más alto y más bajo de dicha estructura. La idea es resolver el algoritmo de esta función sin usar las funciones max() y min()  incorporadas del lenguaje. 

Cree una función llamada "operador" que reciba por argumento una función y una lista. 

Utilizar la lista
lista_1 = [1,2,4,2,1,-5,6,888,6,3]

Y obtener sus valores maximos y minimos a traves de la función operador.
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

def operador(funcion, lista):
    resultado = funcion(lista)
    return resultado


lista_1 = [1,2,4,2,1,-5,6,888,6,3]

print(operador(max, lista_1))
print(operador(min, lista_1))