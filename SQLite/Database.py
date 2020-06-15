import sqlite3
from sqlite3 import Error
import os

class Database:


    def sql_connection():

        app_path = os.getcwd()
        db_path = app_path + '/Empresas.db'

        try:
            con = sqlite3.connect(db_path)
            return con

        except Error:
            print(Error)
        


    def sql_company(con, nombre, rfc):

        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO Empresas VALUES(null, ?, ?)', [nombre, rfc])

        con.commit()
        con.close()
    


    def sql_showCompany(con):

        cursorObj = con.cursor()
        cursorObj.execute('SELECT * FROM Empresas')

        Companies = cursorObj.fetchall()

        for Company in Companies:

            print(Company)
        
        print("\n")



    def sql_updateCompany(con, nombre, rfc, id_empresa):
        
        cursorObj = con.cursor()
        cursorObj.execute('UPDATE Empresas SET nombre = ?, rfc= ? where id_empresa = ?',[nombre,rfc,id_empresa])

        con.commit()



    def sql_employee(con, rfc, nombre, ap_paterno, ap_materno, direccion, telefono, sexo, empresa ):

        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO Empleados VALUES(null, ?,?,?,?,?,?,?,?)", (rfc, nombre, ap_paterno, ap_materno, direccion, telefono, sexo, empresa))

        con.commit()
        con.close()
    


    def sql_showEmployee(con, id_empresa):

        cursorObj = con.cursor()
        cursorObj.execute('SELECT * FROM Empleados where fk_empresa = ?', [id_empresa])

        Employees = cursorObj.fetchall()

        for Employee in Employees:

            print(Employee)
        
        print("\n")
    


    def sql_deleteEmployee(con, id_empleado):
        
        cursorObj = con.cursor()
        cursorObj.execute('DELETE FROM Empleados WHERE id_empleado = ?', [id_empleado])
        
        con.commit()
        con.close()



    def sql_subcategory(con, descripcion):

        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO SubCategorias VALUES(null, ?)', [descripcion])

        con.commit()
        con.close()



    def sql_category(con, descripcion, subcategoria):

        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO Categorias VALUES(null, ?, ?)', [descripcion, subcategoria])

        con.commit()
        con.close()



    def sql_game(con, descripcion, precio_unitaro, cantidad, categoria):

        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO Juegos VALUES(null, ?,?,?,?)", (descripcion, precio_unitaro, cantidad, categoria))

        con.commit()
        con.close()
    


    def sql_type_client(con, descripcion):

        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO Tipo_Clientes VALUES(null, ?)', [descripcion])

        con.commit()
        con.close()



    def sql_client(con, rfc, nombre, ap_paterno, ap_materno, direccion, telefono, sexo, correo_electronico, tipo_cliente):

        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO Clientes VALUES(null, ?,?,?,?,?,?,?,?,?)", (rfc, nombre, ap_paterno, ap_materno, direccion, telefono, sexo, correo_electronico, tipo_cliente))

        con.commit()
        con.close()

