package gestorAplicacion.Taquilla;
import java.io.Serializable;

import gestorAplicacion.Salas.Puesto;
import gestorAplicacion.Salas.Puesto.Tipo;
import gestorAplicacion.Persona.Cliente;


public class Ticket implements Serializable{
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	static List<Ticket> ticket;
	static {
		aticket = new ArrayList<Ticket>();
	}
	
	//Atributos 
	
	private int num_puesto;
	private Tipo tipo_puesto; 
	private float precioTotal;
	private boolean estado;
	private Funcion funcion;
	private float precio_puesto;
	
	
	public Ticket(Funcion funcion, Puesto puesto) {
		this.funcion = funcion;
		this.set_puesto(puesto);
		this.estado = true;
		this.precioTotal = this.calcularPrecio();
	}
	
	public float calcularPrecio() {		
		/*No recibe nada y devuelve un float el cual corresponde al calculo del precio del boleto 
		que depende del precio de la sala y el precio del puesto */
		
			float precio_t=funcion.getSala().getPrecio()+precio_puesto;	 	// Se suma el precio de la sala y el precio de la silla
			
			return precio_t;
		}
	
	public void calcularPrecioDefinitivo(Cliente cliente) {
		
		float total= calcularPrecio(); 
		this.setPrecioTotal(total);				
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

	public void setPrecioTotal(float precioTotal) {
		this.precioTotal = precioTotal;
		
	}
	public boolean isEstado() {
		return estado;
	}
	public void setEstado(boolean estado) {
		this.estado = estado;
	}
	public Funcion getFuncion() {
		return funcion;
	}
	public void setFuncion(Funcion funcion) {
		this.funcion = funcion;
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
		this.precio_puesto=precio;
	}

	public Tipo getTipo_puesto() {
		return tipo_puesto;
	}

	public void setTipo_puesto(Tipo tipo_puesto) {
		this.tipo_puesto = tipo_puesto;
	}
	
}
