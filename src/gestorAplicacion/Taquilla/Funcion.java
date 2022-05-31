package gestorAplicacion.Taquilla;

import java.io.Serializable;
import java.util.*;
import gestorAplicacion.Autocine.*;
import gestorAplicacion.Persona.*;
import gestorAplicacion.Salas.*;

/**
 * @author Jhon Ever Gallego Atehortua.
 * @param Clase Funcion.
 * @summary Clase que representa la funcion en la que se da una pelicula.
 */

// Clase.
public class Funcion implements Serializable {
	
	// Serializacion.
	private static final long serialVersionUID = 1L;
	static List<Funcion> funciones;
	static {
		funciones = new ArrayList<Funcion>();
	}
	
	// Enum Horario.
	/**
	 * 
	 * @summary Enum con los horarios.
	 *
	 */
	public enum Horario{
		UNO("12:00"), DOS("14:00"), TRES("16:00"), CUATRO("18:00"), CINCO("20:00"), SEIS("22:00");
		private String hora;

		private Horario(String hora) {
			this.setHora(hora);
		}
		
		public static Horario getHorario(String hora) {
			Horario[] horarios = {UNO, DOS, TRES, CUATRO, CINCO, SEIS};
			for(Horario horario: horarios) {
				if(hora.equals(horario.getHora())) {
					return horario;
				}
			}
			return null;
		}
		
		// Getters and Setters del enum Horario.
		public String getHora() {
			return hora;
		}
		public void setHora(String hora) {
			this.hora = hora;
		}
	}
	
	// Atributos.
	private static int dia;
	private static int mes;
	private static Horario horario;
	private static Pelicula pelicula;
	private static Sala sala;
	private Autocine autocine;
	private ArrayList<Ticket> tickets = new ArrayList<Ticket>();
	private int cantidadTicketsVendidos = 0;
	private static int cantidadFunciones;
	private static int numero;
	
	// Contructor.
	private Funcion(int dia, int mes, Horario horario, Pelicula pelicula, Sala sala, Autocine autocine) {
		Funcion.dia = dia;
		Funcion.mes = mes;
		Funcion.horario = horario;
		Funcion.pelicula = pelicula;
		Funcion.numero = cantidadFunciones;
		this.setSala(sala);
		this.setAutocine(autocine);
		this.crearTicket();
		Autocine.agregarFuncion(this);
		sala.agregarFuncion(this);
		cantidadFunciones ++;
	}
	
