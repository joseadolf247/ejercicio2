from ast import If
from email import header
from genericpath import isfile
import random
from datetime import datetime
import pandas as pd 
import os
# leer archivos
def obtener_csv_como_lista_de_diccionariosclientes(nombre_archivos):
    separador= ','
    with open(nombre_archivos, encoding="utf-8") as archivo:
        next(archivo)
        cliente=[]
        for linea in archivo:
            linea = linea.rstrip('\n')
            columnas = linea.split(separador)
            clavecliente = columnas[0]
            nombrecliente = columnas[1]
            cliente.append({'Clave Cliente: ':  clavecliente, 'Nombre Cliente: ' : nombrecliente})
        return cliente
def obtener_csv_como_lista_de_diccionariossalas(nombre_archivos):
    separador= ','
    with open(nombre_archivos, encoding="utf-8") as archivo:
        next(archivo)
        salas=[]
        for linea in archivo:
            linea = linea.rstrip('\n')
            columnas = linea.split(separador)
            clavesala = columnas[0]
            nombresala = columnas[1]
            cuposalas = columnas[2]
            salas.append({ 'Clave sala: ':  clavesala , 'Nombre Sala: ' : nombresala, 'Cupo Sala: ' : cuposalas })
        return salas
def obtener_csv_como_lista_de_diccionariosreservaciones(nombre_archivos):
    separador= ','
    with open(nombre_archivos, encoding="utf-8") as archivo:
        next(archivo)
        reserva=[]
        for linea in archivo:
            linea = linea.rstrip('\n')
            columnas = linea.split(separador)
            diareserva = columnas[0]
            clavereserva = columnas[1]
            sala = columnas[2]
            claveclient = columnas [3]
            turn=columnas[4]
            descript=columnas[5]
            reserva.append ({ 'Dia de reservacion: ': diareserva, 'Clave reservacion: ': clavereserva, 'Sala: ':sala, 'Clave cliente: ':claveclient, 'Turno: ':turn, 'Descripcion/Nombre Reservacion: ':descript })
        return reserva
# diccionarios de reservacion
salas=[]
cliente=[]
reserva=[]
# listas para aleatoriedad
turno=["Matutino", "Vespertino", "Nocturno"]
nombre_clientes = 'clientes.csv'  
nombre_salas= 'salas.csv'
nombre_reservaciones='reserva.csv'
if os.path.isfile(nombre_clientes and nombre_salas and nombre_reservaciones) is True:
    cliente = obtener_csv_como_lista_de_diccionariosclientes('clientes.csv')
    cliente = pd.read_cvs('clientes.csv', header= None)
    salas = obtener_csv_como_lista_de_diccionariossalas('salas.csv')
    salas = pd.read_cvs('salas.csv', header= None)
    reserva = obtener_csv_como_lista_de_diccionariosreservaciones('reserva.csv')
    reserva = pd.read_cvs('reserva.csv', header= None)
else: 
    print("No hay archivos previos") 
