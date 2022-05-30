package gestorAplicacion.Persona;
import java.io.Serializable;
import java.util.*;
import gestorAplicacion.Taquilla.*;
import gestorAplicacion.Autocine.*;


/**
 * Clase Cliente, lleva todo lo relativo a la información del espectador
 *
 */
public class Cliente implements Serializable {
 
    /*Atributos*/
    private String nombre;
    private int edad;
    private int id;
    private double dinero;
    private static final long serialVersionUID = 1L;
	private String ocupacion;
	private List<Ticket> historialCompras= new ArrayList<Ticket>(); //una lista con los boletos que ha comprado el cliente en su vida
	private Autocine autocine;
    
 
    public double getDinero() {
		return dinero;
	}

	public void setDinero(double dinero) {
		this.dinero = dinero;
	}

	/*Constructores*/
    public Cliente(String nombre, int edad, int id, Autocine autocine) {
        this.nombre = nombre;
        this.edad = edad;
        this.id = id;
        this.autocine=autocine;
    }
    
    public String GeneroMasVisto() {
		/*
		No recibe nada y devuelve string del género más visto del cliente
		 */
		List<String> genreList=new ArrayList<String>();		//lista con los generos que ha visto el cliente
		for(Ticket ticket: historialCompras) {
			genreList.add(ticket.getFuncion().getPelicula().getGenero()); 	//Recorre el historial de compras del cliente y anexa de los boletos sus generos
		}
		List<Integer> veces=new ArrayList<Integer>();		//lista para guardar la frecuencia de cada genero
		for(String genre: genreList) {
			int num = Collections.frequency(genreList, genre);	//De la lista de géneros extrae la frecuencia de cada elemento
			veces.add(num);
		}
		
		return genreList.get(veces.indexOf(Collections.max(veces))); 	//se devuelve el genero de la lista que tenga el indice correspondiente al maximo de las ocurrencias de cada genero
		
	}
    
 
    /*set y get*/
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
     * 
     */
    public void pagarReserva(double precio) {
        dinero -= precio;
    }
 
    /**
     * Indicamos si el espectador tiene edad para ver la pelicula 
     *

     */
    public boolean tieneEdad(int edadMinima) {
        return edad >= edadMinima;
    }
    
    public List<Ticket> getHistorialCompras() {
		return historialCompras;
	}
	public void setHistorialCompras(List<Ticket> historialCompras) {
		this.historialCompras = historialCompras;
	}


	public Autocine getAutocine() {
		return autocine;
	}

	public void setAutocine(Autocine autocine) {
		this.autocine = autocine;
	}
	
 
    
    @Override
    public String toString() {
        return "el nombre del cliente es " + this.nombre + " de " + this.edad + " años y con identificación " + id +" y con "+ dinero + " pesos.";
    }
 
}
