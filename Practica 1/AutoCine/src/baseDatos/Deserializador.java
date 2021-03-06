package baseDatos;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
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

public class Deserializador {
	
	public static <E> void deserializador(List<E> list, String className) {
		FileInputStream fileIn;
		try {
			// Creamos una cadena con la ruta del archivo que vamos a cargar
			String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
			System.out.println(path);
			// utilizamos un file para crear este archivo si no existe aun
			File archivo = new File(path);
			archivo.createNewFile(); // Crea un nuevo archivo si no existe

			// usamos un FileInputStream para poder saber de donde cargar el archivo
			fileIn = new FileInputStream(path);

			// Si el archivo esta vacio se lanza un throw EOFException y se muestra como un
			// mensaje de vacio, pero si no se usa el objeto in para leer el archivo
			ObjectInputStream in = new ObjectInputStream(fileIn);

			// Lee el listado de elementos
			ArrayList<E> listado = (ArrayList<E>) in.readObject();

			// Recorro el ArrayList
			for (E el : listado) {
				list.add(el);
			}

			in.close();
			fileIn.close();

		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Esta vacio");
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	/**
	 * Funcion para deserializar toda la aplicacion Generic IT
	 */
	public static void deserializarTodo() {
		Deserializador.deserializador(Autocine.getAutocine(), "Autocine");
		Deserializador.deserializador(Funcion.getFunciones(), "Funciones");
		Deserializador.deserializador(Sala3D.getSalas3D(), "Salas 3D");
		Deserializador.deserializador(Sala.getSalas(), "Salas");
		Deserializador.deserializador(Pelicula.getPeliculas(), "Peliculas");
		Deserializador.deserializador(Puesto.getPuestos(), "Puesto");
		Deserializador.deserializador(Cliente.getClientes(), "Clientes");
		Deserializador.deserializador(Ticket.getTicket(), "Tickets");
		Deserializador.deserializador(Sala2D.getSalas2D(), "Salas 2D");
		
	}

	public static Autocine deserializador() {
		// TODO Auto-generated method stub
		return null;
	}
}
