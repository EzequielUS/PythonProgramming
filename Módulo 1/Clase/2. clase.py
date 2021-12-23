# # # # Funciones
# # # PATH = "./Carpeta"

# # # def modificador(*tupla, **diccionario):
# # #     """ 
# # #     Summary:
# # #         ....
    
# # #     Args:
# # #         valor1 (int): ..
# # #         valor1 (int): ..
# # #         valor1 (int): ..

# # #     Return: 
# # #         resultado (int): ...
# # #     """

# # # def modificador():
# # #     pass




# # # #################################
# # # def main():
# # #     print("Bienvenido usuario: ")

# # #     nombre = ("Ezequiel", "Ustar")
# # #     diccionario = {"domicilio": "Estados Unidos", "numero": 1444}
# # #     entero_1 = modificador(*nombre, **diccionario)

# # #     if entero_1 > 10:
# # #         pass


# # # if __name__ == "__main__":
# # #     main()



















# # ############################################

# # """ FIBONACCI """
# # # Claudio
# # fia = [0,1] 

# # numero = int (input ("ingrese numero para susecion:")) 
# # cont=0 

# # if numero < 2: 
# #     print ("numero debe ser mayor que 2") 

# # cuantas= int (input("cuantas sucesiones?")) 

# # def fib (a=numero, b=numero): 
# #     return int(a + b) 

# # while cuantas <= cont : 
# #     resultado = fia[-1] + fia[-2]
# #     fia.append(resultado)


# #     fib(numero)
# #     cont+=1 
# #     print(fib)



# # # Pablo
# # lista  = [0,1]
# # i = 1

# # while i<20:
# #     lista.append(lista[i-1] + lista[i])
# #     i+=1

# # print(lista)

# # # FEDE:
# # a, b = 0, 1
# # lista_fibonacci= [a,b]
# # resultado = int(input("Ingresa el total de numeros de tu lista: "))

# # for numero in range (resultado):
# #     b, a = a+b, b
# #     lista_fibonacci.append(b)
  
# # print(lista_fibonacci)


# # # Natalia:

# # def fib(elementos):
# #     a=0
# #     b=1
# #     c=a+b
# #     lista=[a,b]

# #     if elementos<2:
# #         print("La cantidad debe ser mayor a 2")
# #         return None

# #     for i in range(elementos-2):
# #         lista.append(c)
# #         a=b
# #         b=c
# #         c=a+b
# #     print(lista)

# # fib(15)



# # ####
# # def fib(cantidad):
# #     if cantidad < 2:
# #         print("Cantidad ingresada incorrecta")
# #         return None

# #     fibonacci = [0, 1]

# #     while len(fibonacci) < cantidad:
# #         fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
# #     return fibonacci


# # lista = fib(2)
# # print(f"Fibonacci de 2: {lista}")

# # lista = fib(5)
# # print(f"Fibonacci de 5: {lista}")

# # lista = fib(10)
# # print(f"Fibonacci de 10: {lista}")


# # """Promedio"""
# # # Pablo
# # def promedio_variable(*args):
# #     prom = sum(args)/len(args)
# #     return prom

# # resultado = promedio_variable(1,2,3,4,5,6,7,8)

# # # Leandro
# # def promedio_variable(*args):
# #     total = 0
# #     for n in args:
# #         total = n + total
# #     valor_final = total / len(args)
# #     return valor_final

# # print(promedio_variable(1,2,3))

# # # Fede:
# # import random

# # def promedio_variable():
# #     a,b,c = random.randint(0,10), random.randint(0,10), random.randint(0,10)
    
# #     print(a,b,c)
# #     promedio = (a + b + c) /3
    
# #     print(promedio)
# #     return promedio

# # promedio_variable()


# # Natalia:

# # def promedio_variable(*numeros):
# #     return sum(numeros)/len(numeros)

# # promedio=promedio_variable(3,7,22,9,0,123)
# # print(promedio)


# # """ Grupos """

# def equipo (*nombres, grupo = 2):
#     nombres = list(nombres)

#     if grupo < 2:
#         grupo = 2
    
#     matriz = []
    
#     while nombres:
#         lista = []

#         if len(nombres) < grupo:
#             for nombre in nombres:
#                 lista.append(nombre)
#             matriz.append(lista)
#             break

#         for i in range(grupo):
#             lista.append(nombres[i])
#             del(nombres[i])
#         matriz.append(lista)

#     return matriz

# equipos = equipo("Juan","Tamara","Lautaro","Gabriel","Agustin", grupo=3)
# # print(equipos)









# Orden superior
# def sumar(x): 
#     return x+100 

# def cuadrado(x): 
#     return x**2 

# def superior(funcion,lista): 
#     resultado = [] 
   
#     for n in lista: 

#         resultado.append(funcion(n)) 

#     return resultado 

# numeros = [2,5,10] 
# print(superior(sumar,numeros)) 
# print(superior(cuadrado,numeros)) 

# Funciones Lambda

# sumar = lambda x,y: x+y

print(lambda x,y: x+y(1,2))


#  map()













