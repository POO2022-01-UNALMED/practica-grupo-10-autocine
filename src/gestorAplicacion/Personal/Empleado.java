package gestorAplicacion.Personal;
import java.util.List;
import java.util.Arrays;
import java.util.*;

public class Empleado {
		
	protected String nombre;
	protected int cedula;
	protected List[] empleados;
	
	public String toString() {
        return "Nombre del empleado:" + this.nombre + ", "
                + "Cédula:" + this.cedula + ", " + "empleados"
                + this.empleados;
    }
}
