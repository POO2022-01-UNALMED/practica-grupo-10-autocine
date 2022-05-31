package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.*;
import java.util.stream.Collectors;
import gestorAplicacion.Taquilla.*;
import gestorAplicacion.Persona.Cliente;
import gestorAplicacion.Salas.Sala;
import gestorAplicacion.Salas.Sala2D;

/**
 * @author Jhon Ever Gallego Atehortua.
 * @param Clase Autocine
 * @summary Clase que contiene las salas, funciones, peliculas, clientes y metodos para la creación, modificación y observacion de los mismos.
 */

// Clase.
public class Autocine implements Serializable {
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	static List<Autocine> autocine;
	static {
		autocine = new ArrayList<Autocine>();
	}
	
	// Atributos.
	private String nombre;
	private static List<Cliente> clientes= new ArrayList<Cliente>();
	private static List<Funcion> cartelera= new ArrayList<Funcion>();
	private List<Pelicula> peliculas= new ArrayList<Pelicula>();
	private List<Sala> salas = new ArrayList<Sala>();
	
	// Constructores.
	public Autocine(String nombre) {
		this.nombre = nombre;
	}
	
	// Metodos.
	/**
	 * 
	 * @param mes
	 * @param dia
	 * @summary Recibe un mes y un dia.
	 * @return Una lista de salas disponibles.
	 */
	public ArrayList<Sala> salasDisponibles(int mes, int dia) {
		ArrayList<Sala> disponibles = new ArrayList<>();
		for(Sala sala: salas) { 
			if(sala.unoDisponible(dia, mes)) {
				disponibles.add(sala);
			}
		}
		return disponibles;
	}

	
	/**
	 * @param pelicula
	 * @param dia
	 * @param mes
	 * @summary Recibe una pelicula, un dia y mes.
	 * @return Una lista de funciones disponibles, que cumpla dichas condiciones.
	 */
	public ArrayList<Funcion> verFuncion(Pelicula pelicula, int dia, int mes) { 
		ArrayList<Funcion> funciones = new ArrayList<Funcion>();
		
		for(Funcion funcion: cartelera) { 
			if(funcion.getPelicula() == pelicula && funcion.getDia() >= dia && funcion.getMes() == mes ) {
				funciones.add(funcion);
			}
		}
		for(Funcion funcion: cartelera) { 
			if(funcion.getPelicula() == pelicula && funcion.getMes() > mes ){
				funciones.add(funcion);
			}
		}
		return funciones;
	}
	
	
	/**
	 * @param cliente
	 * @summary Recibe un cliente.
	 * @return Una lista de funciones disponibles segun el genero mas visto, genero seleccionado por el cliente.
	 */
	public ArrayList<Funcion> verFuncion(Cliente cliente) { 
		ArrayList<Funcion> funciones = new ArrayList<Funcion>();
		
		for(Funcion funcion: cartelera) {
			if(funcion.getPelicula().getGenero() == cliente.GeneroMasVisto()) {	
			}
		}
		return funciones;
	}
	
		
	/**
	 * @param dia
	 * @param mes
	 * @summary Recibe un dia y mes.
	 * @return Una lista de funciones disponibles segun el dia y mes seleccionado.
	 */
	public static ArrayList<Funcion> verFuncion( int dia, int mes) { 
		ArrayList<Funcion> funciones = new ArrayList<Funcion>(); 
		
		for(Funcion funcion: cartelera) {
			if(funcion.getDia() == dia && funcion.getMes() == mes){
				funciones.add(funcion);
			}
		}
		return funciones;
	}

	
	/**
	 * @param mes
	 * @summary Recibe un mes.
	 * @return Una lista de funciones disponibles segun el mes seleccionado.
	 */
	public ArrayList<Funcion> verFuncion(int mes) {	
		ArrayList<Funcion> funciones = new ArrayList<Funcion>(); 
		
		for(Funcion funcion: cartelera) {
			if(funcion.getMes() == mes) {
				funciones.add(funcion);
			}
		}
		return funciones;
	}
	

	/**
	 * @param boleto
	 * @summary Recibe un ticket.
	 * @return Una lista de funciones disponibles segun el ticket relacionado.
	 */
	public ArrayList<Funcion> verFuncion(Ticket ticket) {
		ArrayList<Funcion> funciones = new ArrayList<Funcion>(); 
	
		for(Funcion funcion: cartelera) {
			if(funcion == ticket.getFuncion()) {
				funciones.add(funcion);
			}
		}
		return funciones;
	}


