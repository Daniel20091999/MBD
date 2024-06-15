import pymysql
import os

class app:

    def __init__(self):

        self.conn = pymysql.connect(
            host = 'localhost',
            user ='root',
            passwd='root',
            db='MBD')
        self.cursor = self.conn.cursor()

    
    def añadir_empresa(self):
        #pedimos al usuario los datos a añadir
        nombre_empresa = str(input("Introduce el nombre de la nueva empresa: "))
        cif_empresa = str(input("introduce el CIF de la nueva empresa: "))
        localidad_empresa = str(input("introduce la localidad donde se va a encontrar la nueva empresa: "))
        direccion_empresa = str(input("Introduce la direccion de la nueva empresa: "))
        contacto_empresa = str(input("Introduce el nombre de la persona con la que contactará en la empresa: "))
        telefono_empresa = int(input("Introduce el telefono de la empresa: "))
        #creamos la consulta a ejecutar en la BBDD
        consulta_sql = "insert into t_empresa(nombre_empresa, cif_empresa, localidad_empresa, direccion_empresa, contacto_empresa, telefono_empresa) values('{}', '{}', '{}', '{}', '{}', '{}')".format(nombre_empresa, cif_empresa, localidad_empresa, direccion_empresa, contacto_empresa, telefono_empresa)
        self.cursor.execute(consulta_sql)
        #Avisamos al usuario de que se ha añadido correctamente la empresa en la BBDD
        print("Empresa añadida correctamente")
        #Decimos a la BBDD que guarde los cambios para que se muestre la nueva informacion en la BBDD
        self.conn.commit()
        #Cerramos la conexion para que consuma recursos inecesarios
        self.conn.close()
        
        
    #definimos una funcion para mostrar los datos de la tabla t_empresa
    def mostrar_empresas(self):
        sql = "select * from t_empresa"
        self.cursor.execute(sql)
        empresas = self.cursor.fetchall()
        print("Empresas existentes\n")
        for empresa in empresas:
            print("Nombre empresa: ", empresa[1])
    
    #definimos una funcion para mostrar los datos de solo una empresa
    def mostrar_datos_empresa(self, nombre_empresa):
        sql = "select * from t_empresa where nombre_empresa = '{}'".format(nombre_empresa) 
        self.cursor.execute(sql)
        empresas = self.cursor.fetchall()
        print("Los datos de la empresa son los siguientes: \n")
        for empresa in empresas:
            print(".- 1 Nombre empresa: ", empresa[1])
            print(".- 2 CIF empresa: ", empresa[2])
            print(".- 3 Localidad: ", empresa[3])
            print(".- 4 Direccion: ", empresa[4])
            print(".- 5 Persona de Contacto: ", empresa[5])
            print(".- 6 Telefono empresa: ", empresa[6])

            
    #definimos un metodo para actualizador los datos de una empresa
    def actualizar_empresa(self):
        self.mostrar_empresas()
        nombre_empresa_seleccionada = str(input("Introduce el nombre la empresa que quieres modificar: "))
        self.mostrar_datos_empresa(nombre_empresa_seleccionada)
        dato_a_modificar = int(input("¿Qué dato quieres eliminar?(1-6): "))
        if dato_a_modificar == 1:
            nuevo_nombre = str(input("Introduce el nuevo nombre de la empresa: "))
            consulta_sql = "update t_empresa set nombre_empresa = '{}' where  nombre_empresa = '{}'".format(nuevo_nombre, nombre_empresa_seleccionada)
            self.cursor.execute(consulta_sql)
            print("Nombre de la empresa actualizado correctamente")
            self.conn.commit()
            self.conn.close()
        if dato_a_modificar == 2:
            nuevo_cif = str(input("Introduce el nuevo CIF de la empresa: "))
            consulta_sql = "update t_empresa set cif_empresa = '{}' where  nombre_empresa = '{}'".format(nuevo_cif, nombre_empresa_seleccionada)
            self.cursor.execute(consulta_sql)
            print("CIF de la empresa actualizado correctamente")
            self.conn.commit()
            self.conn.close()
        if dato_a_modificar == 3:
            nueva_localidad = str(input("Introduce la nueva localidad de la empresa: "))
            consulta_sql = "update t_empresa set localid_empresa = '{}' where  nombre_empresa = '{}'".format(nueva_localidad, nombre_empresa_seleccionada)
            self.cursor.execute(consulta_sql)
            print("Localidad de la empresa actualizado correctamente")
            self.conn.commit()
            self.conn.close()
        if dato_a_modificar == 4:
            nueva_direccion = str(input("Introduce la nueva direccion de la empresa: "))
            consulta_sql = "update t_empresa set direccion_empresa = '{}' where  nombre_empresa = '{}'".format(nueva_direccion, nombre_empresa_seleccionada)
            self.cursor.execute(consulta_sql)
            print("Direccion de la empresa actualizado correctamente")
            self.conn.commit()
            self.conn.close()
        if dato_a_modificar == 5:
            nuevo_contacto = str(input("Introduce el nombre de la nueva persona de contacto de la empresa: "))
            consulta_sql = "update t_empresa set contacto_empresa = '{}' where  nombre_empresa = '{}'".format(nuevo_contacto, nombre_empresa_seleccionada)
            self.cursor.execute(consulta_sql)
            print("Persona de contacto de la empresa actualizado correctamente")
            self.conn.commit()
            self.conn.close()
        if dato_a_modificar == 6:
            nuevo_telefono= int(input("Introduce el nuevo telefono de la empresa: "))
            consulta_sql = "update t_empresa set telefono_empresa = '{}' where  nombre_empresa = '{}'".format(nuevo_telefono, nombre_empresa_seleccionada)
            self.cursor.execute(consulta_sql)
            print("Telefono de contacto de la empresa actualizado correctamente")
            self.conn.commit()
            self.conn.close()
            
            
         
        
aplicacion = app()

aplicacion.actualizar_empresa()
        
        