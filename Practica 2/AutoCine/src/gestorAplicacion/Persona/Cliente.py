from gestorAplicacion.Taquilla import *
from gestorAplicacion.Taquilla.Ticket import Ticket
from gestorAplicacion.Autocine.Autocine import Autocine
from gestorAplicacion.Persona import *

from typing import Collection
from collections import Counter

#*
# * @author Jimena Uribe Giraldo.
# * @summary Clase Cliente, lleva todo lo relativo a la información del espectador
# 
# 



class Cliente:
    
    def __init__(self,id,nombre,edad,autocine):
        self._historialCompras = [] #una lista con los boletos que ha comprado el cliente en el cine a traves de su vida
        self._id= id
        self._nombre = nombre
        self._edad = edad
        Autocine.agregarCliente(self)
        self._autocine = autocine

    def GeneroMasVisto(self):
        #No recibe nada y devuelve string del género más visto del cliente

        genreList = [] #lista con los generos que ha visto el cliente
        for ticket in self._historialCompras:
            genreList.append(Ticket.getFuncion().getPelicula().getGenero()) #Recorre el historial de compras del cliente y anexa los generos de los tickets

        veces=Counter(genreList).items()   #lista para guardar la frecuencia de cada genero

        occ=Counter(genreList).values() #De la lista de géneros extrae la frecuencia de cada elemento
        valor_max=max(occ)
        
        for genero  in veces:
            if genero[1]==valor_max:
                return genero[0]



    #
    #Getting and setting
    #
    def getId(self):
        return self._id
    def setId(self, id):
        self._cedula = id

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad

  

    def getHistorialCompras(self):
        return self._historialCompras
    def setHistorialCompras(self, historialCompras):
        self._historialCompras = historialCompras


    def getAutocine(self):
        return self._autocine
    def setAutoine(self, autocine):
        self._autocine = autocine
    
