



from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.salas.silla import Silla

#*
# * @author Jimena Uribe Giraldo
# * @param Clase Sala2D.
# * @summary Clase que que hereda de la Clase Sala. En esta se crean los puestos para la Sala 2D.
# 


class Sala2D(Sala):


    def __init__ (self,*args):
        if(len(args) == 4):
            filas, columnas, filasvip, cine = args
            super().__init__(filas, columnas, filasvip, 2000,cine)
            
        elif(len(args) == 2):
            vip , cine = args
            super().__init__(8, 12, vip, 2000, cine)

    
    def getTipo(self):
        return "2D"

    def cantidadSillas(self):
        #	No recibe nada y devuelve un entero el cual corresponde a la cantidad de puestos
        #	disponibles
        return len(super().getSillas())
    
    def getCantidadSillas(self):
        return len(super().getSillas())
    
    def crearSilleteria(self):
              #	No recibe ningun parametro y no retorna nada
        #	Crea cada puesto según la cantidad de filas prefencial, filas, y columnas
        total: int =  int(self._filas)*int(self._columnas)  #Numero de sillas 
        totalvip: int = int(self._filasvip)*int(self._columnas) #Numero de sillas vip(se va reduciendo con cada nueva silla vip creada)

        tipo : str = "VIP"          #Se cambia el tipo de silla

        for i in range(total):  
            
            if(totalvip<=0):				#Si se acaban las sillas VIP cambiar el tipo por las sencillas 
                tipo = "SENCILLA"

            else:								
                totalvip-=1
                
            silla : Silla = Silla(tipo,i+1) #Se crea un objeto de silla 
            
            self._sillas.append(silla) #Se agrega la silla que creamos 
