from gestorAplicacion.Taquilla import *
from gestorAplicacion.Autocine import *

#*
# * @author Jimena Uribe Giraldo.
# * @summary Clase Cliente, lleva todo lo relativo a la información del espectador
# *
# 
class Cliente:

    # Serializacion.
    _SERIALVERSIONUID = 1
    clientess = None
    @staticmethod
    def _static_initializer():
        gestorAplicacion.Persona.Cliente.clientess = []

    _static_initializer()

    #Atributos
    _edad = 0
    _historialCompras = [] #una lista con los boletos que ha comprado el cliente en su vida


    #Constructores
    def __init__(self, id, nombre, edad, autocine):
        #instance fields found by Java to Python Converter:
        self._id = 0
        self._nombre = None
        self._autocine = None

        self._id = id
        self._nombre = nombre
        Cliente._edad = edad
        self._autocine=autocine

    def GeneroMasVisto(self):
        #		
        #		No recibe nada y devuelve string del género más visto del cliente
        #		 
        genreList = [] #lista con los generos que ha visto el cliente
        for ticket in gestorAplicacion.Persona.Cliente._historialCompras:
            Ticket.getFuncion()
            genreList.append(Funcion.getPelicula().getGenero()) #Recorre el historialdel cliente y anexa sus generos
        veces = [] #lista para guardar la frecuencia de cada genero
        for genre in genreList:
            occ = Collections.frequency(genreList, genre) #De la lista de géneros extrae la frecuencia
            veces.append(occ)

        return genreList[(veces.index(Collections.max(veces)) if Collections.max(veces) in veces else -1)] #devuelve el género más visto



    #set y get
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    @staticmethod
    def getEdad():
        return gestorAplicacion.Persona.Cliente._edad

    def setEdad(self, edad):
        Cliente._edad = edad

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id


    @staticmethod
    def getHistorialCompras():
        return gestorAplicacion.Persona.Cliente._historialCompras
    def setHistorialCompras(self, historialCompras):
        Cliente._historialCompras = historialCompras


    def getAutocine(self):
        return self._autocine

    def setAutocine(self, autocine):
        self._autocine = autocine

    @staticmethod
    def getClientes():
        return gestorAplicacion.Persona.Cliente.clientess


    def toString(self):

        return "Cliente: " + self._nombre + "-" + str(gestorAplicacion.Persona.Cliente._edad)


