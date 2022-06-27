from gestorAplicacion.Salas.Puesto import Tipo


#*
# * @author Jimena Uribe Giraldo.
# * @summary En esta clase todo lo relacionado a Ticket (Boleto), puesto, precio, función
# 


class Ticket:
    
    def __init__(self, funcion, puesto):
        
        self._estado : bool= True
        self._funcion = funcion
        self._num_puesto = 0
        self._precio_puesto = 0
        self.setAtr_puesto(puesto)
        self._precioTotal =  self.calcularPrecio()
        
    # Funciones
    
    def calcularPrecio(self) -> float:
        #		No recibe nada y devuelve un float el cual corresponde al calculo del precio del boleto 
        #		que depende del precio de la sala y el precio del puesto 

        precio_t: float = self._funcion.getSala().getPrecio()+self._precio_puesto  #Se suma el precio de la sala y el precio del puesto
        return precio_t
    
    @staticmethod
    def calcularPrecioDefinitivo(cliente):

        total = self.calcularPrecio()
        self.setPrecioTotal(total)

    def setAtr_puesto(self, puesto):

        ###Recibe el puessto con la que deseo asignarle los atributos de numero,tipo de puesto y precio de puesto  y no devuelve nada
        self._num_puesto = puesto.getNumero()     #Se establece al atributo de num_puesto  el numero del puesto que recibe
        self.setTipo_puesto(puesto.getTipo())     # Se establece al atributo tipo_puesto el tipo dl puesto que recibe 
        self.setPrecio_puesto(puesto.getPrecio()) # Se establece al atributo precio_puesto el precio del puesto que recibe

    def tipoString(self) -> str:
        
        #		Sin parametros  y retorna un String el cual indica el tipo de puesto del ticket
        #	
        
        if(self._tipo_puesto == Tipo.PREFENCIAL):
            return "P" 
        return "G"     
    # 
    # getter and setters
    # 
    def getNum_puesto(self):
        return self._num_puesto
    def setNum_puesto(self, num_puesto):
        self._num_puesto = num_puesto


    def getTipo_puesto(self):
        return self._tipo_puesto
    def setTipo_puesto(self, tipo_puesto):
        self._tipo_puesto = tipo_puesto


    def getPrecioTotal(self):
        return self._precioTotal
    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal


    def isEstado(self):
        return self._estado
    def setEstado(self, estado):
        self._estado = estado


    def getFuncion(self):
        return self._funcion
    def setFuncion(self, funcion):
        self._funcion = funcion

    def getPrecio_puesto(self):
        return self._precio_puesto
    def setPrecio_puesto(self, precio_puesto):
        self._precio_puesto = precio_puesto