while True :
   print( "")
   print("(1) Revesaciones")
   print("(2) Reportes")
   print("(3) Registrar una sala.")
   print("(4) Registrar a un nuevo cliente.")
   print("(5) Salir")
   print( "")
   menu = int(input(f'¿Que opcion realizara?: '))
   if menu == 1:
        while menu == True :
            print( "")
            print("(1) Registrar una nueva reservacion")
            print("(2) Modificar descripcion de una reservacion")
            print("(3) Consultar disponibilidad de una sala")
            print( "")
            menu2 = int(input(f'¿Que opcion realizara?: '))
            if menu2 == 1:
                dia = input("¿Que dia deseas realizar la reservacion? (FORMATO DD/MM/YY): ")
                print("Salas disponibles: ")
                for diaasignado in reserva:
                    for dianoasignado in salas:
                        print('\t', dianoasignado['Nombre Sala: '] - diaasignado['Sala: ']) 
                for dianoasignado in salas:
                    print('\t', dianoasignado['Nombre Sala: '])
                salaescoger=input("¿Que sala escogera?: ")
                if salaescoger in dianoasignado['Nombre Sala: ']: 
                    print("Ingrese una sala valida")                
                    salaescoger=input("¿Que sala escogera?: ")
                else: 
                    print("Estas son las claves de los clientes registrados: ")
                    for clavesasigcliente in cliente:
                        print('\t', clavesasigcliente['Nombre Cliente: '])
                numcliente = input("¿Cual es su numero de cliente?:  ")
                if numcliente in clavesasigcliente['Nombre Cliente: ']: 
                    print("Ingrese una sala valida")                
                    numcliente = input("¿Cual es su numero de cliente?:  ")
                else: 
                    print("Turnos que contamos: ")
                    for recorrido in turno:
                        print('\t', recorrido)
                    turnoescoger=input("¿Cual turno escogera?: ")
                    for clavesturno in reserva:
                        if turnoescoger in clavesturno['Turno: ']: 
                            print("Ingrese una sala valida")                
                            turnoescoger=input("¿Cual turno escogera?: ") 
                descripcion = input("Descripcion/Nombre de la reservacion: ")
                mi_listareser=[]
                for i in range(1, 2):
                    mi_listareser.append(random.randint(0, 20))
                    unicosreser = list(dict.fromkeys(mi_listareser))
                print("Tu clave de reservacion es: ")   
                print(unicosreser)
                reserva.append ({ 'Dia de reservacion: ': dia, 'Clave reservacion: ': unicosreser, 'Sala: ':salaescoger, 'Clave cliente: ':numcliente, 'Turno: ':turnoescoger, 'Descripcion/Nombre Reservacion: ':descripcion })
                menu = False
            elif menu2 == 2:
                print("Estas son las claves de las salas reservadas: ")
                print(reserva['Sala: '])
                clave= input("¿Cual es el nombre de sala desea modificar?: ")
                des=input("Ingrese la descripcion/nombre que quedara: ")
                for recorrido in reserva:
                    if clave not in recorrido['Sala: ']:
                        reserva['Descripcion/Nombre Reservacion: '] = des
            elif menu2 == 3: 
                dia2 = input("¿Que dia desea rentar la sala?: (FORMATO DD/MM/YY): ")
                print("Estas son las salas disponibles para este dia: ")
                for recorrido in reserva:
                    if dia2 not in recorrido['Dia de reserva: ']:
                        print("no hay salas disponibles")
                    else: 
                        print(recorrido['Sala: '])
   elif menu == 2:
        while menu ==True :
            print( "")
            print("(1) Reporte en pantalla de reservaciones para una fecha")
            print("(2) Exportar reporte tabular a excel")
            print( "")
            menu3 = int(input(f'¿Que opcion realizara?: '))
            if menu3 == 1:
                fecha3=input("¿De que dia desea el reporte? (formato dd/mm/yy) : ")
                for fecha in reserva:
                    if fecha3 == fecha['Dia de reserva: ']:
                        print("Reporte de dia ", fecha['Dia de reserva: '])
                        print("\t, Sala: ", fecha['Sala: '])
                        print("\t, Turno: ", fecha['Turno: '])
                        print("\t, Clave de cliente: ", fecha['Clave cliente: '])
                        print("\t, Clave de cliente: ", fecha['Descripcion/Nombre Reservacion: '])
            elif menu3 == 2:
                cliente.to_excel('cliente.xlsx', sheet_name= 'clientes')
                salas.to_excel('salas.xlsx', sheet_name= 'salas')
                reserva.to_excel('reservas.xlsx', sheet_name= 'reserva')
                print("Se exportaran datos a excel...")
                
   elif menu == 3:
        mi_listasala=[]
        for i in range(1, 2):
            mi_listasala.append(random.randint(0, 20))
            unicossala = list(dict.fromkeys(mi_listasala))
        print("La clave de sala sala: ")
        print(unicossala)
        nomsala=input("¿Cual sera el nombre de la sala?: ")
        cuposala=input("¿Cual es el cupo de la sala?: ")
        salas.append ({ 'Clave sala: ':  unicossala , 'Nombre Sala: ' : nomsala, 'Cupo Sala: ' : cuposala })
        print("Se ha registrado con exito la sala")
   elif menu == 4:
        mi_listacliente=[]
        for i in range(1, 2):
            mi_listacliente.append(random.randint(0, 20))
            unicoscliente = list(dict.fromkeys(mi_listacliente))
        print("La clave del cliente sera: ")
        print(unicoscliente)
        nomcliente=input("¿Cual es el nombre del cliente?: ")
        cliente.append ({ 'Clave Cliente: ':  unicoscliente, 'Nombre Cliente: ' : nomcliente })
        print("Se ha registrado con exito el cliente")
   elif menu == 5:
        print("Se esta guardaando informacion en cvs...")
        cliente.to_csv('clientes.csv')
        salas.to_csv('salas.csv')
        reserva.to_csv('reserva.csv')
        print("...")
        print("Saliendo..")
        break
