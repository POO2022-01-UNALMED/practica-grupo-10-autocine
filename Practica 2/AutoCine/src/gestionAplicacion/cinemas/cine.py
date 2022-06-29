#**
#* @author: Jhon Ever Gallego Atehortua.
#* @param: Clase Autocine.
#* @summary: Clase Autocine. Clase que contiene as salas, funciones, peliculas, cientes y metodos para a creación, modificación y observación de los mismos.
#**

import random
from gestionAplicacion.boleteria.funcion import Funcion
from gestionAplicacion.boleteria.pelicula import Pelicula
from gestionAplicacion.boleteria.horario import Horario
from gestionAplicacion.boleteria.boleto import Boleto
from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.cinemas.cliente import Cliente

# Clase.
class Cine: 
    
    # Atributos.
    def __init__(self,nombre):
        self._nombre = nombre
        self._clientes = []
        self._cartelera = []
        self._peliculas = []
        self._salas= []
        self._dineroGanado= 0
        self._DESCUENTOMVC = 0.2
        
    # Metodos.
    #**
	#* @param mes
	#* @param dia
	#* @summary Recibe un mes y un dia.
	#* @return Una lista de salas disponibles.
	#**
    def salasDisponibles(self, mes: int, dia: int):
        disponibles=list()
        for sala in self._salas:
            if sala.almenosUnoDisponible(mes, dia):
                disponibles.append(sala)
        return disponibles


    def mostValueClient(self) -> str:
        clienteList=list()
        for client in self._clientes:
            clienteList.append(len(client.getHistorialCompras())) 
        valormax=max(clienteList)  
        for client in self._clientes:
            if(valormax==len(client.getHistorialCompras())):
                client.setDescuento(self._DESCUENTOMVC)
                return client.getNombre()
        return "Se ha aplicado el descuentos  a nuestro cliente mas fiel "


    #**
	#* @param pelicula
	#* @param dia
	#* @param mes
    #* @param cliente
	#* @summary Recibe una pelicula, un dia y mes.
	#* @return Una lista de funciones disponibles, que cumpla dichas condiciones.
	#**
    def verFuncion(self, *args) -> list:
        funciones: list = []
        if(len(args) == 3):
            pelicula: Pelicula = args[0]
            dia, mes = args[1:]
            for funcion in self.getCartelera():
                if(funcion.getPelicula() == pelicula and funcion.getDia() >= dia and funcion.getMes() == mes):
                    funciones.append(funcion)
            for funcion in self.getCartelera():
                if(funcion.getPelicula() == pelicula and funcion.getMes() > mes):
                    funciones.append(funcion)
        # Este es el que recibe dia, mes.
        elif(len(args) == 2):
            dia, mes = args
            for funcion in self.getCartelera():
                if(funcion.getDia() == dia and funcion.getMes() == mes):
                    funciones.append(funcion)
        elif(len(args) == 1):
            # Recibe mes.
            if(type(args[0]) == int):
                mes = args[0]
                for funcion in self.getCartelera():
                    if(funcion.getMes() == mes):
                        funciones.append(funcion)     
            # Recibe cliente.
            else:
                cliente: Cliente = args[0]
                for funcion in self.getCartelera():
                   if(funcion.getPelicula().getGenero() == cliente.mostWatchedGenre()):
                       funciones.append(funcion)
        return funciones

    def clientesValiosos(self)-> list: 
        clienteList=[]	
        for cliente in self._clientes:
            clienteList.append(len(cliente.getHistorialCompras())) 	
        cantidad= len(clienteList)			
        clienteList.sort(reverse=True)		
        top10= round(cantidad/10)								 
        mejoresCompas=[]			                                  
        for i in range(0, top10) :					
            valor =clienteList[i]							
            for client in self._clientes:
                if(len(client.getHistorialCompras())==valor):			
                    if not client in mejoresCompas:
                        mejoresCompas.append(client)
        return mejoresCompas


    #**
	#* @param num
	#* @summary Recibe una cedula.
	#* @return Verifica si un cliente está en la lista de clientes.
	#**
    def verificarCliente(self, num: int) -> bool:
        lista : list = []   
        for cliente in self.getClientes():
            lista.append(cliente.getCedula())
        return num in lista
    
    
    #**
	#* @param num
	#* @summary Recibe una cedula.
	#* @return Retorna un objeto cliente cuya cedula concuerde con la ingresada.
	#**
    def buscadorCliente(self, num : int):
        lista = self.getClientes()
        for cliente in lista:
            if (int(cliente._cedula)== int(num)):
                return cliente
        return None


    #**
	#* @param num
	#* @summary Recibe el numero de sala.
	#* @return Un objeto de clase Sala, cuyo numero coincida con el ingresado.
	#**
    def buscarSala(self, num):
        lista = self.getSalas()
        for sala in lista:
            if (int(sala.getNumero())== int(num)):
                return sala
        return None

    
    #**
	#* @param nombre
	#* @summary Recibe el nombre de una pelicula.
	#* @return Objeto de clase Pelicula, cuyo nombre coincida con el ingresado.
	#**
    def BuscadorPelicula(self, nombre):
        lista = self.getPeliculas()
        for pelicula in lista:
            if (str(pelicula.getNombre())==nombre):
                return pelicula
        return None


    #**
	#* @param numero
	#* @summary Recibe un numero de funcion.
	#* @return Retorna un objeto funcion.
	#**
    def BuscadorFuncion(self,numero):
        lista=[]
        for funcion in self._cartelera:
            lista.append(funcion.getNumero())

            if funcion.getNumero()==int(numero):  
                return funcion
        return None


    #**
	#* @param num_silla
	#* @param funcion
	#* @summary Recibe un numero de puesto y una funcion.
	#* @return Un objeto de clase Ticket, cuyo numero de puesto sea igual al ingresado.
	#**
    def BuscadorBoleto (self,num_silla: int,funcion:Funcion):
        lista=[]
        for boleto in funcion.getBoletos():
            lista.append(boleto.getNum_silla())

            if boleto.getNum_silla==num_silla:
                return boleto
        return None

        
    # Metodos para agregar elementos a las listas de la clase Autocine.
    #**
	#* @summary Metodos para agregar elementos a las listas de la clase Autocine.
	#**
    def agregarCliente(self,nuevo: Cliente):
       self._clientes.append(nuevo)

    def agregarPelicula(self,nuevo: Pelicula):
        self._peliculas.append(nuevo)

    def agregarSala(self,nuevo: Sala):
        self._salas.append(nuevo)

    def agregarFuncion(self,nuevo:Funcion):
        self._cartelera.append(nuevo)     


    # Getters and Setters.
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getClientes(self):
        return self._clientes
    def setClientes(self, clientes):
        self._clientes = clientes

    def getCartelera(self):
      return self._cartelera
    def setCartelera(self, cartelera):
      self._cartelera = cartelera

    def getPeliculas(self):
     return self._peliculas
    def setPeliculas(self, peliculas):
        self._peliculas = peliculas

    def getSalas(self):
        return self._salas
    def setSalas(self, salas):
        self._salas = salas

    def getDineroGanado(self):
        return self._dineroGanado
    def setDineroGanado(self, dineroGanado):
        self._dineroGanado = dineroGanado

    def getDescuentomvc(self):
        return self._DESCUENTOMVC
    def setDescuentomvc(self, DESCUENTOMVC):
        self._DESCUENTOMVC = DESCUENTOMVC