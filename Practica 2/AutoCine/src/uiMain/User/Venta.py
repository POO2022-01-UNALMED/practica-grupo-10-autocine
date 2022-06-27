#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: Funcion encargada para la ventana de venta de tickets, en la cual podemos evidenciar la inscripción de clientes al sistema.
#**

from ast import NotIn
from tkinter import *
from uiMain.User.FieldFrame import FieldFrame
from gestionAplicacion.Persona.Cliente import Cliente
from gestionAplicacion.Autocine.Autocine import Autocine
from gestionAplicacion.Taquilla.Funcion import Funcion
from gestionAplicacion.Taquilla.Pelicula import Pelicula
from gestionAplicacion.Taquilla.Horario import Horario
from gestionAplicacion.Salas.Sala2D import Sala2D
from uiMain.User.Excepciones.NoTipo import NoTipo
from uiMain.User.Excepciones.NotIn import NotIn
from uiMain.User.Excepciones.NotChair import NotChair


def ventana(variable, window, autocine):
    venta = Frame()                 
    cliente = None                    

    frame = FieldFrame("Cedula Cliente", ["Cedula"], "Ingrese Dato", None, None, window)

    def vender(existente):
        nonlocal frame
        nonlocal venta
        nonlocal cliente
        nonlocal autocine

        boton_recomendada = None
        boton_funcion = None
        boton_pelicula = None
        label = None

        frame.pack_forget()
        frame = Frame(window)
        frame.pack()
        venta = Frame(frame)
        venta.pack()
        texto = Label(venta, text="Busqueda por : ")
        nueva = None

        def mostrar_puestos(funcion):
            nonlocal nueva
            nonlocal cliente
            nonlocal autocine
            nonlocal label

            puestos = funcion.verDisponibilidad()        #esto es una lista de tuplas con (disponibilidad: boolean, y número)
            filas = funcion.getSala().getFilas()        #columnas para más adelante
            columnas = funcion.getSala().getColumnas()  #columnas para más adelante
            nueva.pack_forget()
            label.pack_forget()
            label = Label(venta, text="Seleccione la silla que desea")
            label.pack()
            nueva = Frame(venta)
            nueva.pack()

            def vender_ticket(numero):
                nonlocal nueva
                funcion.getTickets()[numero].calcularPrecioDefinitivo(cliente)
                funcion.VentaTicket(funcion.getTicket()[numero], cliente)
                
                nueva.pack_forget()
                nueva = FieldFrame("Se ha vendido el boleto", [], "numero " + str(numero + 1), [], None, venta)
                precio = Label(venta, text="El precio es " + str(funcion.getTickets()[numero].getPrecioTotal()))
                
                nueva.pack()
                precio.pack()
                nueva.button.bind('<ButtonRelease>', lambda x=variable: variable.cambiar())
                descuento_aplicado = Label(venta, text="Descuento aplicado \n" + str((cliente.getDescuento())*funcion.getTickets()[numero].calcularPrecio()))
                descuento_aplicado.pack()

            def Hola():
                raise NotChair
            num = 0
            botones = []  
            funciones = []  
            for i in range(filas):          
                for j in range(columnas):   
                    if (num < funcion.getSala().getCantidadPuestos()): 
                        if (puestos[num][0] == True):                   
                            funciones.append(lambda: vender_ticket(num))
                            a = Button(master=nueva, text=str(puestos[num][1]), height=2, width=4,
                                       command=lambda x=(columnas * i + j): vender_ticket(x))
                        else:                                         
                            a = Button(master=nueva, text=str(puestos[num][1]), height=2, width=4, bg="blue", command=Hola)
                        botones.append(a)
                        botones[num].grid(column=j, row=i, padx=3, pady=3)
                        num += 1

        def mostrar_funciones(funciones):
            nonlocal nueva
            nonlocal texto
            nonlocal cliente
            nonlocal autocine
            nonlocal label
            try:
                nueva.pack_forget()    
                label.pack_forget()     
            except AttributeError:
                pass
            
            nueva = FieldFrame("Mostrar", ["Número de Funcion"], "Ingrese Dato", None, None, venta)
            nueva.pack()                                                                            
            texto.pack_forget()

            def obtenerFuncion():
                nonlocal nueva
                numero = nueva.getValue("Número de Funcion") 
                try:
                    autocine.BuscadorFuncion(numero).getHorario() 
                except: 
                    raise NotIn                               

                mostrar_puestos(autocine.BuscadorFuncion(numero))

            nueva.button.bind('<ButtonRelease>', lambda x: obtenerFuncion())      
            label = Label(venta, text=str(Funcion.formatearFunciones(funciones)))
            label.pack()
            try:
                boton_recomendada.pack_forget()
                boton_funcion.pack_forget()
            except AttributeError:
                boton_funcion.pack_forget()

        def llamar_funcion():
            nonlocal label
            nonlocal nueva
            nonlocal autocine

            label.pack_forget()
            funcion = FieldFrame("Fecha", ["Dia", "Mes"], "Ingrese datos", None, None, venta)
            funcion.pack()
            try:
                nueva.pack_forget()                                                          
            except AttributeError:
                pass
            nueva = funcion                                                                   
            funciones = None

            def funcionesxfuncion():
                nonlocal funciones

                funciones = autocine.verFuncion(int(funcion.getValue("Dia")), int(funcion.getValue("Mes")))
                mostrar_funciones(funciones)

            nueva.button.bind('<ButtonRelease>', lambda x: funcionesxfuncion())

        if (existente):                         
            nombre = cliente.getNombre()
            puesto = cliente.getOcupacion()

            label = Label(venta, text=str(nombre) + " / " +  str(puesto))                                                
            label.pack()
            texto.pack()
            boton_recomendada = Radiobutton(venta, text="Recomendada", value=1, command=lambda: mostrar_funciones(autocine.verFuncion(cliente)))  
            boton_recomendada.pack()                                                                    
            boton_funcion = Radiobutton(venta, text="Funcion", value=3, command=llamar_funcion)         
            boton_funcion.pack()
        else:                                   
            nombre = cliente.getNombre()
            puesto = cliente.getOcupacion()

            label = Label(venta, text=str(nombre) + " / " + str(puesto))
            label.pack()

            boton_funcion = Radiobutton(venta, text="Funcion", value=3, command=llamar_funcion)
            boton_funcion.pack()

    def cedula(numero):
        nonlocal autocine
        nonlocal frame
        nonlocal cliente
        try:                    
            int(numero)
        except:
            raise NoTipo

        if (autocine.buscadorCliente(numero) == None):  
            frame.pack_forget()
            frame = FieldFrame("Inscripción", ["Cedula referido", "Nombre", "Edad", "Ocupacion"], "ingrese datos", None, None, window)
            frame.pack()

            def crearCliente():
                nonlocal cliente
                if (int(frame.getValue("Cedula referido")) != 0):                                               
                    try:
                        [int(i) / 0 for i in frame.getValue("Nombre") if i in list("123456789")]
                        [int(i) / 0 for i in frame.getValue("Ocupacion") if i in list("123456789")]
                        int(frame.getValue("Edad"))
                        autocine.buscadorCliente(int(frame.getValue("Cedula referido"))).getDescuento()
                    except:
                        raise NoTipo

                    cliente = Cliente(numero, str(frame.getValue("Nombre")), int(frame.getValue("Edad")), frame.getValue("Ocupacion"), autocine)
                    cliente.referidos()                                                                 
                                                                                                        
                    vender(False)
                else:                                                                                   
                    try:                                                                                
                        [int(i) / 0 for i in frame.getValue("Nombre") if i in list("123456789")]       
                        [int(i) / 0 for i in frame.getValue("Ocupacion") if i in list("123456789")]
                        int(frame.getValue("Edad"))

                    except:
                        raise NoTipo

                    cliente = Cliente(numero, str(frame.getValue("Nombre")), int(frame.getValue("Edad")), frame.getValue("Ocupacion"), autocine)
                    vender(False)
            frame.button.bind('<ButtonRelease>', lambda x: crearCliente())
        else:
            cliente = autocine.buscadorCliente(numero)
            vender(True)

    frame.pack()
    frame.button.bind('<ButtonRelease>', lambda x: cedula(frame.getValue("Cedula")))