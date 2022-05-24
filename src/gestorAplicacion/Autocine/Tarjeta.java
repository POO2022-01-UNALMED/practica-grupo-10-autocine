package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * 
 * @author Jhon Ever Gallego Atehortua.
 * @summary Clase tarjeta.
 */

// Clase.
public class Tarjeta implements Serializable{ 
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	private static ArrayList<Tarjeta> tarjetas;
	static {
		tarjetas = new ArrayList<Tarjeta>();
	}
	
	// Constantes.
	public static final double CARGA_INICIAL = 50000;
	public static final double RECARGA = 3000;
	public static final double DESCUENTO = 0.1;
	
	// Atributos.
	private String cedula;
	private double saldo;
	
	// Constructores.
	public Tarjeta(String cedula, double saldo) {
		this.cedula = cedula;
		this.saldo = saldo;
		tarjetas.add(this);
	}
	
	public Tarjeta() {
		this("", 0);
	}

	// Getters and Setters.
	public String getCedula() {
		return cedula;
	}
	public void setCedula(String cedula) {
		this.cedula = cedula;
	}
	public double getSaldo() {
		return saldo;
	}
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	public static ArrayList<Tarjeta> getTarjetas() {
		return tarjetas;
	}
	public static void setTarjetas(ArrayList<Tarjeta> tarjetas) {
		Tarjeta.tarjetas = tarjetas;
	}
	
	// Metodos.
	public String darCedula() {
		return cedula;
	}
	
	public double darSaldo() {
		return saldo;
	}
	
	public void descontar(double cantidad) throws Exception {
		if (cantidad > saldo) {
			throw new Exception("La tarjeta no tiene saldo suficiente.");
		}
		saldo -= cantidad;
	}
	
	public void cargar(double cantidad) {
		saldo += cantidad;
	}
	
	public void recargar() {
		saldo += RECARGA;
	}
	
	public String toString() {
		return "Cedula: " + cedula;
	}
	
}