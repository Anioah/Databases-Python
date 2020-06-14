from Client import Client
from Company import *
""" from app import app """
from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

db = client['company_register']
collection1 = db['company']
collection2 = db['client']
collection3 = db['sales']

import sys

def menu():

    print("\n Menú \n \n 1) Alta de Empresa \n 2) Mostrar datos empresas \n 3) Mostrar datos clientes \n 4) Editar datos \n 5) Eliminar Empresa \n 6) Eliminar Cliente \n 7) Salir")
    menu = int(input("Selecciona una opción: "))
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
    collection1.insert_one({"RFC": RFC_e, "name": name_e, "Address": direction_e })
    return newCompany



def newClient():
    print("\n Introduce un nuevo cliente \n ")

    RFC_c = input("Introduce el RFC del Cliente: ")
    name_c = input("Introduce el Nombre del Cliente: ")
    direction_c = input("Introduce la Dirección del Cliente: ")
    name_com = input("Introduce la empresa asociada")

    newClient = Client(RFC_c, name_c, direction_c,name_com)
    collection2.insert_one({"RFC": RFC_c, "Name": name_c, "Address":direction_c, "Partner": name_com})
    print("\n ***** Cliente agregado con éxito *****" )

    return newClient

if opc is 1:

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

elif opc is 2:
    
    if newClient!="":
        for documento in collection1.find({}):
            print(documento)
        opc = menu()
        
    else:
        print("\n No existen registros ")
        opc=menu()

elif opc is 3:

    print("Ingrese el nombre de la empresa asociada: ")
    name = str(input())
    if newClient!="":
        for documento in collection2.find({
            "Partner": name
        }):
            print(documento)
        menu()
        opc = input("\n Elije una opción: ")

    else:
        print("\n No existen registros ")
        opc=menu()

elif opc is 5:

    print("Ingrese el nombre de la empresa a eliminar: ")
    delete_name = str(input())
    if newClient!="":
        collection1.delete_one({
            "name": delete_name
        })
        collection2.delete_one({
            "Partner": delete_name
        })
        print("Eliminado Exitosamente")
        print("\n Menú de registro \n \n 1) Nueva Empresa\n 2) Mostrar datos de clientes \n 3) Fin")
        opc = input("\n Elije una opción: ")

elif opc is 6:

    print("Ingrese RFC del cliente a eliminar: ")
    delete_rfc = str(input())
    if newClient!="":
        collection2.delete_one({
            "RFC": delete_rfc
        })
        print("Eliminado Exitosamente")
        menu()
        opc = input("\n Elije una opción: ")
    
elif opc is 7:
        print("Programa finalizado ")
        sys.exit()

# init commit