"""
funciones osn fragmentos de codigos que podems reutilizar cada vez que que los necesitemos
ademas permiten la fragmentacion, o modular el desarrollo de una aplicacion
para utilizar una funcion llamamos a su nombre.


existen 2 tipos:
sin retorno: Que solamente hacen algo y hasta ahi se puede utilizar.
con retorno: Que nos entrega un valor para seguir trabajando sobre el.
"""

#Funcion para sumar dos numeros sin retornos
def suma1(num1, num2):
    suma =num1+num2
    print(f"El resultado de la suma es {suma}")
#Funcion para sumar dos numeros sin retornos
def suma2(num1,num2):
    suma =num1+num2
    return suma
def login(usuario : str, contrasena : str):
    if usuario =="duoc" and contrasena=="duocadmin":
        return True
    else:
        return False

suma1(20,50)
suma1(1000,-999)
suma1(1,15)
print(suma2(60,65)*2)

usuario=input("Ingrese usuario : ")
contrasena=input("Ingresa contrasena : ")
if login(usuario, contrasena):
    print("Usuario correcto")
else:
    print("Usuario incorrecto")

#Funcion para calcular el indice de masa corporal IMC peso/altura al cuadrado
def imc1(peso : int, altura : float)
    