# # Estructuras complejas
# listas = [1, "Ezequiel", True, int()]

# listas[0] = 2
# listas[1] = "Matias"
# listas[2] = False

# listas.append(123)
# listas.insert(0, "VALOR")

# listas[0:2:1]


# ######

# tuplas = (1, "Ezequiel", True, int())
# elemento = tuplas[0]

# tuplas.index()
# tuplas.counter("Ezequiel")


# #####

# diccionarios = {
#     'valor': 1,
#     'valor_2': 2,
# }

# elemento = diccionarios["valor"]


# ##################

# alumnos = [["Ezequiel", "Python Programming"], ["Romina", "Python para visualizacion"]]

# diccionarios = {
#     "Ezequiel": {
#         'curso': "Python Programming"
#     }
# }

# curso = alumnos[0][1]
# curso = diccionarios["Ezequiel"]["curso"]


# ################
# longitud_de_alumnos = len(alumnos)
# longitud_de_alumnos = len(diccionarios)

# alumnos[2] = "Nada"

# del alumnos[2]
# del curso

# ################

# edad = 18

# if edad >= 18:
#     print("Sos mayor de edad")
# elif edad > 12 and edad < 18:
#     print("No podes ingresar")
# else:
#     print("Sos muy menor.")


"""
Crear un programa que:
Utilice una estructura que me permita asociar roles junto a sus contraseñas.
Pregunte el tipo de rol que desempeña una persona en una institución (“admin”, “profesor”, ”alumno”). 
Luego se deberá pedir una contraseña, siendo la única válida, la que se ha definido previamente según su rol. 
Si la contraseña ingresada es válida, se procederá a pedir el nombre de la persona, y si no es vacío, se la saludara. 

Contemplar los casos donde no se cumple como corresponde, y mostrar un mensaje en pantalla. 

"""