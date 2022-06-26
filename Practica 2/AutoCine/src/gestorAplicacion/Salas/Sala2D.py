from gestorAplicacion.Autocine import *

#*
# * @author Jimena Uribe Giraldo
# * @param Clase Sala2D.
# * @summary Clase que que hereda de la Clase Sala. En esta se crean los puestos para la Sala 2D.
# 

class Sala2D(Sala):
    # Serializacion.
    _SERIALVERSIONUID = 1
    salas2D = None
    @staticmethod
    def _static_initializer():
        gestorAplicacion.Salas.Sala2D.salas2D= []

    _static_initializer()

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public Sala2D(int filas, int columnas, int filasPreferencial, Autocine autocine)
    def __init__(self, filas, columnas, filasPreferencial, autocine):
        super().__init__(filas, columnas, filasPreferencial, 2000, autocine)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public Sala2D(int preferencial, Autocine autocine)
    def __init__(self, preferencial, autocine):
        self(8, 12, preferencial, autocine)

    def cantidadPuestos(self):
        #	No recibe nada y devuelve un entero el cual corresponde a la cantidad de puestos
        #	disponibles

        return len(self.puestos)

    def crearPuestos(self):
        #	No recibe ningun parametro y no retorna nada
        #	Crea cada puesto según la cantidad de filas prefencial, filas, y columnas

        total = self.filas*self.columnas #numero de puestos

        totalpreferencial = self.filasPreferencial*self.columnas #numero de puestos prefe y se le resta 1 cada que se compre uno

        tipo = "PREFENCIAL"

        for i in range(0, total):

            if totalpreferencial<=0:
                tipo = "GENERAL"
            else:
                totalpreferencial -= 1

            puesto = Puesto(tipo,i+1)

            self.puestos.append(puesto)

    #get y set
    @staticmethod
    def getSalas2D():
        return gestorAplicacion.Salas.Sala2D.salas2D
    @staticmethod
    def setSalas2D(salas2d):
        gestorAplicacion.Salas.Sala2D.salas2D = salas2d


