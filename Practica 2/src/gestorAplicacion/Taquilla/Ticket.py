from gestorAplicacion import Salas.Puesto
from gestorAplicacion import Salas.Puesto.Tipo
from gestorAplicacion import Persona.Cliente

#*
# * @author Jimena Uribe Giraldo.
# * @summary En esta clase todo lo relacionado a Ticket (Boleto), puesto, precio, función
# 
class Ticket:

    # Serializacion.
    _SERIALVERSIONUID = 1
    tickets = None
    @staticmethod
    def _static_initializer():
        gestorAplicacion.Taquilla.Ticket.tickets = []

    _static_initializer()

    #Atributos 

    _precioTotal = 0
    _estado = False
    _funcion = None
    _precio_puesto = 0


    def __init__(self, funcion, puesto):
        #instance fields found by Java to Python Converter:
        self._num_puesto = 0
        self._tipo_puesto = None

        Ticket._funcion = funcion
        self._set_puesto(puesto)
        Ticket._estado = True
        Ticket._precioTotal = Ticket.calcularPrecio()

    @staticmethod
    def calcularPrecio():
        #		No recibe nada y devuelve un float el cual corresponde al calculo del precio del boleto 
        #		que depende del precio de la sala y el precio del puesto 

        precio_t = Funcion.getSala().getPrecio() + gestorAplicacion.Taquilla.Ticket._precio_puesto # Se suma el precio de la sala y el precio de la silla

        return precio_t

    @staticmethod
    def calcularPrecioDefinitivo(cliente):

        total = gestorAplicacion.Taquilla.Ticket.calcularPrecio()
        gestorAplicacion.Taquilla.Ticket.setPrecioTotal(total)

    def estado(self):
        #	 Sin parÃ¡metros y retorna un String que corresponde al estado de disponibilidad
        #	 del ticket	
        #	 
        if gestorAplicacion.Taquilla.Ticket._estado:
            return "Libre"
        return "Ocupado"


    def tipoString(self):
        #		Sin parÃ¡metros  y retorna un String el cual indica el tipo de puesto del ticket
        #		 
        if self._tipo_puesto is gestorAplicacion.Salas.Puesto.Tipo.PREFERENCIAL:
            return "P"
        return "G"


    # get y set



    def getPrecio_puesto(self):
        return gestorAplicacion.Taquilla.Ticket._precio_puesto

    def getPrecioTotal(self):
        return gestorAplicacion.Taquilla.Ticket._precioTotal

    @staticmethod
    def setPrecioTotal(precioTotal):
        Ticket._precioTotal = precioTotal

    @staticmethod
    def isEstado():
        return gestorAplicacion.Taquilla.Ticket._estado
    @staticmethod
    def setEstado(estado):
        Ticket._estado = estado
    @staticmethod
    def getFuncion():
        return gestorAplicacion.Taquilla.Ticket._funcion
    def setFuncion(self, funcion):
        Ticket._funcion = funcion

    def getNum_puesto(self):
        return self._num_puesto

    def _set_puesto(self, puesto):
        #		Recibe el puesto con el que se asignan los atributos de num,tipo
        #		  y precio y no devuelve nada	
        #		 

        self._num_puesto = puesto.getNumero()
        self.setTipo_puesto(puesto.getTipo())
        self.setPrecio_puesto(puesto.getPrecio())

    def setPrecio_puesto(self, precio):
        Ticket._precio_puesto=precio

    def getTipo_puesto(self):
        return self._tipo_puesto

    def setTipo_puesto(self, tipo_puesto):
        self._tipo_puesto = tipo_puesto

    @staticmethod
    def getTicket():
        return gestorAplicacion.Taquilla.Ticket.tickets
    def setTicket(self, tickets):
        Ticket.tickets = tickets

