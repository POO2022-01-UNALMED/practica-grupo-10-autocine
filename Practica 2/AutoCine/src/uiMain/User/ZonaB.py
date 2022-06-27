#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: En esta clase esta lo del frame principal de la ventana, en donde se mostraran los procesos principales de la aplicacion, donde se pediran los datos y en donde están los botones que permiten enviar la información.
#**

from dataclasses import field
from textwrap import fill
from tkinter import *
from tkinter import messagebox
from uiMain.User.Excepciones.NotChair import NotChair
from uiMain.User.ZonaA import ZonaA
from gestorAplicacion.Autocine.Autocine import Autocine
from gestorAplicacion.Taquilla.Pelicula import Pelicula
from gestorAplicacion.Taquilla.Funcion import Funcion
from uiMain.User.FieldFrame import FieldFrame
from gestorAplicacion.Salas.Sala2D import Sala2D
from gestorAplicacion.Salas.Sala3D import Sala3D
from uiMain.User.FieldFrame import FieldFrame
import uiMain.User.Venta as Venta
from gestorAplicacion.Taquilla.Funcion import Horario
from uiMain.User.Excepciones.NotIn import NotIn
from uiMain.User.Excepciones.NoTipo import NoTipo
from uiMain.User.Excepciones.RangoNoPer import RangoNoPer
from uiMain.User.Excepciones.NoDisp import NoDisp

