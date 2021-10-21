import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('../../BHD_Database13.db')
        conexion.execute('PRAGMA foreign_keys = ON')
        print("conexion establecida")
        return conexion
    except Error:
        print(Error)


def crearTabla(conexion):
    conexion.execute(
        'CREATE TABLE INMUEBLES(ID_INMUEBLE TEXT PRIMARY KEY, NOMBRE_DE_INMUEBLE TEXT NOT NULL UNIQUE, DIRECCION TEXT NOT NULL, CANTIDAD_DE_UNIDADES INTEGER NOT NULL, SERVICIOS TEXT, UNIDADES_ACTIVAS INTEGER NOT NULL)')
        #'CREATE TABLE INMUEBLES(ID_INMUEBLE TEXT PRIMARY KEY, NOMBRE_DE_INMUEBLE TEXT NOT NULL UNIQUE, DIRECCION TEXT NOT NULL, CANTIDAD_DE_UNIDADES INTEGER NOT NULL, SERVICIOS TEXT,ID_COCHERA TEXT, REGLAMENTO_Y_ACTAS TEXT, UNIDADES_ACTIVAS INTEGER NOT NULL, ID_AMENITIE TEXT, FOREIGN KEY(ID_AMENITIE) REFERENCES AMENITIES(ID_AMENITIE), FOREIGN KEY(ID_COCHERA) REFERENCES COCHERAS(ID_COCHERA))')
    conexion.execute(
        'CREATE TABLE UNIDADES(ID_UNIDAD TEXT PRIMARY KEY, NUMERO_DE_UNIDAD INTEGER NOT NULL UNIQUE, GASTOS_DE_UNIDAD INTEGER NOT NULL, ID_INMUEBLE TEXT NOT NULL, FOREIGN KEY(ID_INMUEBLE) REFERENCES INMUEBLES(ID_INMUEBLE))')
        #'CREATE TABLE UNIDADES(ID_UNIDAD TEXT PRIMARY KEY, NUMERO_DE_UNIDAD INTEGER NOT NULL UNIQUE, USUARIOS_DE_UNIDAD TEXT NOT NULL, GASTOS_DE_UNIDAD INTEGER NOT NULL, ID_INMUEBLE TEXT NOT NULL, FOREIGN KEY(ID_INMUEBLE) REFERENCES INMUEBLES(ID_INMUEBLE))')
    conexion.execute(
        'CREATE TABLE USUARIOS_RESIDENTES(ID_USUARIO TEXT PRIMARY KEY, NOMBRE TEXT NOT NULL, APELLIDO TEXT NOT NULL, EMAIL TEXT NOT NULL UNIQUE, TIPO_DE_DOCUMENTO TEXT NOT NULL, NUMERO_DE_DOCUMENTO TEXT NOT NULL UNIQUE, TELEFONO INTEGER, CLAVE TEXT NOT NULL, ID_UNIDAD TEXT, ID_INMUEBLE TEXT, FOREIGN KEY(ID_INMUEBLE) REFERENCES INMUEBLES(ID_INMUEBLE) ,FOREIGN KEY(ID_UNIDAD) REFERENCES UNIDADES(ID_UNIDAD))')
    # USUARIO_DIRECTIVA INTEGER, PROPIETARIO INTEGER, ID_COCHERA TEXT / FOREIGN KEY(ID_COCHERA) REFERENCES COCHERAS(ID_COCHERA)
    conexion.execute(
        'CREATE TABLE SERVICIOS(ID_SERVICIO TEXT PRIMARY KEY, TIPO_DE_SERVICIO TEXT NOT NULL, ABONADO INTEGER, CANTIDAD_DE_PROVEEDORES TEXT)')
    conexion.execute(
        'CREATE TABLE PROVEEDORES(ID_PROVEEDOR TEXT PRIMARY KEY, NOMBRE_DE_EMPRESA TEXT NOT NULL, NOMBRE_FANTASIA TEXT NOT NULL, RUT INTEGER NOT NULL UNIQUE, DIRECCION TEXT NOT NULL, TELEFONO_CONTACTO INTEGER NOT NULL, EMAIL TEXT NOT NULL UNIQUE)')
    conexion.execute(
        'CREATE TABLE RECLAMOS(ID_RECLAMO TEXT PRIMARY KEY, DESCRIPCION TEXT NOT NULL, ID_INMUEBLE TEXT NOT NULL, ID_UNIDAD TEXT NOT NULL, ID_USUARIO TEXT NOT NULL, ID_SERVICIO, FECHA DATETIME, ESTADO TEXT NOT NULL, FOREIGN KEY(ID_INMUEBLE) REFERENCES INMUEBLES(ID_INMUEBLE), FOREIGN KEY(ID_UNIDAD) REFERENCES UNIDADES(ID_UNIDAD), FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS_RESIDENTES(ID_USUARIO),FOREIGN KEY(ID_SERVICIO) REFERENCES SERVICIOS(ID_SERVICIOS))')
   # conexion.execute(
    #    'CREATE TABLE SEGUIMIENTO_RECLAMOS(ID_SEGUIMIENTO_RECLAMO INTEGER PRIMARY KEY AUTOINCREMENT, ESTADO TEXT NOT NULL DEFAULT PENDIENTE, COMENTARIOS TEXT NOT NULL, FECHA_Y_HORA TEXT NOT NULL, ID_RECLAMO TEXT NOT NULL, FOREIGN KEY(ID_RECLAMO) REFERENCES RECLAMOS(ID_RECLAMO))')
    conexion.execute(
        'CREATE TABLE AMENITIES(ID_AMENITIE TEXT PRIMARY KEY, TIPO TEXT, ID_RESERVA TEXT, ESTADO INTEGER NOT NULL, FOREIGN KEY(ID_RESERVA) REFERENCES AGENDA_AMENITIES(ID_RESERVA))')
    conexion.execute(
        'CREATE TABLE ADMINISTRACIONES(ID_ADMINISTRACION TEXT PRIMARY KEY, NOMBRE_ADMINISTRACION TEXT NOT NULL UNIQUE, EMAIL TEXT NOT NULL UNIQUE, TELEFONO INTEGER NOT NULL, INMUEBLES TEXT NOT NULL, LISTA_DE_USUARIOS_ADMINISTRADORES TEXT NOT NULL, LISTA_DE_PROVEEDORES TEXT)')
    conexion.execute(
        'CREATE TABLE AGENDA_AMENITIES(ID_RESERVA TEXT PRIMARY KEY, FECHA_HORA DATETIME NOT NULL UNIQUE, ID_USUARIO TEXT, FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS_RESIDENTES(ID_USUARIO))')
    conexion.execute(
        'CREATE TABLE MULTAS_AMENITIES(ID_MULTA TEXT PRIMARY KEY, DETALLE TEXT NOT NULL, IMPORTE INTEGER NOT NULL, ID_RESERVA TEXT NOT NULL, FOREIGN KEY(ID_RESERVA) REFERENCES AGENDA_AMENITIES(ID_RESERVA))')
    conexion.execute(
        'CREATE TABLE GASTOS_UNIDADES(ID_GASTOS TEXT PRIMARY KEY, CONCEPTO TEXT NOT NULL, IMPORTE INTEGER NOT NULL, ID_USUARIO TEXT, ID_UNIDAD TEXT NOT NULL, FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS_RESIDENTES(ID_USUARIO), FOREIGN KEY(ID_UNIDAD) REFERENCES UNIDADES(ID_UNIDAD))')
    conexion.execute(
        'CREATE TABLE COCHERAS(ID_COCHERA TEXT PRIMARY KEY, LOCALIZACION TEXT NOT NULL UNIQUE, SECTOR TEXT NOT NULL, DISPONIBILIDAD TEXT NOT NULL, DESCRIPCION TEXT, ID_INMUEBLE TEXT, ID_USUARIO TEXT, FOREIGN KEY (ID_INMUEBLE) REFERENCES INMUEBLES(ID_INMUEBLE), FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS_RESIDENTES(ID_USUARIO))')
    conexion.execute(
        'CREATE TABLE SESIONES(ID INTEGER PRIMARY KEY, ID_USUARIO TEXT, FECHA_HORA TEXT, FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS_RESIDENTES(ID_USUARIO))')



