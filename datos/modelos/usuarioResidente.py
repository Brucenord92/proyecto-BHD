from datos.base_de_datos import BaseDeDatos


def crear_usuario(idUsuario, nombre, apellido, email, tipoDocumento, numeroDeDocumento, telefono, clave, idUnidad, idInmueble):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS_RESIDENTES(ID_USUARIO, NOMBRE, APELLIDO, EMAIL, TIPO_DE_DOCUMENTO, NUMERO_DE_DOCUMENTO, TELEFONO, CLAVE, ID_UNIDAD, ID_INMUEBLE)
        VALUES ('{idUsuario}','{nombre}','{apellido}','{email}','{tipoDocumento}', '{numeroDeDocumento}', '{telefono}', '{clave}', '{idUnidad}', '{idInmueble}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)


def modificar_usuario(id_usuario, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE USUARIOS_RESIDENTES
        SET NOMBRE='{datos_usuario["nombre"]}', APELLIDO='{datos_usuario["apellido"]}', EMAIL='{datos_usuario["email"]}', TIPO_DE_DOCUMENTO='{datos_usuario["tipoDocumento"]}', NUMERO_DE_DOCUMENTO='{datos_usuario["numeroDeDocumento"]}', TELEFONO='{datos_usuario["telefono"]}' CLAVE='{datos_usuario["clave"]}', 
        WHERE ID_USUARIO='{id_usuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT id, nombre, apellido, email, tipoDeDocumento, nuemeroDeDocumento, telefono, idunidad, idinmueble  
        FROM USUARIOS_RESIDENTES
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "nombre": registro[1],
             "apellido": registro[2],
             "email": registro[3],
             "tipoDeDocumento": registro[4],
             "nuemeroDeDocumento": registro[5],
             "telefono": registro[6],
             "idunidad": registro[8],
             "idinmueble": registro[9]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]



def borrar_usuario(id_usuario):
    obtener_usuarios_sql = f"""
        DELETE
        FROM USUARIOS_RESIDENTES
        WHERE ID_USUARIO = {id_usuario}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuarios_sql)

