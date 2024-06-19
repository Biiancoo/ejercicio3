import os,time,csv
from funciones_contacto import *
contactos = []
while True:
    os.system('cls')
    print("MENU CONTACTO")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Guardar contactos en un archivo csv")
    print("4. Salir")
    opciones = (1,2,3,4)
    opc = validar_ocpiones(opciones)
    os.system('cls')
    if opc == 1:
        nombre = validar_nombre()
        numero = validar_numero() 
        correo = validar_correo()
        contacto = {'nombre': nombre,
                    'numero': numero,
                    'correo': correo}
        contactos.append(contacto)
        print("Contacto agregado correctamente...")
    elif opc == 2:
        mostrar_contactos(contactos)
    elif opc == 3:
        exportar_archivo(contactos)
    else:
        print("ADIOS!!")
        time.sleep(2)
        break
