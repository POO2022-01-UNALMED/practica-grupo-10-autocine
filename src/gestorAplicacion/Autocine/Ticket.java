package gestorAplicacion.Autocine;
import java.io.Serializable;
import gestorAplicacion.salas.Puesto;
import gestorAplicacion.salas.Tipo;


public class Ticket implements Serializable{
	private static final long serialVersionUID = 1L;
	
	//Atributos 
	
	private int num_puesto;
	private Tipo tipo_puesto; 
	private float precio_puesto;
	private boolean estado;
	private Pelicula pelicula;
	
	
	public void Boleto(Pelicula pelicula, Puesto puesto) {
		this.pelicula = pelicula;
		this.set_puesto(puesto);
		this.estado = true;
		this.precio_puesto = this.precio_puesto();
	}
	
	public String estado() {
	/* Sin parámetros y retorna un String que corresponde al estado de disponibilidad
	 del ticket	
	 */
		if(estado) {	//Si la está disponible imprime Libre, si no ocupado 
			return "Libre";
		}
		return "Ocupado";		
	}
	
	
	public String tipoString() {
		/*Sin parámetros  y retorna un String el cual indica el tipo de puesto del ticket
		 */
		if(tipo_puesto==Tipo.PREFERENCIAL) {	//El tipo de la puesto es Preferencial retornara P, si no General
			return "P";
		}
		return "G";		

	
	// get y set
	
	

	public float getPrecio_puesto() {
		return precio_puesto;
	}

	
	public boolean isEstado() {
		return Estado;
	}
	public void setEstado(boolean estado) {
		this.Estado = estado;
	}
	public Pelicula getPelicula() {
		return Pelicula;
	}
	public void setPelicula(Pelicula pelicula) {
		this.pelicula = pelicula;
	}

	public int getNum_puesto() {
		return num_puesto;
	}

	private void set_puesto(puesto puesto) {	
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
