import csv
import os
import time



def verificador_edad():
    while True:
        try:
            valor = int(input(f"Ingrese edad: "))
            if valor >=0 and valor <136:
                print("Edad guardada correctamente")
                time.sleep(1)
                return valor
            else:
                print("Error, ingrese edad valida")
        except:
            print("Ingrese la edad correctamente (en numeros enteros)")

def verificador_valor(texto):
    while True:
        valor=input(f"Ingrese {texto}: ")
        if len(valor)>=3:
            print(f"{texto} guardado correctamente")
            time.sleep(1)
            return valor
        else:
            print(f"Error,el {texto} no es valido!!!")

def verificador_eleccion():
    opc = input("Desea seguir agregando personas?\n-Seleccione cualquier letra para continuar agregando\n-Escriba NO para parar de agregar personas\n").upper()
    if opc.upper() == "NO":
        return opc
    else:
        return "SI"



def nombre_corto(personas):

    for nombre in personas :
        if nombre == 0:
            nombre_mas_largo = personas[0]
        else:
            if len(personas[nombre])<len(nombre_mas_largo):
                nombre_mas_largo = personas[nombre]
                
    
    return nombre_mas_largo
