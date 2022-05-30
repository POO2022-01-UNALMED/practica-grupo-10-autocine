package gestorAplicacion.Salas;
import java.io.Serializable;
import java.util.*;
import gestorAplicacion.Autocine.*;

public class Sala2D extends Sala implements Serializable{
	// Serializacion.
		private static final long serialVersionUID = 1L;
		static List<Sala2D> salas2D;
		static {
			salas2D= new ArrayList<Sala2D>();
		}
	
	public Sala2D(int filas, int columnas, int filasPreferencial, Autocine autocine) {
		super(filas, columnas, filasPreferencial, 2000, autocine);
	}
	
	public Sala2D(int preferencial, Autocine autocine) {
		this(8, 12, preferencial, autocine);
	}
	
	public int cantidadPuestos() {
	/*No recibe nada y devuelve un entero el cual corresponde a la cantidad de puestos
	disponibles*/

		return super.puestos.size();
	}
	
	public void crearPuestos() {			
	/*No recibe ningun parametro y no retorna nada
	Crea cada puesto según la cantidad de filas prefencial, filas, y columnas*/
		
		int total = filas*columnas; 	//numero de puestos

		int totalpreferencial = filasPreferencial*columnas; //numero de puestos prefe y se le resta 1 cada que se compre uno
													
		String tipo = "PREFENCIAL";
		
		for(int i = 0;i<total;i++) {	//for que itera la cantidad de puestos 
			
		   if(totalpreferencial<=0) {	//si se acabaron los preferencial cambia tipo a GENERAL
			 tipo = "GENERAL";
			}
		   else {				//sino  se reduce totalpreferencial en uno
			 totalpreferencial--;
			}
			
		   Puesto puesto = new Puesto(tipo,i+1);	
											
		   puestos.add(puesto);					
		}
	}
	
	//get y set
	public static List<Sala2D> getSalas2D() {
		return salas2D;
	}
	public static void setSalas2D(List<Sala2D> salas2d) {
		salas2D = salas2d;
	}

}
