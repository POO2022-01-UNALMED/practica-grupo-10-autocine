#*
# * @author Daniel Alejandro Giraldo Giraldo.
# * @param clase Pelicula.
# * @summary Clase que tiene la imformacion relacionada con las peliculas.
# 

from gestorAplicacion import Autocine.Autocine
from gestorAplicacion import Salas.Sala


# clase
class Pelicula:

    #artributos

    def __init__(self, nombre, genero, duracion, lenguaje, clasificacion, autocine):
        #instance fields found by Java to Python Converter:
        self._nombre = None
        self._genero = None
        self._duracion = 0
        self._lenguaje = None
        self._clasificacion = 0
        self._autocine = None

        self._nombre = nombre
        self._genero = genero
        self._duracion = duracion
        self._lenguaje = lenguaje
        self._clasificacion = clasificacion
        self._autocine = autocine
        gestorAplicacion.Autocine.Autocine.agregarPelicula(self)

    # gets y sets
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero = genero

    def getDuracion(self):
        return self._duracion
    def setDuracion(self, duracion):
        self._duracion = duracion

    def getLenguaje(self):
        return self._lenguaje
    def setLenguaje(self, lenguaje):
        self._lenguaje = lenguaje

    def getClasificacion(self):
        return self._clasificacion
    def setClasificacion(self, clasificacion):
        self._clasificacion = clasificacion
    @staticmethod
    def getPeliculas():
        return gestorAplicacion.Taquilla.Pelicula.peliculass

    @staticmethod
    def setPeliculas(peliculass):
        Pelicula.peliculass = peliculass