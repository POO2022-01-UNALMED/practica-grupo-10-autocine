


from typing import Collection
from collections import Counter


#*
# * @author Jimena Uribe Giraldo.
# * @summary Clase Cliente, lleva todo lo relativo a la información del espectador
# 
# 

class Cliente:

    def __init__(self,cedula,nombre,edad,ocupacion,cine, referido = None):
        self._historialCompras = [] #una lista con los boletos que ha comprado el cliente en el cine a traves de su vida
        self._cedula = cedula
        self._nombre = nombre
        self._edad = edad
        self._ocupacion = ocupacion
        cine.agregarCliente(self)
        self._cine = cine
        self._descuento = 0
        self._referidos = 0
        if (self._ocupacion == "Estudiante"):
            self._descuento += 0.1


    #Descuentos

    def descuentoCliente(self):
        
        self._cine.mostValueClient()    #Descuento del 20% al cliente que mas ha comprado
        
        if (self._descuento<=0.39 and self._referidos>0):#Si los descuentos no sobrepasan el 0.4, se aplican

            self._descuento+=0.01*self._referidos
        return "Descuento aplicado"

    #La pelicula más vista
    def mostWatchedGenre(self):
        #No recibe nada pero devuelve una string con el genero mas visto del cliente

        genreList=[]    ##lista con los generos que ha visto el cliente
        for boleto in self._historialCompras:
            genreList.append(boleto.getFuncion().getPelicula().getGenero()) #Recorre el historial de compras del cliente y anexa los generos de los tickets

        cuenta=Counter(genreList).items()   #lista para guardar la frecuencia de cada genero

        occ=Counter(genreList).values() #De la lista de géneros extrae la frecuencia de cada elemento
        valor_max=max(occ)
        
        for genero  in cuenta:
            if genero[1]==valor_max:
                return genero[0]

    def referidos(self):
        #No recibe ni devuelve nada, su proposito es sumar referidos al cliente y llamar el metodo para aplicar el descuento por cada referido
        
        self._referidos+=1
        self.descuentoCliente()    
    #
    #Get y Set
    #
    def getCedula(self):
        return self._cedula
    def setCedula(self, cedula):
        self._cedula = cedula

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad

    def getOcupacion(self):
        return self._ocupacion
    def setOcupacion(self, ocupacion):
        self._ocupacion = ocupacion

    def getDescuento(self):
        return self._descuento
    def setDescuento(self, descuento):
        self._descuento = descuento

    def getHistorialCompras(self):
        return self._historialCompras
    def setHistorialCompras(self, historialCompras):
        self._historialCompras = historialCompras

    def getReferidos(self):
        return self._referidos
    def setReferidos(self, referidos):
        self._referidos = referidos

    def getCine(self):
        return self._cine
    def setCine(self, cine):
        self._cine = cine
