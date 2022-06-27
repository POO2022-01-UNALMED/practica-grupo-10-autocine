#**
#* @author Jhon Ever Gallego Atehortua.
#* @param Clase Funcion.
#* @summary Clase que representa la funcion en la que se da una pelicula.
#**

from code import interact
from hashlib import new
from tkinter import NONE
from xmlrpc.client import Boolean
from enum import Enum

from gestorAplicacion.Autocine.Autocine import Autocine
from gestorAplicacion.Taquilla.Funcion import Horario
from gestorAplicacion.Taquilla.Ticket import Ticket
from gestorAplicacion.Salas.Sala import Sala
from gestorAplicacion.Persona.Cliente import Cliente


# Clase.
class Funcion:
    
    # Enum Horario.
	#**
	#* 
	#* @summary Enum con los horarios.
	#*
	#**
    class Horario(Enum):
        UNO="12:00"
        DOS="14:00"
        TRES="16:00"
        CUATRO="18:00" 
        CINCO="20:00" 
        SEIS="22:00"

    def __init__(self,hora):
        self._hora = hora     

    @classmethod
    def getHorario(cls,hora)->"Horario": 
        horarios=[cls.UNO, cls.DOS, cls.TRES, cls.CUATRO, cls.CINCO, cls.SEIS]
        for horario in horarios:        
            if(hora == Funcion.getHora()):   
                return horario     
        return Horario(None)

    # Getters and Setters del enum Horario.
    def getHora(self)->str:    
        return self._hora
    def setHora(self,hora):
        self._hora=hora
    
    
    # Atributos.
    def __init__(self, dia, mes, horario, pelicula, sala, autocine):
        self._boletos = [] 
        self._dia: int = dia
        self._mes: int = mes
        self._horario = horario
        self._pelicula = pelicula
        self.setSala(sala) 
        self.setAutocine(autocine)
        
        Sala.agregarFuncion(self)
        self._numero = len(Autocine.getCartelera()) + 1 
        self._cantidadBoletosVendidos:int=0
        Autocine.agregarFuncion(self)
        self.crearTicket()         

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
    def crearFuncion(cls, dia: int, mes: int, horario: Horario, pelicula, num_sala: int, autocine):
        sala = Autocine.buscarSala(num_sala)
        if(sala != None): 
            if(Sala.verificarDisponibilidad(dia, mes, Funcion.getHora())):
                return Funcion(dia, mes, horario, pelicula, sala, autocine)  
            else:
                return None
        else:
            return None

    
    #**
	#* @summary Metodo que se encarga de crear un boleto para cada puesto.
	#**
    def crearTicket(self):
        puestos = self._sala.getPuestos()     
        disponibles: int = self._sala.cantidadPuestos()
        total: int = len(self._sala.getPuestos())
        for i in range(total):
            if(disponibles > 0):
                ticket: Ticket = Ticket(self, puestos[i])       #si es mayor que 0 crea el boleto, lo anade a la lista boletos y disponibles-
                self._tickets.append(ticket)
                disponibles-=1
    
    
    #**
	#* @summary Metodo que se encarga de la disponibilidad de un puesto en una sala.
	#* @return La disponibilidad de un puesto y su tipo.
	#**
    def verDisponibilidad(self):
        total = []   
        for ticket in self._tickets:
            if ticket != None:                                
                tupla_tickets: tuple = (Ticket.isEstado(), Ticket.tipoString() + str(Ticket.getNum_puesto()))    
                total.append(tupla_tickets)
        return total
    
    
    #**
	#* @param ticket
	#* @param cliente
	#* @summary Recibe ticket para cambiar su estado y un cliente al cual se le asigna. Metodo para vender un ticket.
	#* @return Un Boolen de si se pudo o no vender un ticket. Retorna True o False segun sea el caso.
	#**
    def VentaTicket(self, ticket, cliente) -> bool:
        if (Ticket.isEstado() == True and Cliente.getEdad() >= self.getPelicula().getClasificacion()):
            Ticket.setEstado(False)   
            self._cantidadTicketsVendidos+=1    
            Ticket.calcularPrecioDefinitivo(cliente)    
            return True
        else:
            return False


    # Getters and Setters.
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


    def getTickets(self):
        return self._tickets
    def setTickets(self, tickets):
        self._tickets = tickets


    def getCantidadTicketsVendidos(self):
        return self._cantidadTicketsVendidos
    def setCantidadTicketsVendidos(self, cantidadTicketsVendidos):
        self._cantidadTicketsVendidos = cantidadTicketsVendidos


    def getAutocine(self):
        return self._autocine
    def setAutocine(self, autocine):
        self._autocine = autocine


    def getCantidadfunciones(self):
        return self._cantidadFunciones
    def setCantidadfunciones(self, cantidadFunciones):
        self._cantidadFunciones = cantidadFunciones


    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero