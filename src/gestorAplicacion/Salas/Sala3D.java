package gestorAplicacion.Salas;

import java.io.Serializable;
import gestorAplicacion.Autocine.*;

/**
 * 
 * @author Jhon Ever Gallego Atehortua.
 * @param Clase Sala3D.
 * @summary Clase que que hereda de la Clase Sala. En esta se crean los puestos para la Sala 3D.
 */

// Clase.
public class Sala3D extends Sala implements Serializable {
	
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	
	
	// Atributos.
	private int cantidadGafas;
	
	
	// Contructores.
	public Sala3D(int filas, int columnas, int cantidadGafas, Autocine autocine) {
		super(filas, columnas, 0, 5000, autocine);
		this.cantidadGafas = cantidadgafas;
	}
	
	public Sala3D(int filas, int columnas, Autocine autocine) {
		this(filas, columnas, filas*columnas, autocine);
	}
	
	
	// Metodos.
	/**
	 * 
	 * @summary Da la cantidad de puestos disponibles para su creacion segun la disponibilidad de gafas 3D.
	 * @return La cantidad de puestos disponibles para la creacion de una funcion.
	 */
	public int cantidadPuestos() {
		int totalpuestos = puestos.size();
		if(totalpuestos < cantidadGafas) {
			return totalpuestos;
		}
		return cantidadGafas;
	}
	
	
	/**
	 * 
	 * @summary Metodo para crear los puestos dependiendo la cantidad de filas y columnas.
	 */
	public void crearPuestos() {
		int total = filas*columnas;
		String tipo = "PREFERENCIAL";
		for(int i = 0; i < total; i++) {
			Puesto puesto = new Puesto(tipo, i+1);
			puestos.add(puesto);
		}
	}
	

	// Getters and Setters.
	public int getCantidadGafas() {
		return cantidadGafas;
	}
	public void setCantidadGafas(int cantidadGafas) {
		this.cantidadGafas = cantidadGafas;
	}
	
	
	
}