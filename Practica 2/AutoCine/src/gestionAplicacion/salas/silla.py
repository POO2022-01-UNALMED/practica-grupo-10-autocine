


from gestionAplicacion.salas.tipo import Tipo

class Silla:
    def __init__(self,tipo,numero):
        self.setTipo(tipo)      #se debe establecer el precio depende del tipo
        self._numero:int = numero




    #
    #Getting and setting
    #
    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo:str):
        if (tipo=="VIP"):
            self._tipo=Tipo.VIP          
        else:
            self._tipo=Tipo.SENCILLA


    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero


    def getPrecio(self):
        if(self._tipo==Tipo.VIP):     #Se ponen los precios de VIP como 7000 y 5000
            return 20000
        else:
            return 15000

    def setPrecio(self, precio):
        self._precio = precio