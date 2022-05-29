package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.*;
import java.util.stream.Collectors;
import gestorAplicacion.Taquilla.*;
import gestorAplicacion.Persona.*;
import gestorAplicacion.Salas.*;

/**
 * 
 * @author Jhon Ever Gallego Atehortua.
 * @param Clase Autocine.
 * @summary Clase que contiene las salas, funciones, peliculas, clientes y metodos para la creación, modificación y observacion de los mismos.
 */

// Clase.
public class Autocine implements Serializable {
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	
	// Constantes.
	
	// Atributos.
	private String nombre;
	private List<Cliente> clientes = new ArrayList<Cliente>();
	private List<Funcion> cartelera = new ArrayList<Funcion>();
	private List<Pelicula> peliculas = new ArrayList<Pelicula>();
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
	 * 
	 * @param pelicula
	 * @param dia
	 * @param mes
	 * @summary Recibe una pelicula, un dia y mes. 
	 * @return Una lista de funciones disponibles.
	 */
	public ArrayList<Funcion> verFuncion(Pelicula pelicula, int dia, int mes) {
		ArrayList<Funcion> funciones = new ArrayList<Funcion>();
		
		for (Funcion funcion: cartelera) {
			if(funcion.getPelicula() == pelicula && funcion.getDia() >= dia && funcion.getMes() == mes) {
				funciones.add(funcion);
			}
		}
		
		for (Funcion funcion: cartelera) {
			if(funcion.getPelicula() == pelicula && funcion.getMes() > mes) {
				funciones.add(funcion);
			}
		}
		return funciones;
	}
	
	
	
	
	
	
	
	
}
