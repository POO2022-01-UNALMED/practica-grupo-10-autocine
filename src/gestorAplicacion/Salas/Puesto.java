/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @param clase Puesto.
 * @summary Clase que tiene la imformacion relacionada con los puestos.
 */
package gestorAplicacion.Salas;
import java.io.Serializable;

//clase
public class Puesto implements Serializable{

    //serializacion

    private static final long serialVersionUID = 1L;

    //tipo

    public enum Tipo {Preferencial, Estandar}

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

    public void setTipo(Tipo tipo) {
        if(tipo.equals("Preferencial")) {
            this.tipo = tipo.Preferencial;
        }
        else{
            this.tipo = tipo.Estandar;
        }
    }
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }

    public float getPrecio() {
        if (this.tipo == tipo.Preferencial) {
            return 25000;
        }
        else{
            return 15000;
        }
    }
    public void setPrecio(float precio) {
        this.precio = precio;
    }
}
