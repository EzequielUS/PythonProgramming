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


"""
Crear un programa que:

Contenga una función que se llame “promedio_variable”. 
Esta función debe tomar un número arbitrario de argumentos numéricos y devolver el promedio.
"""


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


"""
Crear las funciones max() y min() , las cuales reciban una lista o tupla de valores enteros como argumento  y devuelven el valor más alto y más bajo de dicha estructura. La idea es resolver el algoritmo de esta función sin usar las funciones max() y min()  incorporadas del lenguaje. 
"""


"""
Crear la función sum(), la cual reciba una lista o tupla de valores enteros como argumento  y devuelva la suma de los valores pertenecientes a dicha estructura. La idea es resolver el algoritmo de esta función sin usar la función sum() incorporada del lenguaje. 
"""


"""
Crear una función que me permita obtener las raíces de un polinomio de grado 2. 
Resultados esperados:  raices(1, 1, -6) ->  (2.0, -3.0)
"""


"""
Escribir un programa que cree un diccionario vacío y lo vaya llenando con personas. Donde el nombre(str) será la clave(el key) y el valor(value) la edad(int). El programa debe estar acompañado de un menú: 

Menú: 
A) Agregar. 
B) Mostrar el más chico. 
C) Mostrar el más grande. 
D) Salir. 

La opción de agregar inserta a una persona. Mostrar el más chico, nos debería mostrar el nombre de la persona más chica, y viceversa el de mostrar el más grande. Con la opción 4 deberíamos salir del programa.

"""