def insertarRegistro(conexion):

    conexion.execute("INSERT INTO INMUEBLES (ID_INMUEBLE, NOMBRE_DE_INMUEBLE, DIRECCION, CANTIDAD_DE_UNIDADES, SERVICIOS, UNIDADES_ACTIVAS) VALUES('EDA123MVDUY', 'Edificio A', '18 de julio 1234', 45, 'Lista de servicios', 33)")
    conexion.commit()
    conexion.execute("INSERT INTO UNIDADES (ID_UNIDAD, NUMERO_DE_UNIDAD, GASTOS_DE_UNIDAD, ID_INMUEBLE) VALUES('EDA123A103', 'A103', 1500, 'EDA123MVDUY')")
    conexion.commit()
    conexion.execute("INSERT INTO SERVICIOS(ID_SERVICIO, TIPO_DE_SERVICIO, ABONADO, CANTIDAD_DE_PROVEEDORES) VALUES('ELEC100', 'ELECTRICISTA', 1, 'JUAN RAYO')")
    conexion.commit()
    conexion.execute("INSERT INTO SERVICIOS(ID_SERVICIO, TIPO_DE_SERVICIO, ABONADO, CANTIDAD_DE_PROVEEDORES) VALUES('SANI300', 'SANITARIO', 1, 'PEDRO AGUA')")
    conexion.commit()
    conexion.execute("INSERT INTO SERVICIOS(ID_SERVICIO, TIPO_DE_SERVICIO, ABONADO, CANTIDAD_DE_PROVEEDORES) VALUES('JARD200', 'JARDINERO', 1, 'MATEO FLORES')")
    conexion.commit()


con = conectar()
crearTabla(con)
insertarRegistro(con)
con.close()
