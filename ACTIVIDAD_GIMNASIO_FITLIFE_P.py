import os
import msvcrt
import csv

#Funcion apra crear tittulo
def titulo(texto : str):
    os.system("cls")
    print(f"\033[33m🔰{texto.upper()}🔰\033[0m")
def error(texto : str):
    os.system("cls")
    print(f"\033[31m❌{texto.upper()}❌\033[0m")
def exito(texto : str):
    print(f"\033[32m✔{texto.upper()}✔\033[0m")
    
#TUPLAS - CLASES
clases=[
    ("PESAS","LUN-MIE 8:30-10:00AM",10),
    ("ZUMBA","MAR-JUE 3:30-5:40PM",20),
    ("NUTRICIÓN","VIE 6:00-7:30",2),
    ("CROSSFIT","SAB 11:30-12:55PM",10)]
#DICCIONARIO - USUARIOS
usuarios={}
#LISTA - RESERVAS
reservas=[]
#CONTADOR PARA EL ID DE USUARIO
numero_usuario=100
#INICIAR EL SISTEMA
print("<<PRESS ANY KEY>>")
msvcrt.getch()
os.system("cls")
while True:
    print("\033[35m═══════════════════════════════════")
    print("     SISTEMA GESTIÓN FITLIFE       ")
    print("═══════════════════════════════════\033[0m")
    print("1) REGISTRAR USUARIO")
    print("2) RESERVAR CLASES")
    print("3) CONSULTAR CLASES DISPONIBLES")
    print("4) CONSULTAR CLASES DE USUARIO")
    print("5) CONSULTAR USUARIOS")
    print("0) SALIR")
    print("\033[35m═══════════════════════════════════\033[0m")
    opcion=input("SELECCIONE: ")
    if opcion=="0":
        titulo("adios")
        break
    elif opcion=="1":
        titulo("registrar ususario")
        nombre=input("Ingrese nombre de usuario : ").title()
        #validar que nombre de usuaio no se repita
        if nombre not in usuarios.values():
            usuarios[numero_usuario]=nombre
            exito(f"Usuario registrado {numero_usuario}")     
            numero_usuario+=100        

        else:
            error("Usuario ya registrado")
    elif opcion=="2":
        titulo("Reservar clase")
        codigo=int(input("Ingrese codigo de usuario : "))
        if codigo in usuarios:
            curso=input("Ingrese curso para inscribir : ").capitalize()
            centinelaCurso=False
            centinelaCupo=False
            for c in clases:
                if c[0].capitalize()==curso:
                    centinelaCurso=True
                    if c[2]>0:#verificamos si hay cupos
                        centinelaCupo=True
                        #realizar la reserva
                        reservas.append([codigo, usuarios[codigo],c[0],c[1]])
                        exito("Reserva Realizada")
                        #descontar cupo
                        actualizacionCupo= (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacionCupo)
                        #Registrar reserva
                        with open('reporte_reservas.csv','w',newline='', encoding='utf-8') as f:
                            escrbir=csv.writer(f,delimiter=',')
                            escrbir.writerow(reservas)
                        break
                if centinelaCurso==False:
                    error("No existe el curso")
                if centinelaCupo==False:
                    error("No existe cupo")
        else:
            error("Codigo no existe")
    elif opcion=="3":
        titulo("Consultar clases disponibles")
        for c in clases:
            print(f"{c[0]} Horario: {c[1]} Cupos{c[2]}")
    elif opcion=="4":
        titulo("Consultar reservas de usuario")
        if len(reservas)>0:
            codigo=int(input("Ingrese codigo de usuario : "))
            centinela=False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]} Curso:{r[2]} Horario: {r[3]}")
                    centinela=True
            if centinela==False:
                    error("El codigo no tiene reservas asociadas")
        else:
            error("No existen reseras")

    elif opcion=="5":
        titulo("Consultar ususarios")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
        else:
            error("No hay usuarios registrados")
    else:
        error("OPCION NO VALIDA")


