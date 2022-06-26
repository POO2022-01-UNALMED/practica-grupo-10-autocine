/**
 * @author Daniel Alejandro Giraldo Giraldo.
 * @param clase Sala.
 * @summary Clase que tiene la imformacion relacionada con las salas.
 */
package gestorAplicacion.Salas;
import gestorAplicacion.Autocine.Autocine;
import gestorAplicacion.Taquilla.Funcion;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//clase

public abstract class Sala implements Serializable {

    //serializador
    private static final long serialVersionUID = 1L;
    static List<Sala> salass;
    static {
        salass = new ArrayList<Sala>();
    }

        //atributos
        protected int numero;
        protected int filas;
        protected int columnas;
        protected int filasPreferencial;
        protected float precio;
        protected Autocine autocine;

        protected ArrayList<Puesto> puestos = new ArrayList<Puesto>();

        protected ArrayList<Funcion> funciones = new ArrayList<Funcion>();

        //Constructores

    public Sala( int filas, int columnas, int filaspreferencial, int precio, Autocine autocine){
            this.filas = filas;
            this.columnas = columnas;
            this.filasPreferencial = filaspreferencial;
            this.precio = precio;
            this.autocine = autocine;


            this.crearPuestos();

            Autocine.agregarSala(this);

            this.numero = Autocine.getSalas().size();
        }


        //Metodos abtractos


        public abstract int cantidadPuestos ();

        public abstract void crearPuestos ();

        //Metodos

        public void agregarFuncion (Funcion funcion){
            funciones.add(funcion);
        }

        public boolean verificarDisponibilidad ( int dia, int mes){
            String consulta = "" + dia + mes;
            ArrayList<String> fechas = new ArrayList<String>();
            ArrayList<String> horarios = new ArrayList<String>();
            ArrayList<String> disponibles = new ArrayList<>(
                    Arrays.asList("12:00", "14:00",
                            "16:00", "18:00", "20:00", "22:00"));
            for (Funcion func : funciones) {
                String info = "" + func.getDia() + func.getMes();
                fechas.add(info);
                info = "";

            }

            for (int i = 0; i < fechas.size(); i++) {
                if (fechas.get(i).equals(consulta)) {
                    horarios.add(funciones.get(i).getHorario());
                }
            }

            for (String horario : horarios) {
                disponibles.remove(horario);
            }

            String respuesta = "";

            for (String d : disponibles) {
                respuesta += d + "\n";
            }

            return respuesta.equals("12:00\n14:00\n16:00\n18:00\n20:00\n22:00\n");
        }

        public boolean verificarDisponibilidad ( int dia, int mes, String hora){


            String consulta = dia + "/" + mes + "/" + hora;

            ArrayList<String> fechasfunciones = new ArrayList<String>();
            for (Funcion func : funciones) {
                String info = func.getDia() + "/" + func.getMes() + "/" + func.getHorario();
                fechasfunciones.add(info);

                info = "";
            }

            for (String i : fechasfunciones) {
                if (i.equals(consulta)) {
                    return false;
                }
            }

            return true;
        }
        public boolean unoDisponible ( int dia, int mes){


            String consulta = "" + dia + mes;

            ArrayList<String> fechas = new ArrayList<String>();


            ArrayList<String> horarios = new ArrayList<String>();


            ArrayList<String> disponibles = new ArrayList<>(
                    Arrays.asList("12:00", "14:00",
                            "16:00", "18:00", "20:00", "22:00"));

            for (Funcion func : funciones) {
                String info = "" + func.getDia() + func.getMes();
                fechas.add(info);
                info = "";

            }

            for (int i = 0; i < fechas.size(); i++) {
                if (fechas.get(i).equals(consulta)) {
                    horarios.add(funciones.get(i).getHorario());
                }
            }

            for (String horario : horarios) {
                disponibles.remove(horario);
            }

            String respuesta = "";

            for (String d : disponibles) {
                respuesta += d + "\n";
            }

            if (respuesta.length() >= 5) {
                return true;
            } else {
                return false;
            }
        }
        public String verHorarios ( int dia, int mes){

            String consulta = "" + dia + mes;
            ArrayList<String> fechas = new ArrayList<String>();
            ArrayList<String> horarios = new ArrayList<String>();
            ArrayList<String> disponibles = new ArrayList<>(Arrays.asList("12:00", "14:00", "16:00", "18:00", "20:00", "22:00"));

            for (Funcion func : funciones) {

                String info = "" + func.getDia() + func.getMes();
                fechas.add(info);
                info = "";

            }

            for (int i = 0; i < fechas.size(); i++) {
                if (fechas.get(i).equals(consulta)) {
                    horarios.add(funciones.get(i).getHorario());
                }
            }

            for (String horario : horarios) {
                disponibles.remove(horario);
            }

            String respuesta = "";

            for (String d : disponibles) {
                respuesta += d + "\n";
            }

            return respuesta;

        }


        //
        //getting and setting
        //

        public String getTipo () {
            /*returna el tipo en String*/

            if (this instanceof Sala2D) {
                return "2D";
            } else {
                return "3D";
            }
        }
        public int getNumero () {
            return numero;
        }

        public void setNumero ( int numero){
            this.numero = numero;
        }

        public int getFilas () {
            return filas;
        }

        public void setFilas ( int filas){
            this.filas = filas;
        }

        public int getColumnas () {
            return columnas;
        }

        public void setColumnas ( int columnas){
            this.columnas = columnas;
        }

        public int getFilasPreferencial () {
            return filasPreferencial;
        }

        public void setFilasPreferencial ( int filasPreferencial){
            this.filasPreferencial = filasPreferencial;
        }

        public float getPrecio () {
            return precio;
        }

        public void setPrecio ( float precio){
            this.precio = precio;
        }

        public Autocine getAutocine () {
            return autocine;
        }

        public void setAutocine (Autocine autocine){
            this.autocine = autocine;
        }

        public ArrayList<Puesto> getPuestos () {
            return puestos;
        }

        public void setPuestos (ArrayList < Puesto > puestos) {
            this.puestos = puestos;
        }
        public static List<Sala> getSalas() {
            return salass;
        }
        public static void setSalas(List<Sala> salas) {
            Sala.salass = salas;
        }
    }
