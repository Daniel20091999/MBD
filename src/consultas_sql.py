from conexion import conexion

def añadir_empresa():
    nombre_empresa = str(input("Introduce el nombre de la nueva empresa: "))
    cif_empresa = str(input("introduce el CIF de la nueva empresa: "))
    localidad_empresa = str(input("introduce la localidad donde se va a encontrar la nueva empresa: "))
    direccion_empresa = str(input("Introduce la direccion de la nueva empresa: "))
    contacto_empresa = str(input("Introduce el nombre de la persona con la que contactará en la empresa: "))
    telefono_empresa = int(input("Introduce el telefono de la empresa"))
                           