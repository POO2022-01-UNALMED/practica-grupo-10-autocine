package gestorAplicacion.Taquilla;
import java.io.Serializable;
import java.util.*;

import gestorAplicacion.Salas.Puesto;
import gestorAplicacion.Salas.Puesto.Tipo;
import gestorAplicacion.Persona.Cliente;

/**
 * @author Jimena Uribe Giraldo.
 * @summary En esta clase todo lo relacionado a Ticket (Boleto), puesto, precio, función
 */
public class Ticket implements Serializable{
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	static List<Ticket> tickets;
	static {
		tickets = new ArrayList<Ticket>();
	}
	
	//Atributos 
	
	private int num_puesto;
	private Tipo tipo_puesto; 
	private static float precioTotal;
	private static boolean estado;
	private static Funcion funcion;
	private static float precio_puesto;
	
	
	public Ticket(Funcion funcion, Puesto puesto) {
		Ticket.funcion = funcion;
		this.set_puesto(puesto);
		Ticket.estado = true;
		Ticket.precioTotal = Ticket.calcularPrecio();
	}
	
	public static float calcularPrecio() {		
		/*No recibe nada y devuelve un float el cual corresponde al calculo del precio del boleto 
		que depende del precio de la sala y el precio del puesto */
		
			float precio_t = Funcion.getSala().getPrecio() + precio_puesto;	 	// Se suma el precio de la sala y el precio de la silla
			
			return precio_t;
		}
	
	public static void calcularPrecioDefinitivo(Cliente cliente) {
		
		float total= calcularPrecio(); 
		setPrecioTotal(total);				
	}
	
	public String estado() {
	/* Sin parÃ¡metros y retorna un String que corresponde al estado de disponibilidad
	 del ticket	
	 */
		if(estado) {	//Si la estÃ¡ disponible imprime Libre, si no ocupado 
			return "Libre";
		}
		return "Ocupado";		
	}
	
	
	public String tipoString() {
		/*Sin parÃ¡metros  y retorna un String el cual indica el tipo de puesto del ticket
		 */
		if(tipo_puesto==Tipo.PREFERENCIAL) {	//El tipo de la puesto es Preferencial retornara P, si no General
			return "P";
		}
		return "G";
	}

	
	// get y set
	
	

	public float getPrecio_puesto() {
		return precio_puesto;
	}
	
	public float getPrecioTotal() {
		return precioTotal;
	}

	public static void setPrecioTotal(float precioTotal) {
		Ticket.precioTotal = precioTotal;
		
	}
	public static boolean isEstado() {
		return estado;
	}
	public static void setEstado(boolean estado) {
		Ticket.estado = estado;
	}
	public static Funcion getFuncion() {
		return funcion;
	}
	public void setFuncion(Funcion funcion) {
		Ticket.funcion = funcion;
	}

	public int getNum_puesto() {
		return num_puesto;
	}

	private void set_puesto(Puesto puesto) {	
		/*Recibe el puesto con el que se asignan los atributos de num,tipo
		  y precio y no devuelve nada	
		 */

		this.num_puesto = puesto.getNumero();			
		this.setTipo_puesto(puesto.getTipo());		
		this.setPrecio_puesto(puesto.getPrecio());	
		}

	public void setPrecio_puesto(float precio) {
		Ticket.precio_puesto=precio;
	}

	public Tipo getTipo_puesto() {
		return tipo_puesto;
	}

	public void setTipo_puesto(Tipo tipo_puesto) {
		this.tipo_puesto = tipo_puesto;
	}
	
	public static List<Ticket> getTicket() {
		return tickets;
	}
	public void setTicket(List<Ticket> tickets) {
		Ticket.tickets = tickets;
	}
	
}
