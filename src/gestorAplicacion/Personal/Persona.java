package gestorAplicacion.Personal;
import java.util.List;
import java.util.Arrays;

public abstract class Persona {
	
	protected String nombre;
	protected int cedula;
	protected List[] empleados;
	protected List[] clientes;
	
	public Persona() {
		
		nombre="";
		cedula = 0;
		empleados = null;
		clientes = null;
		
	}
	
	public Persona(String nombre, int cedula, List[] empleados, List[] clientes ) {
			
		this.nombre = nombre;
		this.cedula = cedula;
		this.empleados = empleados;
		this.clientes = clientes;
	}
	
	@Override
	public abstract String toString();
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getCedula() {
		return cedula;
	}
	public void setCedula(int cedula) {
		this.cedula = cedula;
	}
	public List[] getEmpleados() {
		return empleados;
	}
	public void setEmpleados(List[] empleados) {
		this.empleados = empleados;
	}
	public List[] getClientes() {
		return clientes;
	}
	public void setClientes(List[] clientes) {
		this.clientes = clientes;
	}

	

}
