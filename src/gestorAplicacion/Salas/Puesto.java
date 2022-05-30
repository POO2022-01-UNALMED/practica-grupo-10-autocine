/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @param clase Puesto.
 * @summary Clase que tiene la imformacion relacionada con los puestos.
 */
package gestorAplicacion.Salas;
import gestorAplicacion.Taquilla.Pelicula;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

//clase
public class Puesto implements Serializable{

    //serializacion

    private static final long serialVersionUID = 1L;
    static List<Puesto> puestos;
    static {
        puestos = new ArrayList<Puesto>();
    }

    //tipo

    public enum Tipo {PREFERENCIAL, GENERAL}

    //atributos

    private Tipo tipo;
    private int numero;
    private float precio;

    //metodos

    public Puesto(String tipo, int numero) {
        setTipo(tipo);
        setNumero(numero);
    }

    //gets y sets
    public Tipo getTipo() {
        return tipo;
    }

    public void setTipo(String Tipo) {
        if(tipo.equals("PREFERENCIAL")) {
            this.tipo = tipo.PREFERENCIAL;
        }
        else{
            this.tipo = tipo.GENERAL;
        }
    }
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }

    public float getPrecio() {
        if (this.tipo == tipo.PREFERENCIAL) {
            return 25000;
        }
        else{
            return 15000;
        }
    }
    public void setPrecio(float precio) {
        this.precio = precio;
    }
    public static List<Puesto> getPuestos() {
        return puestos;
    }

    public static void setPuestos(List<Puesto> puestos) {
        Puesto.puestos = puestos;
    }
}
