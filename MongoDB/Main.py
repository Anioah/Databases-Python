from Client import Client
from Company import *
import sys

def menu():
    print("\n Menú \n \n 1) Alta de Empresa \n 2) Mostrar datos \n 3) Salir")
    menu = input("\n Elije una opción: ")
    return menu


opc = menu()

newClient = ""
companies = []



def newCompany():
    print("\n Registre una nueva Empresa \n")

    RFC_e = input("Introduce el RFC de la Empresa: ")
    name_e = input("Introduce el Nombre: ")
    direction_e = input("Introduce la Dirección: ")
    clients = []
    newCompany = Company(name_e, RFC_e, direction_e, clients)

    return newCompany



def newClient():
    print("\n Introduce un nuevo cliente \n ")

    RFC_c = input("Introduce el RFC del Cliente: ")
    name_c = input("Introduce el Nombre del Cliente: ")
    direction_c = input("Introduce la Dirección del Cliente: ")

    newClient = Client(RFC_c, name_c, direction_c)

    print("\n ***** Cliente agregado con éxito *****" )

    return newClient




while opc != "3":

    if opc == "1":

        opt = ""

        new_comp = newCompany()
        companies_list = Companies(companies)
        companies_list.addCompany(new_comp)
        
        while opt != "no":
            new_comp.add(newClient())
            opt = input("\n ¿Desea introducir un nuevo cliente? ")

        else:
            
            print("\n  **************** Empresa agregada con éxito ****************")
            opc=menu()

    elif opc == "2":

        if newClient!="":

            print(repr(companies_list))
            print("\n Menú de registro \n \n 1) Nueva Empresa\n 2) Mostrar \n 3) Fin")
            opc = input("\n Elije una opción: ")

        else:
            print("\n No existen registros ")
            opc=menu()
else:
    print("Programa finalizado ")
    sys.exit()


# init commit