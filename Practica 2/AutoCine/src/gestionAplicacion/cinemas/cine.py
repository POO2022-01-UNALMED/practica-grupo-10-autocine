

import random

from gestionAplicacion.boleteria.funcion import Funcion
from gestionAplicacion.boleteria.pelicula import Pelicula
from gestionAplicacion.boleteria.horario import Horario
from gestionAplicacion.boleteria.boleto import Boleto
from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.cinemas.cliente import Cliente


class Cine: 

    def __init__(self,nombre):
        self._nombre = nombre
        self._clientes = []
        self._cartelera = []
        self._peliculas = []
        self._salas= []
        self._dineroGanado= 0
        self._DESCUENTOMVC = 0.2



    



           
    
    def salasDisponibles(self, mes: int, dia: int):
        #Recibe un mes y un dia y retorna una lista de salas que tengan al menos un horario disponible ese dia

        disponibles=list()
        
        for sala in self._salas:
            if sala.almenosUnoDisponible(mes, dia):
                disponibles.append(sala)
        
        return disponibles

    def mostValueClient(self) -> str:
        '''
        No recibe nada y retorna una String con el nombre del cliente mas fiel al que le fue
		 aplicado el descuento. Su proposito es calcular el cliente que más compras ha hecho
		 para dar un descuento del 0.2.
        '''
        clienteList=list()
        
        for client in self._clientes:
            clienteList.append(len(client.getHistorialCompras()))   #Recorre el historial de compras del cliente y anexa el tamano de su historial de compra
        
        valormax=max(clienteList)   #Se establece el mayor numero de boletos comprados por parte de un cliente

        for client in self._clientes:
            if(valormax==len(client.getHistorialCompras())):    #Si la cantidad de boletos comprados es igual a valor max conseguir el nombre de este
                client.setDescuento(self._DESCUENTOMVC)
                return client.getNombre()

        return "Se ha aplicado el descuentos  a nuestro cliente mas fiel "


    def verFuncion(self, *args) -> list:
        funciones: list = []

        # Este es el ver funcion que recibe pelicula, dia, mes
        
        if(len(args) == 3):
            pelicula: Pelicula = args[0]
            dia, mes = args[1:]

            for funcion in self.getCartelera():
                if(funcion.getPelicula() == pelicula and funcion.getDia() >= dia and funcion.getMes() == mes):
                    funciones.append(funcion)
            for funcion in self.getCartelera():
                if(funcion.getPelicula() == pelicula and funcion.getMes() > mes):
                    funciones.append(funcion)

        # Este es el que recibe dia, mes
        elif(len(args) == 2):
            dia, mes = args
            for funcion in self.getCartelera():
                if(funcion.getDia() == dia and funcion.getMes() == mes):
                    funciones.append(funcion)

        elif(len(args) == 1):

            #recibe mes
            if(type(args[0]) == int):
                mes = args[0]
                for funcion in self.getCartelera():
                    if(funcion.getMes() == mes):
                        funciones.append(funcion)
                        
            #recibe cliente 
            else:
                cliente: Cliente = args[0]
                for funcion in self.getCartelera():
                   if(funcion.getPelicula().getGenero() == cliente.mostWatchedGenre()):
                       funciones.append(funcion)
            

        return funciones


    #Al 10 por ciento de los clientes mas fieles aplicarle un 10% de descuento a cada uno de ellos 

    def clientesValiosos(self)-> list:
        '''
        Recibe nada y retorna una List des objetos tipo Cliente. Su proposito es calcular
	    de entre la lista de clientes el 0.1 que tiene mayor cantidad de compras en historialCompras
        '''    
        clienteList=[]		#Aca estaran los tamanos de historial de compra de cada cliente
        
        for cliente in self._clientes:
            clienteList.append(len(cliente.getHistorialCompras())) 	#Recorre el historial de compras del cliente y anexa el tamano de su historial de compra
        
        cantidad= len(clienteList)				#Cantidad de clientes que se tiene
        
        clienteList.sort(reverse=True)		#Ordenar la lista de mayor a menor
        top10= round(cantidad/10)								# El 10% de los clientes 
        mejoresCompas=[]			                                    #Clientes mas fieles
        
        for i in range(0, top10) :					
            valor =clienteList[i]								#Conseguir el 10% de los tamanos de historial de compra mas grandes
            for client in self._clientes:
                
                if(len(client.getHistorialCompras())==valor):				#Si el tamano de historial de compra es igual al valor agregar a los mejores clientes (mejoresCompas)
                    if not client in mejoresCompas:
                        mejoresCompas.append(client)
        
        return mejoresCompas


    def verificarCliente(self, num: int) -> bool:
        '''
        Recibe un numero de cedula, retorna un boolean. Su proposito es verificar
		que un cliente este en la lista de clientes de acuerdo a su numero de cedula
        '''

        lista : list = []   #Lista de cédulas
        
        for cliente in self.getClientes():
            lista.append(cliente.getCedula())
        
        return num in lista
    
    
    
    

    def buscadorCliente(self, num : int):
        '''
        Recibe un numero de cedula, retorna un objeto de clase Cliente. Su proposito es retornar el
		cliente cuyo numero de cedula concuerde con el ingresado al metodo
        '''

        lista = self.getClientes()
        for cliente in lista:
            if (int(cliente._cedula)== int(num)):
                return cliente
        return None

    def buscarSala(self, num):
        '''
        Recibe el numero de una sala, retorna un objeto de clase Sala. Su proposito es retornar la
		sala cuyo numero coincida con el numero ingresado
        '''
        lista = self.getSalas()
        for sala in lista:
            if (int(sala.getNumero())== int(num)):
                return sala
        return None

    
    def BuscadorPelicula(self, nombre):
        '''
        Recibe el nombre de una pelicula, retorna un objeto de clase Pelicula. Su proposito es retornar la
		pelicula cuyo nombre coincida con el nombre ingresado
        '''
        lista = self.getPeliculas()
        for pelicula in lista:
            if (str(pelicula.getNombre())==nombre):
                return pelicula
        return None



    def BuscadorFuncion(self,numero):
        '''
        Recibe un numero de funcion, retorna un objeto de clase Funcion. Su propósito es retornar la
		funcion cuyo numero de cedula concuerde con el ingresado al metodo
        '''
        lista=[]
        for funcion in self._cartelera:
            lista.append(funcion.getNumero())

            if funcion.getNumero()==int(numero):    #Si el numero de la funcion es igual al numero que se ingreso es la que se estaba buscando
                return funcion
        return None

    def BuscadorBoleto (self,num_silla: int,funcion:Funcion):
        '''
        Recibe un numero de silla y una funcion, retorna un objeto de clase Boleto. Su proposito es retornar el
		boleto cuyo numero de silla asociado a una funcion ingresada concuerde con el ingresado.
        '''
        lista=[]
        for boleto in funcion.getBoletos():
            lista.append(boleto.getNum_silla())

            if boleto.getNum_silla==num_silla:  #Si el numero que se ingreso concuerda con el numero de la silla del boleto es el que se estaba buscando
                return boleto
        return None

        
                
	#Metodos para agregar elementos a las listas de la clase Cine

    def agregarCliente(self,nuevo: Cliente):
       self._clientes.append(nuevo)

    def agregarPelicula(self,nuevo: Pelicula):
        self._peliculas.append(nuevo)

    def agregarSala(self,nuevo: Sala):
        self._salas.append(nuevo)

    def agregarFuncion(self,nuevo:Funcion):
        self._cartelera.append(nuevo)     


	
    #
    #Getting and setting
    #



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