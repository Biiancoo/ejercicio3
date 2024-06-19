import os,time,csv


def validar_ocpiones(opc):
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in opc:
                return opcion
            else:
                print("ERROR,ingrese una opcion valida!!")

        except:
            print("ERROR,la opcion debe ser ingresada en numeros enteros!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre de la persona que desea agregar: ")
        if len(nombre)>=3 and len(nombre)<=10:
            print("Nombre guardado con exito")
            
            return nombre
        else:
            print("ERROR,ingrese un nombre valido")
      

def validar_numero():
    while True:
        numero = input("Ingrese numero de telefono (solo 8 digitos): ")
        if len(numero) == 8 and numero.isdigit():
            print("Numero guardado con exito")
            return numero
        else:
            print("ERROR,debe ingresar 8 digitos")
     

def validar_correo():
    while True:
        correo = input("Ingrese correo electronico: ")
        if '@' and ".com" or ".cl" in correo:
            print("Correo guardado con exito")
            time.sleep(2)
            return correo
        else:
            print("ERROR,correo mal ingresado, verifique si se encuentra (@ , .com /.cl)")



def mostrar_contactos (contactos):
    if not contactos:
            print("No hay contactos para guardados...")
            time.sleep(2)

    else:
        for x in range(len(contactos)):
            contacto = contactos[x]
            print(f"Contacto {x + 1}: ")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Número: {contacto['numero']}")
            print(f"Correo: {contacto['correo']}")
            print("")
        time.sleep(4)


def exportar_archivo(contactos):
    if len(contactos)==0:
        print("Lista vacia, registre un trabajado en la opción 1")
        time.sleep(2)
    else:
        nombre_archivo = str(input("Ingrese nombre del archivo: "))
        with open( nombre_archivo + ".csv","w",newline="") as archivo:
            archivo.write(f"Nombre,Número,Correo\n")
            for x in contactos:
                archivo.write(f"{x['nombre']},{x['numero']},{x['correo']}\n")
        print("Se a guardado correctamente")