	// Metodos.
	/**
	 * @param dia
	 * @param mes
	 * @param horario
	 * @param pelicula
	 * @param num_sala
	 * @param autocine
	 * @summary Recibe una fecha: (dia, mes, horario), pelicula, numero de sala y el autocine. 
	 * @return Una funcion para una pelicula.
	 */
	public static Funcion crearFuncion(int dia, int mes, Horario horario, Pelicula pelicula, int num_sala, Autocine autocine) {
		Sala sala = Autocine.buscarSala(num_sala);
		if(sala != null) {
			if(sala.verificarDisponibilidad(dia, mes, horario.getHora())) {
				return new Funcion(dia, mes, horario, pelicula, sala, autocine);
			}
			else {
				return null;
			}
		}
		else {
			return null;
		}
	}
	
	
	/**
	 * @summary Metodo que se encarga de crear un boleto para cada puesto.
	 */
	public void crearTicket() {
		ArrayList<Puesto> puestos = sala.getPuestos();
		int disponibles = sala.cantidadPuestos();
		
		for(int i = 0; i < sala.getPuestos().size(); i++) {
			if(disponibles > 0) {
				Ticket ticket = new Ticket(this,puestos.get(i));
				tickets.add(ticket);
				disponibles --;
			}
			else {
				tickets.add(null);
			}
		}		
	}
	
	
	/**
	 * @summary Metodo que se encarga de la disponibilidad de un puesto en una sala.
	 * @return La disponibilidad de un puesto y su tipo.
	 */
	public String verDisponiblidad() {
		ArrayList<ArrayList<String>> total = new ArrayList<ArrayList<String>>();
		for(int i = 0; i < sala.getFilas(); i++) {
			ArrayList<String> fila = new ArrayList<String>();
			for(int j = 0; j < sala.getColumnas(); j++) {
				Ticket ticket = tickets.get((i)*sala.getColumnas()+j);
				if(ticket != null) {
					String formato_ticket = ticket.estado() + ticket.tipoString() + String.valueOf(ticket.getNum_puesto());
					fila.add(formato_ticket);
				}
				else {
					String formato_ticket = "";
					fila.add(formato_ticket);
				}
			}
			total.add(fila);
		}
		String formato = "";
		for (ArrayList<String> fila: total) {
			String patron = "%-6s   ".repeat(sala.getColumnas());
			Object[] fila_args = fila.toArray(new String[0]);
			formato += String.format(patron, fila_args) + "\n";
		}
		formato += "\n" + centerString(sala.getColumnas()*9, "PANTALLA") + "\n";
		return formato;
	}
	
	
	/**
	 * @param width
	 * @param s
	 * @summary Metodo que centra un String s a una cantidad de caracteres minima. 
	 * @return El String centrado.
	 */
	public static String centerString(int width, String s) {
		return String.format("%-" + width + "s", String.format("%" + (s.length() + (width - s.length()) / 2) + "s", s));
	}
	
	
	/**
	 * @param ticket
	 * @param cliente
	 * @summary Recibe ticket para cambiar su estado y un cliente al cual se le asigna. Metodo para vender un ticket.
	 * @return Un Boolen de si se pudo o no vender un ticket. Retorna True o False segun sea el caso.
	 */
	public Boolean ventaTicket(Ticket ticket, Cliente cliente) {
		if(ticket.isEstado() == true && cliente.getEdad() >= Funcion.getPelicula().getClasificacion()) {
			ticket.setEstado(false);
			cliente.getHistorialCompras().add(ticket);
			cantidadTicketsVendidos ++;
			ticket.calcularPrecioDefinitivo(cliente);
			return true;
		}
		else {
			return false;
		}	
	}
	
	
	// Getters and Setters.{
	public static int getDia() {
		return dia;
	}
	public void setDia(int dia) {
		Funcion.dia = dia;
	}
	public static int getMes() {
		return mes;
	}
	public void setMes(int mes) {
		Funcion.mes = mes;
	}
	public static String getHorario() {
		return horario.getHora();
	}
	public void setHorario(Horario horario) {
		Funcion.horario = horario;
	}
	public static Pelicula getPelicula() {
		return pelicula;
	}
	public void setPelicula(Pelicula pelicula) {
		Funcion.pelicula = pelicula;
	}
	public static Sala getSala() {
		return sala;
	}
	public void setSala(Sala sala) {
		Funcion.sala = sala;
	}
	public Autocine getAutocine() {
		return autocine;
	}
	public void setAutocine(Autocine autocine) {
		this.autocine = autocine;
	}
	public ArrayList<Ticket> getTickets() {
		return tickets;
	}
	public void setTickets(ArrayList<Ticket> tickets) {
		this.tickets = tickets;
	}
	public int getCantidadTicketsVendidos() {
		return cantidadTicketsVendidos;
	}
	public void setCantidadTicketsVendidos(int cantidadTicketsVendidos) {
		this.cantidadTicketsVendidos = cantidadTicketsVendidos;
	}
	public static int getCantidadFunciones() {
		return cantidadFunciones;
	}
	public static void setCantidadFunciones(int cantidadFunciones) {
		Funcion.cantidadFunciones = cantidadFunciones;
	}
	public static int getNumero() {
		return numero;
	}
	public void setNumero(int numero) {
		Funcion.numero = numero;
	}
	public static List<Funcion> getFunciones() {
		return funciones;
	}
	public static void setFunciones(List<Funcion> funciones) {
		Funcion.funciones = funciones;
	}
	

	
}