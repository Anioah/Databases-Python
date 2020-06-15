from Database import *

class OpcionesMenu:


    def Company():

        print("\n Registre una nueva Empresa \n")

        nombre = input("Ingresa el nombre de la empresa: ")
        rfc = input("Ingresa el RFC de la empresa: ")

        Database.sql_company(Database.sql_connection(), nombre, rfc)

        print("Empresa creada correctamente")

    

    def showCompany():

        print("\n")
        Database.sql_showCompany(Database.sql_connection())



    def updateCompany():

        print("\n Actualizar Empresa \n")

        nombre = input("Ingresa el nombre de la empresa: ")
        rfc = input("Ingresa el RFC de la empresa: ")
        id_empresa = input("Indique la clave de identificación de la empresa: ")

        Database.sql_updateCompany(Database.sql_connection(), nombre, rfc, id_empresa)

        print("Empresa actualizada correctamente")



    def Employee():

        print("\n Registre al Empleado \n")

        rfc = input("Ingrese el RFC del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        ap_paterno = input("Ingrese el apellido paterno: ")
        ap_materno = input("Ingrese el apellido materno: ")
        sexo = input("Ingrese el sexo del empleado: ")
        direccion = input("Ingrese la direccion del empleado: ")
        telefono = input("Ingrese un número telefónico: ")
        empresa = input("Ingrese el número de identificación de la empresa donde será empleado: ")

        Database.sql_employee(Database.sql_connection(), rfc, nombre, ap_paterno, ap_materno, direccion, telefono, sexo, empresa)

        print("Empleado dado de alta satisfactoriamente")



    def showEmployee():

        id_empresa = input("\n Indique el número de identificación de la empresa del empleado \n")
        print("\n")
        Database.sql_showEmployee(Database.sql_connection(), id_empresa)



    def updateEmployee():

        print("\n Actualización de Empleado \n")
        id_empleado = input("Indique la clave de identificación del empleado: ")
        Database.sql_updateEmployee(Database.sql_connection(), id_empleado)


    def deleteEmployee():

        print("\n Baja de Empleado \n")
        id_empleado = input("Indique la clave de identificación del empleado: ")
        Database.sql_deleteEmployee(Database.sql_connection(), id_empleado)

        print("Empleado eliminado correctamente")



    def Subcategory():
        
        print("\n Registre la Subcategoria \n")

        descripcion = input("Ingrese el nombre de la subcategoria: ")

        Database.sql_subcategory(Database.sql_connection(), descripcion)

        print("Subcategoria agregada correctamente")



    def Category():

        print("\n Registre la Categoria \n")

        descripcion = input("Ingrese el nombre de la categoria: ")
        subcategoria = input("Ingrese la subcategoria a la que pertenece: ")

        Database.sql_category(Database.sql_connection(), descripcion, subcategoria)

        print("Categoria agregada correctamente")



    def Game():

        print("\n Registre el Producto \n")

        descripcion = input("Ingrese el nombre del juego: ")
        precio_unitario = input("Ingrese el precio unitario: ")
        cantidad = input("Ingrese la cantidad del stock: ")
        categoria = input("Ingrese la categoria a la que pertenece: ")

        Database.sql_game(Database.sql_connection(), descripcion, precio_unitario, cantidad, categoria)

        print("Producto agregado correctamente")



    def Type_Client():

        print("\n Registre el tipo de Cliente \n")

        descripcion = input("Ingrese la descripción: ")

        Database.sql_type_client(Database.sql_connection(), descripcion)

        print("Tipo de Cliente agregado correctamente")



    def Client():

        print("\n Registre al Cliente \n")

        rfc = input("Ingrese el RFC del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        ap_paterno = input("Ingrese el apellido paterno: ")
        ap_materno = input("Ingrese el apellido materno: ")
        sexo = input("Ingrese el sexo del cliente: ")
        direccion = input("Ingrese la direccion del cliente: ")
        telefono = input("Ingrese un número telefónico: ")
        correo_electronico = input("Ingrese el correo electrónico: ")
        tipo_cliente = input("Ingrese si el cliente es Físico (1) o Moral (2): ")

        Database.sql_client(Database.sql_connection(), rfc, nombre, ap_paterno, ap_materno, direccion, telefono, sexo, correo_electronico, tipo_cliente)

        print("Empleado dado de alta satisfactoriamente")