package gestorAplicacion.Persona;

/**
 * Clase Cliente, lleva todo lo relativo a la información del espectador
 *
 */
public class Cliente {
 
    /*Atributos*/
    private String nombre;
    private int edad;
    private int id;
    private double dinero;
    
 
    public double getDinero() {
		return dinero;
	}

	public void setDinero(double dinero) {
		this.dinero = dinero;
	}

	/*Constructores*/
    public Cliente(String nombre, int edad, int cedula) {
        this.nombre = nombre;
        this.edad = edad;
        this.id = id;
    }
 
    /*Metodos*/
    public String getNombre() {
        return nombre;
    }
 
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
 
    public int getEdad() {
        return edad;
    }
 
    public void setEdad(int edad) {
        this.edad = edad;
    }
 
    public int getId() {
        return id;
    }
 
    public void setId(int id) {
        this.id = id;
    }
 
    /**
     * Pagamos la entrada del cine
     *
     * @param precio
     */
    public void pagarReserva(double precio) {
        dinero -= precio;
    }
 
    /**
     * Indicamos si el espectador tiene edad para ver la pelicula 
     *
     * @param edadMinima
     * @return
     */
    public boolean tieneEdad(int edadMinima) {
        return edad >= edadMinima;
    }
 
    
    @Override
    public String toString() {
        return "el nombre del cliente es " + this.nombre + " de " + this.edad + " años y con identificación " + id +" y con "+ dinero + " pesos.";
    }
 
}