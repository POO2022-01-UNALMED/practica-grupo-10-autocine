from gestorAplicacion.Autocine import *

#*
# * @author Jimena Uribe Giraldo
# * @param Clase Sala2D.
# * @summary Clase que que hereda de la Clase Sala. En esta se crean los puestos para la Sala 2D.
# 


from fileinput import filename
from importlib.metadata import FileHash
from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.salas.puesto import Puesto

# Clase.
class Sala2D(Sala):
    
    def __init__ (self,*args):
        if(len(args) == 4):
            filas, columnas, filasPreferencial, autocine = args
            super().__init__(filas, columnas, filasPreferencial, 2000,autocine)
            
        elif(len(args) == 2):
            preferencial , autocine = args
            super().__init__(8, 12, preferencial, 2000, autocine)

    
    def getTipo(self):
        return "2D"
    
    def cantidadPuestos(self):
        #	No recibe nada y devuelve un entero el cual corresponde a la cantidad de puestos
        #	disponibles

        return len(super().get.puestos())
    
    def getCantidadPuestos(self):
        return len(super().getPuestos())
    
    def crearPuestos(self):
        #	No recibe ningun parametro y no retorna nada
        #	Crea cada puesto según la cantidad de filas prefencial, filas, y columnas

        total: int =  int(self._filas)*int(self._columnas)  #numero de puestos

         totalPreferencial: int = int(self._filasPreferencial)*int(self._columnas)  #numero de puestos prefe y se le resta 1 cada que se compre uno

        tipo : str = "PREFENCIAL"
            
        for i in range(total):

            if totalpreferencial<=0:
                tipo = "GENERAL"
            else:
                totalpreferencial -= 1

            puesto : Puesto = Puesto(tipo,i+1)

            self.puestos.append(puesto)    

    #get y set
    @staticmethod
    def getSalas2D():
        return gestorAplicacion.Salas.Sala2D.salas2D
    @staticmethod
    def setSalas2D(salas2d):
        gestorAplicacion.Salas.Sala2D.salas2D = salas2d


