package gestorAplicacion.Autocine;

// Clase.
public class Tarjeta { 
	
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
		return "C.C: " + cedula;
	}
	
}