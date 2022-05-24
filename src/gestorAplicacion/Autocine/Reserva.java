/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @summary Clase Puesto.
 */

// Clase.

package gestorAplicacion.Autocine;

import java.io.Serializable;
import java.util.ArrayList;
public class Reserva implements Serializable {

    // Serializacion.

    private static final long serialVersionUID = 1L;
    private static ArrayList<Reserva> reservas;
    static {
        reservas = new ArrayList<Reserva>();
    }

    // Atributos.

    private int CANT_MAXIMA_PUESTOS;
    private boolean pagada;
    /** ticket **/

}