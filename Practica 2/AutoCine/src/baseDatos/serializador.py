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

class Serializador():
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Creo el archivo pickle para guardar los objetos.
            picklefile = open(camino(className), 'wb')
            # Pickle el objeto en el archivo.
            pickle.dump(lista, picklefile)
            # Cierro el archivo para guardar.
            picklefile.close()
            
        except:
            print("paila tuqui tuqui muñeco")

    def serializarTodo():

        Serializador.serializar(Autocine.getAutocine(), "Autocine")
        Serializador.serializar(Cliente.getClientes(), "Clientes")
        Serializador.serializar(Puesto.getPuestos(), "Puestos")
        Serializador.serializar(Sala.getSalas(), "Salas")
        Serializador.serializar(Sala2D.getSalas2D, "Salas2D")
        Serializador.serializar(Sala3D.getSalas3D, "Salas3D")
        Serializador.serializar(Funcion.getFunciones(), "Funciones")
        Serializador.serializar(Pelicula.getPeliculas(), "Peliculas")
        Serializador.serializar(Ticket.getTickets(), "Tickets")