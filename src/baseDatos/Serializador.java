package baseDatos;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

import gestorAplicacion.Autocine.Autocine;
import gestorAplicacion.Salas.Puesto;
import gestorAplicacion.Salas.Sala;
import gestorAplicacion.Taquilla.Funcion;
import gestorAplicacion.Salas.Sala3D;
import gestorAplicacion.Taquilla.Pelicula;
import gestorAplicacion.Taquilla.Ticket;
import gestorAplicacion.Persona.Cliente;
import gestorAplicacion.Salas.Sala2D;


public class Serializador {

	public static <E> void serializar(List<E> lista, String className) {
		FileOutputStream fileOut;

		try {
			String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
			// se crea un fileoutputstream para saber donde serializar los archivos
			fileOut = new FileOutputStream(path);
			// Se crea un objeto output stream para poder escribir en el archivo
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			// Guardamos la lista de objetos
			out.writeObject(lista);
			out.close();
			fileOut.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	/**
	 * Serializamos todas las clases que necesitamos
	 */
	public static void serializarTodo() {
		Serializador.serializar(Autocine.getAutocine(), "Autocine");
		Serializador.serializar(Funcion.getFunciones(), "Funciones");
		Serializador.serializar(Sala3D.getSalas3D(), "Salas 3D");
		Serializador.serializar(Sala.getSalas(), "Salas");
		Serializador.serializar(Pelicula.getPeliculas(), "Peliculas");
		Serializador.serializar(Puesto.getPuestos(), "Puestos");
		Serializador.serializar(Cliente.getClientes(), "Clientes");
		Serializador.serializar(Ticket.getTicket(), "Tickets");
		Serializador.serializar(Sala2D.getSalas2D(), "Salas 2D");
	}

	public static void serializar(Autocine autocine) {
		// TODO Auto-generated method stub
		
	}
}
