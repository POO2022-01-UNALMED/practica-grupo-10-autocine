
#*
# * @author Daniel Alejandro Giraldo Giraldo.
# * @param clase Sala.
# * @summary Clase que tiene la imformacion relacionada con las salas.
# 
from gestorAplicacion import Autocine.Autocine
from gestorAplicacion import Taquilla.Funcion

#clase

class Sala:

    #serializador
    _SERIALVERSIONUID = 1
    salass = None
    @staticmethod
    def _static_initializer():
        gestorAplicacion.Salas.Sala.salass = []

    _static_initializer()

    #atributos



    #Constructores

    def __init__(self, filas, columnas, filaspreferencial, precio, autocine):
        #instance fields found by Java to Python Converter:
        self.numero = 0
        self.filas = 0
        self.columnas = 0
        self.filasPreferencial = 0
        self.precio = 0
        self.autocine = None
        self.puestos = []
        self.funciones = []

        self.filas = filas
        self.columnas = columnas
        self.filasPreferencial = filaspreferencial
        self.precio = precio
        self.autocine = autocine


        self.crearPuestos()

        gestorAplicacion.Autocine.Autocine.agregarSala(self)

        self.numero = gestorAplicacion.Autocine.Autocine.getSalas().size()


    #Metodos abtractos


    def cantidadPuestos(self):
        pass

    def crearPuestos(self):
        pass

    #Metodos

    def agregarFuncion(self, funcion):
        self.funciones.append(funcion)

    def verificarDisponibilidad(self, dia, mes):
        consulta = "" + str(dia) + str(mes)
        fechas = []
        horarios = []
        disponibles = ["12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]
        for func in self.funciones:
            info = "" + func.getDia() + func.getMes()
            fechas.append(info)
            info = ""


        i = 0
        while i < len(fechas):
            if fechas[i] == consulta:
                horarios.append(self.funciones[i].getHorario())
            i += 1

        for horario in horarios:
            disponibles.remove(horario)

        respuesta = ""

        for d in disponibles:
            respuesta += d + "\n"

        return respuesta == "12:00\n14:00\n16:00\n18:00\n20:00\n22:00\n"

    def verificarDisponibilidad(self, dia, mes, hora):


        consulta = str(dia) + "/" + str(mes) + "/" + hora

        fechasfunciones = []
        for func in self.funciones:
            info = func.getDia() + "/" + func.getMes() + "/" + func.getHorario()
            fechasfunciones.append(info)

            info = ""

        for i in fechasfunciones:
            if i == consulta:
                return False

        return True
    def unoDisponible(self, dia, mes):


        consulta = "" + str(dia) + str(mes)

        fechas = []


        horarios = []


        disponibles = ["12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]

        for func in self.funciones:
            info = "" + func.getDia() + func.getMes()
            fechas.append(info)
            info = ""


        i = 0
        while i < len(fechas):
            if fechas[i] == consulta:
                horarios.append(self.funciones[i].getHorario())
            i += 1

        for horario in horarios:
            disponibles.remove(horario)

        respuesta = ""

        for d in disponibles:
            respuesta += d + "\n"

        if len(respuesta) >= 5:
            return True
        else:
            return False
    def verHorarios(self, dia, mes):

        consulta = "" + str(dia) + str(mes)
        fechas = []
        horarios = []
        disponibles = ["12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]

        for func in self.funciones:

            info = "" + func.getDia() + func.getMes()
            fechas.append(info)
            info = ""


        i = 0
        while i < len(fechas):
            if fechas[i] == consulta:
                horarios.append(self.funciones[i].getHorario())
            i += 1


//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
