/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @param clase Pelicula.
 * @summary Clase que tiene la imformacion relacionada con las peliculas.
 */

package gestorAplicacion.Taquilla;
import java.io.Serializable;

// clase
public class Pelicula implements Serializable {

    // serializacion
    private static final long serialVersionUID = 1L;

    //artributos

    private String nombre;
    private String genero;
    private int duracion;
    private String lenguaje;
    private int clasificacion;
    private Autocine autocine;

// constructor

    public Pelicula(String nombre, String genero, int duracion, String lenguaje, int clasificacion, Autocine autocine) {
        this.nombre = nombre;
        this.genero = genero;
        this.duracion = duracion;
        this.lenguaje = lenguaje;
        this.clasificacion = clasificacion;//
        this.Autocine = autocine;
        autocine.agregarPelicula(this);
    }

    // gets y sets
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getGenero() {
        return genero;
    }
    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getDuracion() {
        return duracion;
    }
    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    public String getLenguaje() {
        return lenguaje;
    }
    public void setLenguaje(String lenguaje) {
        this.lenguaje = lenguaje;
    }

    public int getClasificacion() {
        return clasificacion;
    }
    public void setClasificacion(int clasificacion) {
        this.clasificacion = clasificacion;
    }
}