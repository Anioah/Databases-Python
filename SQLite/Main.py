import sys
from OpcionesMenu import *

def menu():
    print("\n Menú \n \n 1) Mostrar Empresas \n 2) Alta de Empresa \n 3) Modificar Empresa \n 4) Mostrar Empleados \n 5) Alta de Empleados \n 6) Modificar Empleado \n 7) Eliminar Empleado \n 8) Salir")
    menu = input("\n Elije una opción: ")
    return menu


opc = menu()


while opc != "unNumeroQueNoViene":
    
    if opc == "1":
        OpcionesMenu.showCompany()
        opc = menu()

    elif opc == "2": 
        OpcionesMenu.Company()
        OpcionesMenu.updateCompany()
        opc = menu()

    elif opc == "3":
        OpcionesMenu.updateCompany()
        opc = menu()
    
    elif opc == "4":
        OpcionesMenu.showEmployee()
        opc = menu()

    elif opc == "5":
        OpcionesMenu.Employee()
        opc = menu()
    
    elif opc == "6":
        OpcionesMenu.updateEmployee()
        opc = menu()
    
    elif opc == "7":
        OpcionesMenu.deleteEmployee()
        opc = menu()

    elif opc == "8":
        print("\n Programa finalizado \n")
        sys.exit()
        
    else:
        print("\n Ingresa una opción válida \n")
        opc = menu()