	// Metodos para agregar elementos a las listas de la clase Autocine.
	/**
	 * @summary Metodos para agregar elementos a las listas de la clase Autocine.
	 */
	public void agregarCliente(Cliente nuevo) {
		clientes.add(nuevo);
	}
	public void agregarPelicula(Pelicula nuevo) {
		peliculas.add(nuevo);
	}
	public void agregarSala(Sala nuevo) {
		salas.add(nuevo);
	}
	public void agregarFuncion(Funcion nuevo) {
		cartelera.add(nuevo);
	}

	
	/**
	 * @param num
	 * @summary Recibe una cedula.
	 * @return Verifica si un cliente está en la lista de clientes.
	 */
	public static Boolean verificarCliente(int num) {
		ArrayList<Integer> lista = new ArrayList<Integer>();  
		
		for(Cliente cliente: clientes) {
			lista.add(cliente.getId());
		}
		
		if (lista.contains(num)) {	
			return true;
		}
		else {
			return false;
		}
		
	}
	
	
	/**
	 * @param num
	 * @summary Recibe una cedula.
	 * @return Retorna un objeto cliente cuya cedula concuerde con la ingresada.
	 */
	public static Cliente BuscadorCliente(int num) {
		ArrayList<Integer> lista = new ArrayList<Integer>();
		
		for(Cliente cliente: clientes) {
			lista.add(cliente.getId());
		
			if (cliente.getId() == num) {
				return cliente;
			}
		}
		return null ;
	}
	
	
	/**
	 * @param numero
	 * @summary Recibe un numero de funcion.
	 * @return Retorna un objeto funcion.
	 */
	public Funcion BuscadorFuncion(int numero) {
		ArrayList<Integer> lista = new ArrayList<Integer>();
		
		for(Funcion funcion: cartelera) {
			lista.add(funcion.getNumero());
			
			if(funcion.getNumero() == numero) {	
				return funcion;
			}
		}
		return null ;
	}
	
	
	/**
	 * @param num_silla
	 * @param funcion
	 * @summary Recibe un numero de puesto y una funcion.
	 * @return Un objeto de clase Ticket, cuyo numero de puesto sea igual al ingresado.
	 */
	public Ticket BuscadorTicket(int num_puesto, Funcion funcion) {
		ArrayList<Integer> lista= new ArrayList<Integer>();

		for(Ticket ticket: funcion.getTickets()) {
			lista.add(ticket.getNum_puesto());

			if(ticket.getNum_puesto() == num_puesto) {												
				return ticket;
			}
		}
		return null;
	}
	
	
	/**
	 * @param nombre
	 * @summary Recibe el nombre de una pelicula.
	 * @return Objeto de clase Pelicula, cuyo nombre coincida con el ingresado.
	 */
	public Pelicula BuscadorPelicula(String nombre) {
		ArrayList<String> lista = new ArrayList<String>();
		
		for(Funcion funcion: cartelera) {
			lista.add(funcion.getPelicula().getNombre());
			if (funcion.getPelicula().getNombre().equals(nombre)) {
				return funcion.getPelicula();
			}
		}
		return null ;
	}
	

	/**
	 * @param num
	 * @summary Recibe el numero de sala.
	 * @return Un objeto de clase Sala, cuyo numero coincida con el ingresado.
	 */
	public Sala buscarSala(int num) {
		List<Integer> lista = new ArrayList<Integer>();
		
		for(Sala sala: salas) {
			lista.add(sala.getNumero());
		}
		
		if (lista.contains(num)) {
			return salas.get(lista.indexOf(num));
		}
		else {
			return null;
		}
	}


	// Getters and Setters.
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public List<Cliente> getClientes() {
		return clientes;
	}
	public void setClientes(List<Cliente> clientes) {
		this.clientes = clientes;
	}
	public List<Funcion> getCartelera() {
		return cartelera;
	}
	public void setCartelera(List<Funcion> cartelera) {
		this.cartelera = cartelera;
	}
	public List<Pelicula> getPeliculas() {
		return peliculas;
	}
	public void setPeliculas(List<Pelicula> peliculas) {
		this.peliculas = peliculas;
	}
	public List<Sala> getSalas() {
		return salas;
	}
	public void setSalas(List<Sala> salas) {
		this.salas = salas;
	}
	public static List<Autocine> getAutocine() {
		return autocine;
	}
	public static void setAutocine(List<Autocine> autocine) {
		Autocine.autocine = autocine;
	}
	
	
}