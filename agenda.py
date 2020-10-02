#grupo 8 Viper Code
#Axel Soto
#Cesar Diaz
#Alejandro Batista

import sqlite3
import modulo
con = sqlite3.connect("contactos.db")
cursor = con.cursor()
#AGENDA
print("Bienvenido a su agenda")
modulo.menu()

select = int(input("> "))
while select != 6:
    if select == 1: #agregar contacto
        print("Porfavor complete los siguientes campos")
        nombrecontacto = str(input("Nombre: "))
        numerocontacto = int(input("Numero: "))
        correocontacto = str(input("Correo Electronico: "))
        modulo.insertar(nombrecontacto,numerocontacto,correocontacto)             
        print("Desea agregar otro contacto?")
        print("1.Si")
        print("2.No")
        opt = int(input("> "))
        while opt == 1:
          print("Porfavor complete los siguientes campos")
          nombrecontacto = str(input("Nombre: "))
          numerocontacto = int(input("Numero: "))
          correocontacto = str(input("Correo Electronico: "))
          modulo.insertar(nombrecontacto,numerocontacto,correocontacto)             
          print("Desea agregar otro contacto?")
          print("1.Si")
          print("2.No")
          opt = int(input("> "))
                    

        modulo.menu()
        select = int(input("> "))

    if select == 2: #Ver todos los contactos
       
       print("Lista de contactos: ")
       query2 = """ SELECT * FROM contactos; """
       cursor.execute(query2)
       result = cursor.fetchall()
       print(result)
       input("Pulse para continuar ")
       modulo.menu()
       select = int(input("> "))
    
    if select == 3: #buscar contacto
        print("Desea buscar por nombre o ID: ")
        print("1.Nombre")
        print("2.ID")
        sl2 = int(input("> "))
        if sl2 == 1:
           nb = str(input("Inserte nombre: "))
           modulo.busquedanombre(nb)
           input("Pulse para continuar ")
           modulo.menu()
           select = int(input("> "))
        elif sl2 == 2:
            nbb = int(input("Inserte numero: "))
            modulo.contactoid(nbb)
            input("Pulse para continuar ")
            modulo.menu()
            select = int(input("> "))
                        
    if select == 4:#Actualizar contacto
        cursor.execute(query2)
        result = cursor.fetchall()
        print(result)
        idconsult = int(input("Por favor ingrese el id del contacto (numero que antecede al nombre): "))
        nombrecontacto = str(input("Introduzca el nuevo nombre: "))
        numerocontacto = int(input("Introduzca el nuevo numero: "))
        correocontacto = str(input("Indroduzca el nuevo correo electronico: "))        
        modulo.actualizarcontacto(nombrecontacto,numerocontacto,correocontacto,idconsult)
        modulo.busquedanombre(nombrecontacto)

        modulo.menu()
        select = int(input("> "))        

    if select == 5: #Eliminar contactos
        print("Tenga en cuenta que se eliminará para siempre.")
        ("Seguro que desea eliminar algún contacto?")
        security = str(input("Ingrese (si) por seguridad: "))
        if security == "si":
            query2 = """ SELECT * FROM contactos; """
            cursor.execute(query2)
            result = cursor.fetchall()
            print(result)            
            nb = str(input("Inserte id de el contacto a borrar: "))
            modulo.borrar_Cont(nb)
            con.commit()
            print("Contacto borrado con exito.")
            input("Pulse para continuar ")


            modulo.menu()
            select = int(input("> "))    

    if select > 6:
        print("Esta opcion no esta en el menu")
        modulo.menu()
        select = int(input("Ingrese una opcion del menu> "))
  
exit()