class ZonaB: 

    def __init__(self, user , autocine):
        self.autocine = autocine
        self.todo = Frame(user, bg = "#FAFAD2") # Este es lo que contiene toda la zona 2.
        self.todo.pack(fill=X)

        self.funciones = {"Venta": self.venta, "Agregar pelicula": self.agregarPelicula, "Eliminar pelicula":self.quitarPelicula, "Agregar una funcion":self.agregarFuncion, "Agregar una sala":self.agregarSala}

        self.titulo_texto = Frame(self.todo)   
        self.titulo_texto.pack()

        self.titulo = Label(self.titulo_texto, font=('Microsoft Himalaya', 32), bg="#FAFAD2", text="¡Bienvenido a la ventana de usuario!")
        self.titulo.pack(fill=X)

        self.texto = Label(self.titulo_texto, font=('Microsoft Himalaya', 24 ), bg="#FAFAD2", text="Por favor selecciona una opción del menú para continuar")
        self.texto.pack(fill=X)

        self.cuerpo = Frame(self.todo, width=800, height=350, bg="#FAFAD2")
        self.cuerpo.pack(fill=X)
        
    # Metodo para devolverse a la ventana inicial de usuario.
    def cambiar(self):
        self.cuerpo.pack_forget()
        self.cuerpo = Frame(self.todo, width=800, height=350, bg="#FAFAD2")

        self.titulo.configure(text="AutoCine")
        self.texto.configure(text="Bienvendio al AutoCine, seleccione lo que desea hacer")

        self.cuerpo.pack()

    # Procesos y consultas.
    # Metodo para la ejecucion de lo respectivo a la venta de tickets.
    def venta(self):
        self.cambiar()
        self.titulo.configure(text="Venta")
        self.texto.configure(text="Permite vender buscando por diferentes peliculas")
        Venta.ventana(self, self.cuerpo, self.autocine) # Se llama a la clase venta pasandole frame y cine como argumentos.
       
    # Metodo para agregar una pelicula.
    def agregarPelicula(self):
        self.cambiar()
        self.titulo.configure(text="Agregar Pelicula")
        self.texto.configure(text="Permite agregar películas a la base de datos")
        nomCriterios="Pelicula"
        criterios = ["Nombre", "Genero", "Duración", "Idioma", "Edad mínima"]
        nomValores = "Información"
        valIniciales = None
        valHabilitados = None  
        agregarPelicula = FieldFrame(nomCriterios, criterios, nomValores, valIniciales, valHabilitados, self.cuerpo)
        agregarPelicula.pack()

        # Metodo para crear un objeto de tipo pelicula.
        def addPeli(action):
            pelicula = Pelicula(agregarPelicula.getValue("Nombre"),
                agregarPelicula.getValue("Genero"),
                int(agregarPelicula.getValue("Duración")),
                agregarPelicula.getValue("Idioma"),
                int(agregarPelicula.getValue("Edad mínima")),
                self.autocine) 
            
            try:
                [int(i)/0 for i in agregarPelicula.getValue("Genero") if i in list("123456789")]        
                [int(i)/0 for i in agregarPelicula.getValue("Idioma") if i in list("123456789")]       
                int(agregarPelicula.getValue("Duración"))
                int(agregarPelicula.getValue("Edad mínima"))
            except:
                raise NoTipo
            
            self.cambiar()    
            messagebox.showinfo(title="Información", message="Pelicula creada con éxito") 

        agregarPelicula.button.bind('<ButtonRelease>',addPeli)

        
    # Metodo para eliminar una pelicula de las que están disponibles en el AutoCine.
    def quitarPelicula(self):
        self.cambiar()
        self.titulo.configure(text="Eliminar pelicula")
        self.texto.configure(text="Permite eliminar películas de la base de datos")
        nomCriterios = "Pelicula"
        criterios = ["Nombre"]
        nomValores = "Información"
        valIniciales = None
        valHabilitados = None     
        quitarPelicula = FieldFrame(nomCriterios, criterios, nomValores, valIniciales, valHabilitados, self.cuerpo)
        quitarPelicula.pack()

        def removePeli(action):
            titles = [i.getNombre() for i in self.autocine.getPeliculas()]      
            try:
                self.autocine.getPeliculas().pop(titles.index(quitarPelicula.getValue("Nombre")))       
            except:                                                                                
                raise NotIn()

            self.cambiar() 
            messagebox.showinfo(title="Información", message="¡Pelicula eliminada del cine con éxito!")  
        quitarPelicula.button.bind('<ButtonRelease>',removePeli)

        peliculasdisponibles = "Peliculas disponibles en el cine:\n"
        for p in self.autocine.getPeliculas():
            peliculasdisponibles += p.getNombre() + "\n"        

        disponibles=Label(self.cuerpo, text=peliculasdisponibles)
        disponibles.pack()


    # Metodo para agregar una funcion manualmente ingresando los valores requeridos.
    def agregarFuncion(self):
        self.cambiar()
        self.titulo.configure(text = "Agregar función")
        self.texto.configure(text = "Permite agregar funciones")
        nomValores = "Información"
        valIniciales = None
        valHabilitados = None
        diames = FieldFrame("Fecha", ["Dia","Mes"], nomValores, valIniciales, valHabilitados, self.cuerpo)     
        diames.pack()
        diames.button.configure(text="Siguiente")

        info=[] # [0]=dia, [1]=mes, [2]=sala, [3]=hora, [4]=pelicula.

        def salasdia(action):      
            info.append(diames.getValue("Dia"))
            info.append(diames.getValue("Mes"))
            
            try:
                int(info[0])       
                int(info[1])
            except:
                info.pop()          
                info.pop()
                raise NoTipo()

            try:
                [i for i in range(1, 13)].index(int(info[1]))    
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            try:
                [i for i in range(1, 32)].index(int(info[0]))      
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            diames.pack_forget()       

            salasdispo = FieldFrame("Sala", ["Numero"], nomValores, valIniciales, valHabilitados, self.cuerpo)      
            salasdispo.pack()
            salasdispo.button.configure(text="Siguente")

            def horariosala(action):       
                info.append(salasdispo.getValue("Numero"))

                try:
                    disp = self.autocine.salasDisponibles(int(info[0]), int(info[1])).copy()      
                    disp.remove(self.autocine.buscarSala(int(info[2])))      
                except:
                    info.pop()
                    raise NotIn()

                salasdispo.pack_forget()       
                disponibles.pack_forget()      

                horariodispo = FieldFrame("Horarios", ["Hora"], nomValores, valIniciales, valHabilitados, self.cuerpo)   
                horariodispo.pack()
                horariodispo.button.configure(text="Siguiente")

                # print(self.autocine.buscarSala(int(info[2])))

                horarioslibres = self.autocine.buscarSala(int(info[2])).verHorarios(int(info[0]),int(info[1]))     
                
                disponibles.configure(text="Horarios disponibles de la sala " + str(info[2])+ ":" + "\n"+horarioslibres)   
                disponibles.pack()

                def peliscine(action):        
                    info.append(horariodispo.getValue("Hora"))

                    try:
                        if info[3] not in self.autocine.buscarSala(int(info[2])).verHorarios(int(info[0]),int(info[1])):
                            x=1/0
                    except:
                        info.pop()
                        raise NotIn()

                    horariodispo.pack_forget()          #
                    disponibles.pack_forget()           

                    pelisdispo = FieldFrame("Titulo", ["Pelicula"], nomValores, valIniciales, valHabilitados, self.cuerpo)
                    pelisdispo.pack()
                    pelisdispo.button.configure(text="Finalizar creación")
                    
                    peliculasdisponibles = ""
                    for p in self.autocine.getPeliculas():              
                        peliculasdisponibles += p.getNombre()+"\n"

                    disponibles.configure(text=peliculasdisponibles)        
                    disponibles.pack()

                    def creacionfinal(action):
                        info.append(pelisdispo.getValue("Pelicula"))
                        titles = [i.getNombre() for i in self.autocine.getPeliculas()]       
                        try:
                            self.autocine.getPeliculas().copy().pop(titles.index(pelisdispo.getValue("Pelicula")))   
                        except:
                            raise NotIn()
                        a = self.autocine.BuscadorPelicula(info[4])
                        Funcion.crearFuncion(int(info[0]), int(info[1]), Horario.getHorario(info[3]), self.autocine.BuscadorPelicula(info[4]), self.autocine.buscarSala(int(info[2])).getNumero(), self.autocine)    

                        self.cambiar()     
                        messagebox.showinfo(title="Información", message="¡Funcion creada con éxito!")   

                    pelisdispo.button.bind("<ButtonRelease>", creacionfinal)     

                horariodispo.button.bind("<ButtonRelease>", peliscine)    

            salasdispo.button.bind("<ButtonRelease>", horariosala)      

            salaslibres = self.autocine.salasDisponibles(int(diames.getValue("Dia")),int(diames.getValue("Mes")))     
            textosalas = "Salas disponibles del dia/mes " + str(diames.getValue("Dia")) + "/" + str(diames.getValue("Mes"))+" :\n"
            for d in salaslibres:
                textosalas += "Sala " + str(d.getNumero()) + "\n"     

            disponibles = Label(self.cuerpo, text=textosalas)      
            disponibles.pack()

        diames.button.bind("<ButtonRelease>",salasdia)      


    # Metodo para la adicion de salas al AutoCine.
    def agregarSala(self):
        self.cambiar()
        self.titulo.configure(text="Agregar una sala")
        self.texto.configure(text="Permite agregar una sala segun su tipo (2D o 3D)")
        checked=IntVar()   
        global nueva        

        def create(action):
            if checked.get() == 2:   

                try:                
                    int(nueva.getValue("Filas"))
                    int(nueva.getValue("Columnas"))
                    int(nueva.getValue("Filas PREFERENCIAL"))
                except:
                    raise NoTipo()

                try:            
                    if int(nueva.getValue("Filas"))<int(nueva.getValue("Filas PREFERENCIAL")):
                        x=1/0
                except:
                    raise RangoNoPer()

                Sala2D(int(nueva.getValue("Filas")), int(nueva.getValue("Columnas")), int(nueva.getValue("Filas PREFERENCIAL")), self.autocine)   
                
            elif checked.get() == 3: 

                try:       
                    int(nueva.getValue("Filas"))
                    int(nueva.getValue("Columnas"))
                    int(nueva.getValue("Gafas disponibles"))
                except:
                    raise NoTipo()

                try:       
                    total = int(nueva.getValue("Filas")) * int(nueva.getValue("Columnas"))
                    if total < int(nueva.getValue("Gafas disponibles")):
                        x=1/0
                except:
                    raise RangoNoPer()
                Sala3D(int(nueva.getValue("Filas")), int(nueva.getValue("Columnas")), int(nueva.getValue("Gafas disponibles")), self.autocine)    

            messagebox.showinfo(title="Información", message="¡Sala creada con éxito!")
            # for i in self.autocine.getSalas():
            #    print(i.getNumero())
            self.cambiar()

        # Metodo para la creacion del fieldframe cuando se selecciona 3D.
        def tres():
            global nueva
            try:
                nueva       #
            except NameError:
                nueva = FieldFrame("Tamaño", ["Filas", "Columnas", "Gafas disponibles"], "Cantidad", None, None, self.cuerpo)
                nueva.pack()

                nueva.button.bind('<ButtonRelease>',create)
            else:
                nueva.pack_forget()   
                nueva = FieldFrame("Tamaño", ["Filas", "Columnas", "Gafas disponibles"], "Cantidad", None, None, self.cuerpo)
                nueva.pack()
                nueva.button.bind('<ButtonRelease>',create)

        # Metodo para la creacion del fieldframe cuando se selecciona 2D.
        def dos():
            global nueva
            try:
                nueva       
            except NameError:
                nueva = FieldFrame("Tamaño", ["Filas", "Columnas", "Filas PRERENCIAL"], "Cantidad", None, None, self.cuerpo)
                nueva.pack()
                nueva.button.bind('<ButtonRelease>',create)
            else:
                nueva.pack_forget()    
                nueva = FieldFrame("Tamaño", ["Filas", "Columnas", "Filas PRERENCIAL"], "Cantidad", None, None, self.cuerpo)
                nueva.pack()
                nueva.button.bind('<ButtonRelease>',create)

        tresd = Radiobutton(self.cuerpo, text="3D", variable=checked, value=3, command=tres)     
        tresd.pack()
        dosd = Radiobutton(self.cuerpo, text="2D", variable=checked, value=2, command=dos)   
        dosd.pack()