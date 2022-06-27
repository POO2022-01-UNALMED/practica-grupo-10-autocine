#**
#* @author Jhon Ever Gallego Atehortua.
#* @param Clase Sala3D.
#* @summary Clase que que hereda de la Clase Sala. En esta se crean los puestos para la Sala 3D.
#**

from fileinput import filename
from importlib.metadata import FileHash
from gestorAplicacion.Salas.Sala import Sala
from gestorAplicacion.Salas.Puesto import Puesto

# Clase.
class Sala3D(Sala):
    
    # Atributos.
    def __init__(self, *args):
        if(len(args) == 4):
            filas, columnas,candidadgafas, autocine = args
            super().__init__(filas, columnas, 0, 5000,autocine)
            self._cantidadgafas = candidadgafas
        elif(len(args) == 3):
            filas, columnas, autocine = args
            super().__init__(filas, columnas, 0,5000, autocine)
            self._cantidadgafas = filas*columnas
            
            
    #**
	#* @summary Da la cantidad de puestos disponibles para su creacion segun la disponibilidad de gafas 3D.
	#* @return La cantidad de puestos disponibles para la creacion de una funcion.
	#**
    def cantidadPuestos(self) -> int:
        totalpuestos: int = len(self._puestos)    

        if (totalpuestos < int(self._cantidadgafas)): 
            return totalpuestos
        return int(self._cantidadgafas)


    #** 
	#* @summary Metodo para crear los puestos dependiendo la cantidad de filas y columnas.
	#**
    def crearPuestos(self):
        total: int = int(self._filas)*int(self._columnas)
        tipo: str = "PREFERENCIAL"
        for i in range(total):              
            puesto: Puesto = Puesto(tipo, i+1)
            self._puestos.append(puesto)


    # Getters and Setters.
    def getCantidadPuestos(self):
        return self._cantidadgafas
    
    def setCantidadPuestos(self, funciones):
        self._cantidadgafas = funciones
        
    def getTipo(self):
        return("3D")
