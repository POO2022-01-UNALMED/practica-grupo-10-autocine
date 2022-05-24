package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * 
 * @author Jhon Ever Gallego Atehortua.
 * @summary Clase Carro.
 */

// Clase.
public class Carro implements Serializable {
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	private static ArrayList<Carro> carros;
	static {
		carros = new ArrayList<Carro>();
	}
	
	
	// Atributos.
	private String placa;
	
	// Constructor.
	public Carro(String placa) {
		this.placa = placa;
	}

	// Getters and Setters.
	public String getPlaca() {
		return placa;
	}
	public void setPlaca(String placa) {
		this.placa = placa;
	}
	public static ArrayList<Carro> getCarros() {
		return carros;
	}
	public static void setCarros(ArrayList<Carro> carros) {
		Carro.carros = carros;
	}
}