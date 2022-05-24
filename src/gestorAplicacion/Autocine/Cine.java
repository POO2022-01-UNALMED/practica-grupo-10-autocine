/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @summary Clase Puesto.
 */

// Clase.

package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.ArrayList;
public class Cine implements Serializable {

    // Serializacion.

    private static final long serialVersionUID = 1L;
    private static ArrayList<Cine> cines;
    static {
        cines = new ArrayList<Cine>();
    }

    // Atributos.

    private int Salas;
    /** tienda **/
}