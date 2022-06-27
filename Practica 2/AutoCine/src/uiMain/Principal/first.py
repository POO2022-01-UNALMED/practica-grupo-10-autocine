#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: First será la ventana de inicio en donde se podrán ver las biografias de los programadores, fotos, opcion para salir de la aplicación  y un botón para ingresar a las funcionalidades del AutoCine.
#**

from msilib.schema import Class
import sys
import os
from tkinter import *
from uiMain.User.Usuario import Usuario


class First(Frame):
    def __init__(self, master, autocine):
        self.autocine = autocine
        super().__init__(master)
        
        frame1=Frame(self, width=100, height=200, bg="#FFA07A") # Frame naranja. 
        frame1.pack(fill=Y, side=LEFT)   # Se hace responsive verticalmente.

        WAndH={"height":200, "width":100}
        frame2=Frame(self, **WAndH) 

        frame3=Frame(frame1, width=100, height=70, bg="yellow") # Frame del saludo de bienvenida.
        frame3.grid(column = 0, row= 0, padx=3, pady=3, columnspan=4)

        # Se brinda un saludo de bienvenida.
        greetings="Bienvenido al AutoCine, "
        self.saludo=Label(frame3, text=greetings, font=('Microsoft Himalaya', 18))
        self.saludo.grid(column=0, row=0, padx=3, pady=3)

        # Se crea el frame donde se presentan fotos relacionados al cine.
        frame4=Frame(frame1, width=100, height=130, bg="#FF6A6A")  # El que es rojo.
        frame4.grid(column=0, row= 1, padx=3, pady=3, columnspan=4)

        # Se muestra la primera foto por defecto.
        self.label1=Label(frame4)
        self.img1=PhotoImage(file=self.getPath('cinepng.png'), width=400, height=400)
        self.label1['image']=self.img1
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        
        #Fotos del cine asignados a los self.img
        self.img2=PhotoImage(file=self.getPath('cinebahia.png'), width=400, height=400)   
        self.img3=PhotoImage(file=self.getPath('cine1.png'), width=400, height=400)
        self.img4=PhotoImage(file=self.getPath('cine2.png'), width=400, height=400)
        self.img5=PhotoImage(file=self.getPath('cine4.png'), width=400, height=400)

        self.label1.bind('<ButtonPress-1>', self.cambioAImg2) # Para cambiar a la segunda imagen.

        # Boton para ir a la ventana principal.
        boton=Button(master=frame4, text="Acceder a ventana de usuario", width=25, height=5, command=self.ventanaUsuario)
        boton.grid(column=0, row=1)


        # Opciones que se tendrán en el menú.
        menubar=Menu(master)
        menu1=Menu(menubar)
        menubar.add_cascade(menu=menu1, label="Opciones")
        menu1.add_command(label="Descripcion", command=self.descripcion) # Para informacion acerca del sistema.
        menu1.add_command(label="Salir", command=master.destroy) # Salir del programa.

        master['menu']=menubar

        # Frame donde van las descripciones.
        frameParte=Frame(frame2, height=50, bg="gray")
        self.parteIns=Label(frameParte, text="Pulse sobre cada \n text para cambiar")
        self.parte1=Label(frameParte, text="Soy Jimena Uribe Giraldo, tengo 19 años y soy de Estadística")
        self.parte2=Label(frameParte, text="Soy Daniel Alejandro Giraldo Giraldo, tengo ")
        self.parte3=Label(frameParte, text="Soy Jhon Ever Gallego Atehortua, tengo ")
        
        # Se define un label donde estarán las fotos.
        self.parteFotos1=Fotos(frame2,"1")
        self.parteFotos2=Fotos(frame2,"2")
        self.parteFotos3=Fotos(frame2,"3")

        frame2.pack()
        frameParte.pack()
        self.parteIns.pack()

        # Se define lo que se hará cuando se haga click sobre cada label.
        self.parteIns.bind('<ButtonPress-1>', self.cambioDeInstrucciones)
        self.parte1.bind('<ButtonPress-1>', self.cambioAParte2)
        self.parte2.bind('<ButtonPress-1>', self.cambioAParte3)
        self.parte3.bind('<ButtonPress-1>', self.cambioAParte1)
    
    
    def getPath(self,txt):
            # Para importar las imagenes.
        import os
        import sys
        txt= "uiMain\\Principal\\" +  txt
        return os.path.join(sys.path[0],txt)

    def cambioDeInstrucciones(self,action):
        # Cambio de hojas.

        self.parteIns.pack_forget()
        self.parte1.pack()
        self.parteFotos1.pack()

    def cambioAParte1(self,action):
        # No recibe nada y se pasa de la hoja 3 a la 1 , cambio de hoja de vida del desarrollador.
    
        self.parte3.pack_forget()
        self.parteFotos3.pack_forget()
        self.parte1.pack()
        self.parteFotos1.pack()

    def cambioAParte2(self,action):
        #No recibe nada y se pasa de la hoja 1 a la 2, cambio de hoja de vida del desarrollador

        self.parte1.pack_forget()
        self.parteFotos1.pack_forget()
        self.parte2.pack()
        self.parteFotos2.pack()

    def cambioAParte3(self,action):
        #No recibe nada y se pasa de la hoja 2 a la 3, cambio de hoja de vida del desarrollador

        self.parte2.pack_forget()
        self.parteFotos2.pack_forget()
        self.parte3.pack()
        self.parteFotos3.pack()

    # Metodos para los cambios de imagen.
    def cambioAImg1(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img1
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg2)


    def cambioAImg2(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img2
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg3)


    def cambioAImg3(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img3
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg4)


    def cambioAImg4(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img4
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg5)


    def cambioAImg5(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img5
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg1)

    # Metodo para cambiar de ventana.
    def ventanaUsuario(self):
            ventana_usuario=Usuario(self.autocine)

    # Metodo para cambiar a la descripcion de la app.
    def descripcion(self):
            global greetings # Descripcion del sistema.
            greetings="En esta aplicación usted podrá registrar un cliente si este es nuevo\nrecomendarle peliculas a clientes viejos o buscar funciones por dia\ntambien podrán seleccionar su asiento y ver cuales estan ocupados.\nUsted también podrá añadir y quitar peliculas, añadir salas\n agregar funciones automatica o manualmente \ny rifar boletos entre los clientes mas fieles"
            self.saludo.config(text = greetings)

class Fotos(Frame):
    def __init__(self, a, parte):
        super().__init__(a)     # Llama al super frame.
        self.fot=[]
        self.parte1Foto1=[Label(self,width=200, height=200) for i in range(4)]       #Crea 4 labels
        for i in range(1,5):
            fil="parte" + parte + "Foto" + str(i) + ".png"
            self.fot.append(PhotoImage(file=self.getPath(fil)))     #Se agregan las imagenes a una lista
        i=0
        for r in range(2):
            for c in range(2):
                self.parte1Foto1[i]["image"]=self.fot[i]     #A cada label le agrega una imagen
                self.parte1Foto1[i].grid(row=r, column=c)
                i+=1
    
    def getPath(self,txt):      # Para las rutas de las imagenes.
        import os
        import sys
        txt= "uimain\\principal\\" +  txt
        return os.path.join(sys.path[0],txt)
