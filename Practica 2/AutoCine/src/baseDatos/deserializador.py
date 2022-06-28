import pickle
from gestorAplicacion.Autocine.Autocine import Autocine
from gestorAplicacion.Persona.Cliente import Cliente
from gestorAplicacion.Salas.Puesto import Puesto
from gestorAplicacion.Salas.Sala import Sala
from gestorAplicacion.Salas.Sala2D import Sala2D
from gestorAplicacion.Salas.Sala3D import Sala3D
from gestorAplicacion.Taquilla.Funcion import Funcion
from gestorAplicacion.Taquilla.Pelicula import Pelicula
from gestorAplicacion.Taquilla.Ticket import Ticket
import pathlib
import os

class Deserializador():
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo.
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # Unpickle los datos.
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        # Cierro el archivo.
        picklefile.close()
        return lista
        # Cierro el archivo.
    
    def deserializarTodo():
        Autocine.autocine = Deserializador.deserializar(Autocine.dependientes, "Autocine")
        Cliente.clientes =  Deserializador.deserializar(Cliente.tecnicos, "Clientes")
        Puesto.setPuestos = Deserializador.deserializar(Puesto.cajasRegistradoras, "Puestos")
        Sala.clientes = Deserializador.deserializar(Sala.clientes, "Salas")
        Sala2D.componentes = Deserializador.deserializar(Sala2D.componentes, "Salas2D")
        Sala3D.productos = Deserializador.deserializar(Sala3D.productos, "Salas3D")
        Funcion.servicios = Deserializador.deserializar(Funcion.servicios, "Funciones")
        Pelicula._componentes = Deserializador.deserializar(Pelicula._componentes, "Peliculas")
        Ticket._empleados = Deserializador.deserializar(Ticket._empleados, "Tickets")