#**
#* @author Jhon Ever Gallego Atehortua.
#* @param Clase Sala3D.
#* @summary Clase que que hereda de la Clase Sala. En esta se crean los puestos para la Sala 3D.
#**

from fileinput import filename
from importlib.metadata import FileHash
from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.salas.silla import Silla

# Clase.
class Sala3D(Sala):

    # Atributos.
    def __init__(self, *args):
        if(len(args) == 4):
            filas, columnas,candidadgafas, cine = args
            super().__init__(filas, columnas, 0, 5000,cine)
            self._cantidadgafas = candidadgafas
        elif(len(args) == 3):
            filas, columnas, cine = args
            super().__init__(filas, columnas, 0,5000, cine)
            self._cantidadgafas = filas*columnas
      
    
    #**
	#* @summary Da la cantidad de puestos disponibles para su creacion segun la disponibilidad de gafas 3D.
	#* @return La cantidad de puestos disponibles para la creacion de una funcion.
	#**  
    def cantidadSillas(self) -> int:
        totalsillas: int = len(self._sillas)    
        if (totalsillas<int(self._cantidadgafas)): 
            return totalsillas
        return int(self._cantidadgafas) 


    #** 
	#* @summary Metodo para crear los puestos dependiendo la cantidad de filas y columnas.
	#**
    def crearSilleteria(self):
        total: int = int(self._filas)*int(self._columnas)
        tipo: str = "VIP"
        for i in range(total):                  
            silla: Silla = Silla(tipo, i+1)
            self._sillas.append(silla)


    # Getters and Setters.
    def getCantidadSillas(self):
        return self._cantidadgafas
    
    def setCantidadSillas(self, funciones):
        self._cantidadgafas = funciones
        
    def getTipo(self):
        return("3D")