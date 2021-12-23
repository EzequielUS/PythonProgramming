"""
Se tiene una lista con información de diferentes personas, el problema es que cada elemento de la lista es un str. 

personas = [ "Rosa 55 Ingeniera", "Tamara 30 Contadora", "Juan 25 Programador", "Tomas 30 Profesor" ] 

Trabajar con los elementos (str) y conseguir una lista con varios diccionarios. 

Debería quedar algo así: 
[{'nombre': 'Rosa', 'edad': 55, 'profesion': 'Ingeniera'}, {'nombre': 'Tamara', 'edad': 30, 'profesion': 'Contadora'}, {'nombre': 'Juan', 'edad': 25, 'profesion': 'Programador'}, {'nombre': 'Tomas', 'edad': 30, 'profesion': 'Profesor'}]
"""

def limpiar(lista):
    datos_personas = []
    for texto in lista:
        datos = texto.split()
        diccionario = {"nombre":datos[0].capitalize(),"edad":int(datos[1]),"profesion":datos[2].capitalize()}
        datos_personas.append(diccionario)
    print(datos_personas)


##############################################################

personas = [
    "Rosa 55 Ingeniera",
    "Tamara 30 Contadora",
    "Juan 25 Programador",
    "Tomas 30 Profesor" ]

limpiar(personas)



"""
Con base a la siguiente cadena de texto, la cual representa los procesos corriendo en una PC.

Obtener los valores correspondientes al PID, Process y User, y almacenarlos en una lista.
"""

p = """+-------+--------------------------------------+-----------------------------+
| PID   | Process                              | User                        |
+-------+--------------------------------------+-----------------------------+
| 0     | System Idle Process                  | NT AUTHORITY\SYSTEM         |
| 4     | System                               | NT AUTHORITY\SYSTEM         |
| 104   |                                      | -                           |
| 168   | Registry                             | -                           |
| 552   | smss.exe                             | -                           |
| 664   | IntelCpHDCPSvc.exe                   | -                           |
| 680   | svchost.exe                          | -                           |
| 852   | csrss.exe                            | -                           |
| 964   | wininit.exe                          | -                           |
| 1056  | Code.exe                             | DESKTOP-BFM0U3K\EducaciónIT |
| 1108  | services.exe                         | -                           |
| 1128  | LsaIso.exe                           | -                           |
| 1136  | lsass.exe                            | -                           |
| 1204  | svchost.exe                          | -                           |
| 1260  | svchost.exe                          | -                           |
| 1292  | fontdrvhost.exe                      | -                           |
| 1328  | NGenuity2Helper.exe                  | DESKTOP-BFM0U3K\EducaciónIT |
| 1372  | WUDFHost.exe                         | -                           |
| 1432  | svchost.exe                          | -                           |
| 1484  | WUDFHost.exe                         | -                           |
| 1508  | svchost.exe                          | -                           |
| 1516  | conhost.exe                          | DESKTOP-BFM0U3K\EducaciónIT |
+-------+--------------------------------------+-----------------------------+
"""

lineas = p.strip().split("\n")[3:-1]
procesos = []

for linea in lineas:
    elementos = []
    columnas = linea[1:-1].split("|")
    procesos.append(elementos)

    for columna in columnas: 
        elementos.append(columna.strip())
    
    procesos.append(elementos)

print(procesos)