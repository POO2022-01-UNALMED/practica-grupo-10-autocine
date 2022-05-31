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
 
	// Serializacion.
	 	private static final long serialVersionUID = 1L;
	 	static List<Cliente> clientes;
	 	static {
	 		clientes = new ArrayList<Cliente>();
	 	}
	 	
    /*Atributos*/
    private int id;
    private String nombre;
    private int edad;
    private List<Ticket> historialCompras= new ArrayList<Ticket>(); //una lista con los boletos que ha comprado el cliente en su vida
    private Autocine autocine;
    
 
	/*Constructores*/
    public Cliente(int id, String nombre, int edad, Autocine autocine) {
		this.id = id;
		this.nombre = nombre;
		this.edad = edad;
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
			int occ = Collections.frequency(genreList, genre);	//De la lista de géneros extrae la frecuencia de cada elemento
			veces.add(occ);
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
	
	public static List<Cliente> getClientes() {
		return clientes;
	}

    
    @Override
	public String toString() {
		
		return "Cliente: " + nombre + "-" + String.valueOf(edad);
		
	}
 
}
