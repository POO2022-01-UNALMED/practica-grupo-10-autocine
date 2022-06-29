

from gestionAplicacion.salas.tipo import Tipo


#*
# * @author Jimena Uribe Giraldo.
# * @summary En esta clase todo lo relacionado a Ticket (Boleto), puesto, precio, función
# 

class Boleto:

    def __init__(self, funcion, silla):
        
        self._disponibilidad : bool= True
        self._funcion = funcion
        self._num_silla = 0
        self._precio_silla = 0
        self.setAtr_silla(silla)
        self._precioTotal =  self.calcularPrecio()
        
    # Funciones

    def calcularPrecio(self) -> float:
         #		No recibe nada y devuelve un float el cual corresponde al calculo del precio del boleto 
        #		que depende del precio de la sala y el precio del puesto 
        bruto: float = self._funcion.getSala().getPrecio()+self._precio_silla   #Se suma el precio de la sala y el precio del puesto
        return bruto

    def calcularPrecioDefinitivo(self, cliente):

        #Recibe a un cliente  y no devuelve nada, este precio se le descuenta un descuento(Si este cliente lo tiene)
        
        total: float = self.calcularPrecio()-(self.calcularPrecio()*(cliente.getDescuento())) #Al precio bruto le resta el descuento del cliente si este lo posee
        self.setPrecioTotal(total)  # Se establece el resultado de la linea anterior al atributo PrecioTotal

    def setAtr_silla(self, silla):

        ###Recibe el puessto con la que deseo asignarle los atributos de numero,tipo de puesto y precio de puesto  y no devuelve nada
        self._num_silla = silla.getNumero()     #Se establece al atributo de num_puesto  el numero del puesto que recibe
        self.setTipo_silla(silla.getTipo())     # Se establece al atributo tipo_puesto el tipo dl puesto que recibe 
        self.setPrecio_silla(silla.getPrecio()) # Se establece al atributo precio_puesto el precio del puesto que recibe

    def tipoString(self) -> str:
         #		Sin parametros  y retorna un String el cual indica el tipo de puesto del ticket
        #
        if(self._tipo_silla == Tipo.VIP):
            return "P-" #El tipo de la silla es PREFERENCIAL retornara P-
        return "G-"     # En caso de que sea GENERAL retornara G-
    # 
    # Get y set
    # 
    def getNum_silla(self):
        return self._num_silla
    def setNum_silla(self, num_silla):
        self._num_silla = num_silla


    def getTipo_silla(self):
        return self._tipo_silla
    def setTipo_silla(self, tipo_silla):
        self._tipo_silla = tipo_silla


    def getPrecioTotal(self):
        return self._precioTotal
    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal


    def isDisponibilidad(self):
        return self._disponibilidad
    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad


    def getFuncion(self):
        return self._funcion
    def setFuncion(self, funcion):
        self._funcion = funcion

    def getPrecio_silla(self):
        return self._precio_silla
    def setPrecio_silla(self, precio_silla):
        self._precio_silla = precio_silla
