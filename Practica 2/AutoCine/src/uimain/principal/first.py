#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase firts.
#* @summary: First será la ventana de inicio en donde se podrán ver las biografias de los programadores, fotos, opcion para salir de la aplicación  y un botón para ingresar a las funcionalidades del AutoCine.
#**

from msilib.schema import Class
import sys
import os
from tkinter import *
from uimain.user.usuario import Usuario

class First(Frame):
    def __init__(self,master,cine):
        self.cine=cine
        super().__init__(master)
        
        frame1=Frame(self,width=100,height=200,bg="#973AF3")  
        frame1.pack(fill=Y, side=LEFT)   # Se hace responsive verticalmente.

        WAndH={"height":200, "width":100}
        frame2=Frame(self, **WAndH) 

        frame3=Frame(frame1,width=100,height=70,bg="#B9B0C2") # Frame del saludo de bienvenida.
        frame3.grid(column = 0, row= 0, padx=3, pady=3,columnspan=4)

        # Se brinda un saludo de bienvenida .
        greetings="Bienvenido al AutoCine. \n Lugar donde podrás transportarte a nuevos mundos y vivir sus historias..."
        self.saludo=Label(frame3,text=greetings,font=('Berlin Sans FB', 18))
        self.saludo.grid(column=0,row=0, padx=3, pady=3)

        # Se crea el frame donde se presentan fotos relacionados al cine.
        frame4=Frame(frame1,width=100,height=100,bg="#B9B0C2")
        frame4.grid(column = 0, row= 1, padx=3, pady=3,columnspan=4)

        # Se muestra la primera foto por defecto.
        self.label1=Label(frame4)
        self.img1=PhotoImage(file=self.getPath('Autocine.png'),width=400,height=400)
        self.label1['image']=self.img1
        self.label1.grid(column=0,row=0,padx=3, pady=3)
        
        # Fotos del cine asignados a los self.img.
        self.img2=PhotoImage(file=self.getPath('Autocine1.png'),width=400,height=400)   
        self.img3=PhotoImage(file=self.getPath('Vikings.png'),width=400,height=400)
        self.img4=PhotoImage(file=self.getPath('Interstellar.png'),width=400,height=400)
        self.img5=PhotoImage(file=self.getPath('Evangelion.png'),width=400,height=400)

        self.label1.bind('<ButtonPress-1>', self.cambioAImg2) # Para cambiar a la segunda imagen.

        # Boton para ir a la ventana principal.
        boton=Button(master=frame4,text="Acceder a ventana de usuario",width=25,height=5,command=self.ventanaUsuario)
        boton.grid(column=0,row=1)

        # Opciones que se tendrán en el menú.
        menubar=Menu(master)
        menu1=Menu(menubar)
        menubar.add_cascade(menu=menu1,label="Opciones")
        menu1.add_command(label="Descripcion",command=self.descripcion) # Para informacion acerca del sistema.
        menu1.add_command(label="Salir",command=master.destroy) # Salir del programa.

        master['menu']=menubar

        #frame donde van las descripciones
        frameHoja=Frame(frame2,height=50,bg="#973AF3")
        self.hojaIns=Label(frameHoja, text="Pulse aqui para conocer a los programadores.\n Luego pulse sobre el texto para cambiar.")
        self.hoja1=Label(frameHoja, text="Soy Jimena Uribe Giraldo y tengo 19 años.\nEstudio Estadistica.\nNací en Apartadó pero vivo en Medellin hace más de 6 años.\nMe gusta cantar y bailar.")
        self.hoja2=Label(frameHoja, text="Soy Daniel Alejandro Giraldo Giraldo y tengo 21 años.\nEstudio Estadistica.\nNací y vivo en Medellin.\nMe gusta el futbol, la musica y los videos juegos.")
        self.hoja3=Label(frameHoja, text="Soy Jhon Ever Gallego Atehortua y tengo 21 años.\nEstudio Ciencias de la Computación.\nNací y vivo en Marinilla.\nMe gusta el deporte, la natación y la musica.")
      
        #Se define un label donde estarán las fotos
        self.hojaFotos1=Fotos(frame2,"1")
        self.hojaFotos2=Fotos(frame2,"2")
        self.hojaFotos3=Fotos(frame2,"3")
        self.hojaFotos4=Fotos(frame2,"4")
        
        frame2.pack()
        frameHoja.pack()
        self.hojaIns.pack()

        #Se define lo que se hará cuando se haga click sobre cada label
        self.hojaIns.bind('<ButtonPress-1>', self.cambioDeInstrucciones)
        self.hoja1.bind('<ButtonPress-1>', self.cambioAHoja2)
        self.hoja2.bind('<ButtonPress-1>', self.cambioAHoja3)
        self.hoja3.bind('<ButtonPress-1>', self.cambioAHoja1)
    
    def getPath(self,txt):
            # Para importar las imagenes
        import os
        import sys
        txt= "uimain\\principal\\" +  txt
        return os.path.join(sys.path[0],txt)

    def cambioDeInstrucciones(self,action):
        #Cambio de hojas
        self.hojaIns.pack_forget()
        self.hoja1.pack()
        self.hojaFotos1.pack()

    def cambioAHoja1(self,action):
        #No recibe nada y se pasa de la hoja 3 a la 1 , cambio de hoja de vida del desarrollador
        self.hoja3.pack_forget()
        self.hojaFotos3.pack_forget()
        self.hoja1.pack()
        self.hojaFotos1.pack()

    def cambioAHoja2(self,action):
        #No recibe nada y se pasa de la hoja 1 a la 2, cambio de hoja de vida del desarrollador
        self.hoja1.pack_forget()
        self.hojaFotos1.pack_forget()
        self.hoja2.pack()
        self.hojaFotos2.pack()

    def cambioAHoja3(self,action):
        #No recibe nada y se pasa de la hoja 2 a la 3, cambio de hoja de vida del desarrollador
        self.hoja2.pack_forget()
        self.hojaFotos2.pack_forget()
        self.hoja3.pack()
        self.hojaFotos3.pack()

    #Metodos para los cambios de imagen
    def cambioAImg1(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img1
        self.label1.grid(column=0,row=0,padx=3,pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg2)

    def cambioAImg2(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img2
        self.label1.grid(column=0,row=0,padx=3,pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg3)

    def cambioAImg3(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img3
        self.label1.grid(column=0,row=0,padx=3,pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg4)

    def cambioAImg4(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img4
        self.label1.grid(column=0,row=0,padx=3,pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg5)

    def cambioAImg5(self,action):
        self.label1.grid_forget()
        self.label1['image']=self.img5
        self.label1.grid(column=0,row=0,padx=3,pady=3)
        self.label1.bind('<ButtonPress-1>', self.cambioAImg1)

    #Metodo para cambiar de ventana
    def ventanaUsuario(self):
            ventana_usuario=Usuario(self.cine)

    #Metodo para cambiar a la descripcion de la app
    def descripcion(self):
            global greetings    #Descripcion del sistema 
            greetings="En esta aplicación usted podrá registrar un cliente, buscar funciones por dia.\nTambien podrán seleccionar su puesto y ver cuales están disponibles u ocupados.\nUsted también podrá añadir y quitar peliculas, añadir salas y agregar funciones."
            self.saludo.config(text = greetings)

class Fotos(Frame):
    def __init__(self,a,hoja):
        super().__init__(a)     #Llama al super frame
        self.fot=[]
        self.hoja1Foto1=[Label(self,width=200, height=200) for i in range(4)]       #Crea 4 labels
        for i in range(1,5):
            fil="hoja"+hoja+"Foto"+str(i)+".png"
            self.fot.append(PhotoImage(file=self.getPath(fil)))     #Se agregan las imagenes a una lista
        i=0
        for r in range(2):
            for c in range(2):
                self.hoja1Foto1[i]["image"]=self.fot[i]     #A cada label le agrega una imagen
                self.hoja1Foto1[i].grid(row=r,column=c)
                i+=1
    
    def getPath(self,txt):      #Para las rutas de las imagenes
        import os
        import sys
        txt= "uimain\\principal\\" +  txt
        return os.path.join(sys.path[0],txt)