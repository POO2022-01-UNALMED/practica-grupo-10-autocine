from enum import Enum

#*
# * @author Daniel Alejandro Giraldo Giraldo.
# * @param clase Puesto.
# * @summary Clase que tiene la imformacion relacionada con los puestos.
# 
from gestorAplicacion import Salas.Puesto.Tipo


#clase
class Puesto:

    #tipo

    class Tipo(Enum):
        PREFERENCIAL = 0
        GENERAL = 1

        #atributos

    def __init__(self, tipo, numero):
        self._tipo = 0
        self._numero = 0
        self._precio = 0

        self.setTipo(tipo)
        self.setNumero(numero)

    #gets y sets
    def getTipo(self):
        return self._tipo


    def setTipo(self, tipo):
        if tipo == "PREFERENCIAL":
            self._tipo = gestorAplicacion.Salas.Puesto.Tipo.PREFERENCIAL
        else:
            self._tipo = gestorAplicacion.Salas.Puesto.Tipo.GENERAL
    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero

    def getPrecio(self):
        if self._tipo == gestorAplicacion.Salas.Puesto.Tipo.PREFERENCIAL:
            return 25000
        else:
            return 15000
    def setPrecio(self, precio):
        self._precio = precio
    @staticmethod
    def getPuestos():
        return gestorAplicacion.Salas.Puesto.puestos

    @staticmethod
    def setPuestos(puestos):
        gestorAplicacion.Salas.Puesto.puestos = puestos
