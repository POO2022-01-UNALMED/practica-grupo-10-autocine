#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: En esta clase se alberga lo correspondiente a la barra superior donde estan los menus de archivo, procesos y consultas y ayuda.
#**

from tkinter import *

class ZonaA(Menu):
    def __init__(self, user,zona2):
        super().__init__(user)
        self.user = user
        self.zona2 = zona2
        self.archivos()     #Se ejecuta cada uno de los metodos que crean cada menu de la barra
        self.procesos()
        self.ayuda()
        self.user["menu"] = self

## ventanita de proceso
    def procesos(self):
        self.procesos = Menu(self)
        dic = self.zona2.funciones
        for key,value in dic.items():
            self.procesos.add_command(label = key, command = value)
        self.add_cascade(menu = self.procesos, label = "Procesos y Consultas")

## ventanita de archivos
    def archivos(self):
        archivos = Menu(self)
        archivos.add_command(label = "Aplicacion",command=self.aplicacion)
        archivos.add_command(label = "Salir", command = self.user.destroy )
        self.add_cascade(menu = archivos, label = "Archivos")

    #Ventana  de dialogo de aplicacion
    def aplicacion(self):
        ventana_nueva=Toplevel()
        ventana_nueva.title("Aplicacion")
        ventana_nueva.geometry("900x300")
        titulo = Label(ventana_nueva, text="AutoCine",font=("Berlin Sans FB",19),width=200)
        titulo.pack(anchor=NW)
        titulo.config(fg="#009ACD",  font=("Cambria",23),pady=15) 

        informacion=Label(ventana_nueva, text="Esta aplicación fue creada con la finalidad de venta y administración de un AutoCine.\n Para esto se tiene a la disposicion un menú en donde se tendrán las siguientes opciones:",font=("Microsoft Himalaya",19),width=200)
        informacion.pack(anchor=W)

        i2=Label(ventana_nueva, text="1. Archivos: En el que se se podrá escoger entre Aplicación (ver información básica) y Salir para regresar al inicio del programa.\n2. Procesos y consultas: Para realizar funciones como son la venta  de un ticket,\n agregar o eliminar una función, programación de funciones, entre otras.\n3. Ayuda: Se encontrará los desarrolladores de la aplicación.",font=("Microsoft Himalaya",19),width=200)
        i2.pack(anchor=W)

        exit_button = Button(ventana_nueva, text="Salir",font=("Berlin Sans FB",15), command=ventana_nueva.destroy) 
        exit_button.pack(pady=10) 

## ventanita de ayuda
    def ayuda(self):
        ayuda = Menu(self)
        ayuda.add_command(label = "Acerca de",command=self.acerca)
        self.add_cascade(menu = ayuda, label = "Ayuda")

    #Ventana de dialogo de Acerca de 
    def acerca(self):
        ventanacerca=Toplevel()
        ventanacerca.title("Acerca de los POO")
        ventanacerca.geometry("400x550")   
        
        titulo = Label(ventanacerca, text="Acerca del proyecto",font=("Berlin Sans FB",19),width=200)
        titulo.pack(anchor=NW)
        titulo.config(fg="#009ACD",font=("Cambria",23)) 

        tlugar=Label(ventanacerca,text="Materia y Ubicación:",font=("Cambria",17),fg="#EE3B3B",width=400)
        tlugar.pack(anchor=W,pady=10)
        ilugar=Label(ventanacerca,text="Programacion Orientada a Objetos.\nProfesor: Jaime Alberto Guzmán.\n\nUniversidad Nacional de Colombia.\nSede Medellin.\nAño: Junio 2022",font=("Microsoft Himalaya",20),width=400)
        ilugar.pack(anchor=W)

        tinfo=Label(ventanacerca,text="Desarrolladores:",font=("Cambria",17),fg="#EE3B3B",width=400)
        tinfo.pack(anchor=W,pady=10)
        info=Label(ventanacerca,text="\nJimena Uribe Giraldo.\nDaniel Alejandro Giraldo Giraldo.\nJhon Ever Gallego Atehortua.",font=("Microsoft Himalaya",20),width=400)

        info.pack(anchor=W)

        exit_button = Button(ventanacerca, text="Salir",font=("Berlin Sans FB",20), command=ventanacerca.destroy) 
        exit_button.pack(anchor=S,pady=30) 