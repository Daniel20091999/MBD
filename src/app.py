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
        
aplicacion = app()

aplicacion.añadir_empresa()
        
        