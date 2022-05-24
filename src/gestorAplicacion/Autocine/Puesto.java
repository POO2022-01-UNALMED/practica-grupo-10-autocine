/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @summary Clase Puesto.
 */

// Clase.

package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.ArrayList;
public class Puesto implements Serializable {

    // Serializacion.

    private static final long serialVersionUID = 1L;
    private static ArrayList<Puesto> puestos;
    static {
        puestos = new ArrayList<Puesto>();
    }

    // Atributos.

    /** posicion : ¿una lista? **/
    private String tipo; /** algo como estandar y premiun **/
    private String Estado; /** pagado, reservado y libre **/
}
