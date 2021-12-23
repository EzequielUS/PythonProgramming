"""
Instalar el módulo requests vía pip y crear un script que obtenga el contenido de una dirección de URL y 
lo guarde en un archivo local. 
(Utilizar el método get(“<ingresar_la_dirección>”))
"""

import requests

# Educación IT
respuesta = requests.get(r"https://www.educacionit.com/")
print(respuesta)
print(respuesta.content)
# print(respuesta.status_code)

# API Random
respuesta = requests.get(r"https://reqres.in/api/users?page=2")
print(respuesta.content)
print(respuesta.status_code)