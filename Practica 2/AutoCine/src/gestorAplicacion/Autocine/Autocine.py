#**
#* @author: Jhon Ever Gallego Atehortua.
#* @param: Clase Autocine.
#* @summary: Clase Autocine. Clase que contiene as salas, funciones, peliculas, cientes y metodos para a creación, modificación y observación de los mismos.
#**

from gestorAplicacion.Taquilla.Funcion import Funcion
from gestorAplicacion.Taquilla.Pelicula import Pelicula
from gestorAplicacion.Taquilla.Funcion import Horario
from gestorAplicacion.Taquilla.Ticket import Ticket
from gestorAplicacion.Salas.Sala import Sala
from gestorAplicacion.Persona.Cliente import Cliente

# Clase.
class Autocine:
    
    # Atributos.
    def __init__(self, nombre):
        self._nombre = nombre
        self._clientes = []
        self._cartelera = []
        self._peliculas = []
        self._salas = []
       
        
    # Metodos.
    #**
	#* @param mes
	#* @param dia
	#* @summary Recibe un mes y un dia.
	#* @return Una lista de salas disponibles.
	#**
    def salasDisponibles(self, mes: int, dia: int):
        disponibles = list()
        
        for sala in self._salas:
            if Sala.unoDisponible(mes, dia):
                disponibles.append(sala)
                
        return disponibles
    
    
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

        if (len(args) == 3):
            pelicula: Pelicula = args[0]
            dia, mes = args[1:]
            for funcion in self.getCartelera():
                if(Funcion.getPelicula() == pelicula and Funcion.getDia() >= dia and Funcion.getMes() == mes):
                    funciones.append(funcion)
            for funcion in self.getCartelera():
                if(Funcion.getPelicula() == pelicula and Funcion.getMes() > mes):
                    funciones.append(funcion)

        # Este es el que recibe dia, mes.
        elif(len(args) == 2):
            dia, mes = args
            for funcion in self.getCartelera():
                if(Funcion.getDia() == dia and Funcion.getMes() == mes):
                    funciones.append(funcion)
        elif(len(args) == 1):
    
            # Recibe mes.
            if(type(args[0]) == int):
                mes = args[0]
                for funcion in self.getCartelera():
                    if(Funcion.getMes() == mes):
                        funciones.append(funcion)    
           
            # Recibe cliente. 
            else:
                cliente: Cliente = args[0]
                for funcion in self.getCartelera():
                   if(Funcion.getPelicula().getGenero() == cliente.GeneroMasVisto()):
                       funciones.append(funcion)
                       
        return funciones
    
    
    # Metodos para agregar elementos a las listas de la clase Autocine.
    #**
	#* @summary Metodos para agregar elementos a las listas de la clase Autocine.
	#**
    def agregarCliente(self, nuevo: Cliente):
       self._clientes.append(nuevo)

    def agregarPelicula(self, nuevo: Pelicula):
        self._peliculas.append(nuevo)

    def agregarSala(self, nuevo: Sala):
        self._salas.append(nuevo)

    def agregarFuncion(self, nuevo:Funcion):
        self._cartelera.append(nuevo)
    
    
    #**
	#* @param num
	#* @summary Recibe una cedula.
	#* @return Verifica si un cliente está en la lista de clientes.
	#**
    def verificarCliente(self, num: int) -> bool:
        lista : list = []
        
        for Cliente in self.getClientes():
            lista.append(Cliente.getId())
        
        return num in lista
    
    
    #**
	#* @param num
	#* @summary Recibe una cedula.
	#* @return Retorna un objeto cliente cuya cedula concuerde con la ingresada.
	#**
    def buscadorCliente(self, num : int):
        lista = self.getClientes()
        for cliente in lista:
            if (int(Cliente._id)== int(num)):
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
            if (int(Sala.getNumero())== int(num)):
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
            if (str(Pelicula.getNombre())==nombre):
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
            lista.append(Funcion.getNumero())
            if Funcion.getNumero()==int(numero): 
                return funcion
            
        return None


    #**
	#* @param num_silla
	#* @param funcion
	#* @summary Recibe un numero de puesto y una funcion.
	#* @return Un objeto de clase Ticket, cuyo numero de puesto sea igual al ingresado.
	#**
    def BuscadorTicket (self, num_puesto: int, funcion:Funcion):
        lista=[]
        for ticket in funcion.getTickets():
            lista.append(Ticket.getNum_puesto())

            if Ticket.getNum_puesto == num_puesto:  
                return ticket
            
        return None
    
    
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