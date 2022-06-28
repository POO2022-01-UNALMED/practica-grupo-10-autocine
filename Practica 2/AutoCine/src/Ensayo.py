from uiMain.Principal.first import First
from tkinter import *
from gestorAplicacion.Autocine.Autocine import Autocine
from gestorAplicacion.Taquilla.Pelicula import Pelicula
from gestorAplicacion.Persona.Cliente import Cliente
from gestorAplicacion.Salas.Sala3D import Sala3D
from gestorAplicacion.Salas.Sala2D import Sala2D
from gestorAplicacion.Taquilla.Funcion import Funcion
from gestorAplicacion.Taquilla.Funcion import Horario
from uiMain.User.Excepciones.NotIn import NotIn
from uiMain.User.Excepciones.NoTipo import NoTipo
from uiMain.User.Excepciones.RangoNoPer import RangoNoPer
import pickle

#entana=Usuario()
"""autocine = Autocine("Autocine")
rey_leon =  Pelicula("Rey Leon", "Animada", 2, "Espanol", 0, autocine)
avengers =  Pelicula("Avengers", "Accion", 2, "Espanol", 12, autocine)
naranja =  Pelicula("La Naranja Mecanica", "Clasica", 2, "Espanol", 18, autocine)
resplandor =  Pelicula("El Resplandor", "Terror", 2, "Espanol", 15, autocine)
toystory =  Pelicula("Toy Story", "Animada", 2, "Espanol", 8, autocine)
harrypotter =  Pelicula("Harry Potter", "Fantasia", 2, "Espanol", 10, autocine)
avatar =  Pelicula("Avatar", "Fantasia", 2, "Espanol", 15, autocine)
pianista =  Pelicula("El Pianista", "Drama", 2, "Espanol", 18, autocine)

cliente1 =  Cliente(1001, "Pedro", 15, "Estudiante", autocine)
cliente2 =  Cliente(1002, "Daniel Santiago", 20, "Estudiante", autocine)
cliente3 =  Cliente(1003, "Daniel Daza", 20, "Estudiante", autocine)
cliente4 =  Cliente(1004, "Marlon Calle", 20, "Estudiante", autocine)
cliente5 =  Cliente(1005, "Jose Daniel Bustamante", 21, "Estudiante", autocine)
cliente6 =  Cliente(1006, "Jaime Guzman", 40, "Trabajador", autocine)
cliente7 =  Cliente(1007, "Luisa Guarin", 30, "Trabajadora", autocine)
cliente8 =  Cliente(1008, "Pedro Gomez", 15, "Estudiante", autocine)
cliente9 =  Cliente(1009, "Juan Esteban", 15, "Estudiante", autocine)
cliente10 =  Cliente(1010, "Alejandra", 20, "Trabajadora", autocine)
cliente11 =  Cliente(1011, "Sofia", 25, "Estudiante", autocine)
cliente12 =  Cliente(1012, "Jose Daniel Bustamante", 21, "Trabajadora", autocine)
cliente13 =  Cliente(1013, "Luisa Guarin", 30, "Trabajadora", autocine)

sala1 =  Sala2D(7, 8, 2,autocine)
sala2 =  Sala2D(9, 8, 2,autocine)
sala3 =  Sala3D(9, 9, 50,autocine)
sala4 =  Sala3D(8, 9, 36,autocine)


funcion_1 = Funcion.crearFuncion(17, 12, Horario.UNO, rey_leon, 1, autocine)
funcion_2 = Funcion.crearFuncion(17, 12, Horario.DOS, naranja, 1,autocine)
funcion_3 = Funcion.crearFuncion(17, 12, Horario.TRES, naranja, 1, autocine)
funcion_11 = Funcion.crearFuncion(17, 12, Horario.CUATRO, rey_leon, 1, autocine)
funcion_22 = Funcion.crearFuncion(17, 12, Horario.CINCO, naranja, 1, autocine)
funcion_33 = Funcion.crearFuncion(17, 12, Horario.SEIS, naranja, 1, autocine)
funcion_4 = Funcion.crearFuncion(17, 12, Horario.CINCO, resplandor, 3, autocine)
funcion_5 = Funcion.crearFuncion(17, 12, Horario.SEIS, avengers, 3, autocine)
funcion_7 = Funcion.crearFuncion(16, 12, Horario.UNO, toystory, 4, autocine)
funcion_8 = Funcion.crearFuncion(17, 12, Horario.CUATRO, toystory, 2, autocine)
funcion_9 = Funcion.crearFuncion(16, 12, Horario.TRES, toystory, 2, autocine)

funcion_1.VentaTicket(funcion_1.getBoletos()[0],cliente1)
funcion_1.VentaTicket(funcion_1.getBoletos()[2],cliente1)
funcion_2.VentaTicket(funcion_2.getBoletos()[3],cliente2)
funcion_2.VentaTicket(funcion_2.getBoletos()[4],cliente2)
funcion_1.VentaTicket(funcion_1.getBoletos()[5],cliente2)
funcion_1.VentaTicket(funcion_1.getBoletos()[6],cliente3)
funcion_2.VentaTicket(funcion_2.getBoletos()[7],cliente3)
funcion_2.VentaTicket(funcion_2.getBoletos()[8],cliente3)
funcion_1.VentaTicket(funcion_1.getBoletos()[9],cliente4)
funcion_1.VentaTicket(funcion_1.getBoletos()[25], cliente5)
funcion_2.VentaTicket(funcion_2.getBoletos()[15], cliente6)
funcion_2.VentaTicket(funcion_2.getBoletos()[17], cliente5)


funcion_4.VentaTicket(funcion_4.getBoletos()[0], cliente7)
funcion_3.VentaTicketfuncion_3.getBoletos()[45], cliente8)
funcion_3.VentaTicket(funcion_3.getBoletos()[3],cliente9)
funcion_3.VentaTicket(funcion_3.getBoletos()[5],cliente10)
funcion_3.VentaTicket(funcion_3.getBoletos()[6],cliente11)
funcion_3.VentaTicket(funcion_3.getBoletos()[9],cliente12)
funcion_3.VentaTicket(funcion_3.getBoletos()[25], cliente13)"""


window = Tk()
window.option_add('*tearOff', FALSE)

picklefile = open('pcs', 'rb')
autocine = pickle.load(picklefile) #Bloque de deserialzación
picklefile.close()

first=First(window,autocine)
first.pack()

window.mainloop()

picklefile = open('pcs', 'wb')
pickle.dump(autocine,picklefile) #Bloque de serialización
picklefile.close()
