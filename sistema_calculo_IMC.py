import msvcrt
import os
import csv
#coleccion para guardar imc
lista_imc=[]
#Funciones para el programa
#1.-Calcular imc
def calcularIMC(peso, altura):
    resultado=peso/(altura**2)
    return resultado
#2.-Verificar estdado del imc
def estadoIMC(resultado):
    if resultado<18.5:
        return"bajo peso"
    elif resultado>=18.5 and resultado<=24.9:
        return"adecuado"
    elif resultado>=25 and resultado<=34.9:
        return"sobrepeso"
    elif resultado>=30 and resultado<=34.9:
        return"obesidad grado 1"
    elif resultado>=35 and resultado<=39.9:
        return"obesidad grado 2"
    else:
        return "obesidad grado 3"
#3.-Imprimir imc list
def imprimiReporte(archivo):
    with open(archivo, 'w', newline='',encoding='utf-8') as a:
        escribir=csv.writer(a,delimiter='')
        escribir.writerow(lista_imc)
while True:
    print("<<pres and key>>")
    msvcrt.getch()
    os.system("cls")


    nombre=input("Ingrese su nombre : ").title()
    peso =float(input("Ingrese su peso : "))
    altura=float(input("Ingrese su altura : "))

    imc=calcularIMC(peso,altura)
    print(f"si imc es {imc}")
    print(estadoIMC)

    lista_imc
                

    resp=input("desea salir (s/n): ").lower()
    if resp=="s":
        break