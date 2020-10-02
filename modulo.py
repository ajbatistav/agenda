import sqlite3
con = sqlite3.connect("contactos.db")
cursor = con.cursor()

def insertar (nombrecontacto,numerocontacto,correocontacto):
   query1 = """ INSERT INTO contactos(nombrecontacto, numerocontacto, correocontacto) VALUES (?,?,?); """
   info_tupla = (nombrecontacto,numerocontacto,correocontacto)
   cursor.execute(query1, info_tupla)
   con.commit()
   print("Datos Guardados")


def busquedanombre(nombrecontacto):
    query3 = """ SELECT *  FROM contactos WHERE nombrecontacto = ? """
    cursor.execute(query3, (nombrecontacto,))
    res = cursor.fetchall()
    print(res)

def vercontactos():
    query2 = """ SELECT * FROM contactos; """
    cursor.execute(query2)
    result = cursor.fetchall()
    print(result)

def contactoid(contactoid):
    query4 = """ SELECT * FROM contactos WHERE contactoid = ? """
    cursor.execute(query4, (contactoid,))
    res = cursor.fetchall()
    print(res)

def actualizarcontacto(nombrecontacto,numerocontacto,correocontacto,contactoid):
   query6 = """ UPDATE  contactos SET nombrecontacto = ?, numerocontacto = ?, correocontacto = ? where contactoid = ?; """
   cursor.execute(query6,[nombrecontacto,numerocontacto,correocontacto,contactoid])
   con.commit()

def menu():
    print("Que desea hacer: ")
    print("1.Agregar nuevo contacto.")
    print("2.Ver todos los contactos.")
    print("3.Buscar contacto por nombre o numero de telefono.")
    print("4.Actualizar un contacto.")
    print("5.Eliminar un contacto.")
    print("6.Salir.")

def borrar_Cont(nombrecontacto):
    query4 ="""DELETE FROM contactos WHERE contactoid = ? ;"""
    cursor.execute(query4, (contactoid,))
    con.commit()
    