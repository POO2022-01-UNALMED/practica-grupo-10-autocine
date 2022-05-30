package gestorAplicacion.Salas;
import java.io.Serializable;
import java.util.*;
import gestorAplicacion.Autocine.*;

public class Sala2D extends Sala implements Serializable{
	private static final long serialVersionUID = 1L;
	
	public Sala2D(int filas, int columnas, int filaspreferencial, Autocine autocine) {
		super(filas, columnas, filaspreferencial, 2000, autocine);
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

		int totalpreferencial = filaspreferencial*columnas; //numero de puestos prefe y se le resta 1 cada que se compre uno
													
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

}
