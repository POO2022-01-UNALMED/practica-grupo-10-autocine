#**
#* @author Jhon Ever Gallego Atehortua.
#* @param Clase Funcion.
#* @summary Clase que representa la funcion en la que se da una pelicula.
#**

from code import interact
from hashlib import new
from tkinter import NONE
from xmlrpc.client import Boolean
from gestionAplicacion.boleteria.horario import Horario
from gestionAplicacion.boleteria.boleto import Boleto
from gestionAplicacion.salas.sala import Sala

# Clase.
class Funcion:

    # Atributos.
    def __init__(self,dia,mes,horario,pelicula,sala,cine):
        self._boletos = []  
        self._dia:int = dia
        self._mes:int = mes
        self._horario = horario
        self._pelicula = pelicula
        self.setSala(sala)  
        self.setCine(cine)
        
        sala.agregarFuncion(self)
        self._numero = len(cine.getCartelera()) +1 
        self._cantidadBoletosVendidos:int=0
        cine.agregarFuncion(self)
        self.crearBoleteria()           


    # Metodos.
	#**
	#* @param dia
	#* @param mes
	#* @param horario
	#* @param pelicula
	#* @param num_sala
	#* @param autocine
	#* @summary Recibe una fecha: (dia, mes, horario), pelicula, numero de sala y el autocine. 
	#* @return Una funcion para una pelicula.
	#**
    @classmethod
    def crearFuncion(cls,dia:int,mes:int,horario:Horario,pelicula,num_sala:int,cine): #devuelve una funcion o none
        sala = cine.buscarSala(num_sala)
        if(sala!=None): #Si se encuentra ese número de sala en ese cine se verifica disponibilidad
            if(sala.verificarDisponibilidad(dia,mes,horario.getHora())):
                return Funcion(dia,mes,horario,pelicula,sala,cine)  #Se asigna una función a ese cine 
            else:
                return None
        else:
            return None

    @classmethod
    def formatearFunciones(cls,funciones):
        #Recibe unas funciones y procede a organizarlas de forma adecuada para el cliente

        resultado = ""
        for funcion in funciones:
            formato = "{}|{}|{}|{}"
            fecha = "Fecha: " + "{:>02d}/{:>02d}".format(funcion.getDia(),funcion.getMes())
            resultado += str(funcion.getPelicula().getNombre())+" "+str(funcion.getPelicula().getClasificacion())+"+"+"\n"

            resultado += formato.format(funcion.getHorario().getHora().center(6),
                                        ("Sala "+str(funcion.getSala().getNumero())).center(8),
                                        str(funcion.getSala().getTipo()).center(4),
                                        "{:>3d}".format(funcion.getNumero()).center(5))
            resultado +=  "\n" + fecha
            resultado += "\n\n"
        return resultado


    #**
	#* @summary Metodo que se encarga de crear un boleto para cada puesto.
	#**
    def crearBoleteria(self):
        sillas = self._sala.getSillas()     
        disponibles:int=self._sala.cantidadSillas() 
        total:int=len(self._sala.getSillas())
        for i in range(total):
            if(disponibles>0):
                boleto:Boleto= Boleto(self,sillas[i])      
                self._boletos.append(boleto)
                disponibles-=1
    
    
    #**
	#* @summary Metodo que se encarga de la disponibilidad de un puesto en una sala.
	#* @return La disponibilidad de un puesto y su tipo.
	#**
    def verDisponibilidad(self):
        total =[] 
        for boleto in self._boletos:
            if boleto!=None:                             
                tupla_boleto:tuple=(boleto.isDisponibilidad(),boleto.tipoString()+str(boleto.getNum_silla()))       #se crea un string de la forma disponibilidad/tipo/numerosilla
                total.append(tupla_boleto)
        return total


    #**
	#* @param ticket
	#* @param cliente
	#* @summary Recibe ticket para cambiar su estado y un cliente al cual se le asigna. Metodo para vender un ticket.
	#* @return Un Boolen de si se pudo o no vender un ticket. Retorna True o False segun sea el caso.
	#**
    def VentaBoleto(self,boleto,cliente)->bool:
        if (boleto.isDisponibilidad()==True and cliente.getEdad()>=self.getPelicula().getClasificacion()):
            boleto.setDisponibilidad(False) 
            cliente.getHistorialCompras().append(boleto)   
            self._cantidadBoletosVendidos+=1        
            boleto.calcularPrecioDefinitivo(cliente)   
            ganancia:float=self._cine.getDineroGanado()+boleto.getPrecioTotal()
            self._cine.setDineroGanado(ganancia)
            self._pelicula.anadirCantidadBoletos()
            return True
        else:
            return False


    # Getters and Setter.s
    def getDia(self):
        return self._dia
    def setDia(self, dia):
        self._dia = dia

    def getMes(self):
        return self._mes
    def setMes(self, mes):
        self._mes = mes

    def getHorario(self):
        return self._horario
    def setHorario(self, horario):
        self._horario = horario

    def getPelicula(self):
        return self._pelicula
    def setPelicula(self, pelicula):
        self._pelicula = pelicula

    def getSala(self):
        return self._sala
    def setSala(self, sala):
        self._sala = sala

    def getBoletos(self):
        return self._boletos
    def setBoletos(self, boletos):
        self._boletos = boletos

    def getCantidadBoletosVendidos(self):
        return self._cantidadBoletosVendidos
    def setCantidadBoletosVendidos(self, cantidadBoletosVendidos):
        self._cantidadBoletosVendidos = cantidadBoletosVendidos

    def getCine(self):
        return self._cine
    def setCine(self, cine):
        self._cine = cine

    def getCantidadfunciones(self):
        return self._cantidadFunciones
    def setCantidadfunciones(self, cantidadFunciones):
        self._cantidadFunciones = cantidadFunciones

    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero