package uiMain;

import java.util.*;

import java.util.stream.Collectors;

import gestorAplicacion.Autocine.Autocine;
import gestorAplicacion.Persona.Cliente;
import gestorAplicacion.Salas.Sala;
import gestorAplicacion.Salas.Sala2D;
import gestorAplicacion.Salas.Sala3D;
import gestorAplicacion.Taquilla.Funcion;
import gestorAplicacion.Taquilla.Pelicula;
import gestorAplicacion.Taquilla.Ticket;
import gestorAplicacion.Taquilla.Funcion.Horario;
import baseDatos.Serializador;
import baseDatos.Deserializador;

/**
 * @author Jimena Uribe Giraldo.
 * @author Daniel Alejandro Giraldo Giraldo.
 * @author Jhon Ever Gallego Atehortua.
 * @param Clase Main.
 * @summary Clase que contiene el main.
 */

public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("¡BIENVENIDO AL AUTOCINE!");
		int opcion;
		Autocine autocine = Deserializador.deserializador();
		do {
			System.out.println("¿Que desea hacer?\n" 
					+ " 1. Vender Tickets.\n" 
					+ " 2. Administrar AUTOCINE.\n" 
					+ " 3. Cerrar.");
			
			Scanner entrada = new Scanner(System.in);
			opcion = entrada.nextInt();
			Serializador.serializar(autocine);
			switch(opcion) {
			case 1: clienteNuevoOViejo(autocine);
			break;
			
			case 2: System.out.println("Administrar seleccionado.\n");
			Ejecucion(autocine);
			break;
			}
		}
		while (opcion != 3);
	}
	
	
	public static void clienteNuevoOViejo(Autocine autocine) {
		
		int id;
		int opcion;
		System.out.print("Digite la cedula del cliente: ");
		Scanner entrada = new Scanner(System.in);
		id = entrada.nextInt();
		if(Autocine.verificarCliente(id)) {
			System.out.println(Autocine.BuscadorCliente(id));
			buscarPorViejo(autocine, id);
		}
		else {
			datos(autocine, id);
			System.out.println("¡El cliente ha sido registrado con exito!");
			System.out.println("");
			buscarPorNuevo(autocine, id);
		}
	}
	
	
	public static void datos(Autocine autocine, int id) {
		
		String nombre;
		int edad;
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite el nombre del cliente: ");
		nombre = entrada.nextLine();
		System.out.print("Digite la edad del cliente: ");
		edad = entrada.nextInt();
		Cliente cliente = new Cliente(id, nombre, edad, autocine);
	}
	
	
	public static void buscarPorViejo(Autocine autocine, int id) {
		
		int opcion = 0;
		System.out.print("Quiere buscar pelicula por:\n" 
				+ " 1. Recomendadas.\n" 
				+ " 2. Funciones.\n" 
				+ " 3. Pelicula.\n");
		
		Scanner entrada = new Scanner(System.in);
		opcion = entrada.nextInt();
		
		switch(opcion) {
		
		case 1: recomendadas(autocine, id);
		break;
		
		case 2: funcionesDia(autocine, id);
		break;
		
		case 3: funcionesPelicula(autocine, id);
		break;	
		}
		
	}
	
		
	public static void buscarPorNuevo(Autocine autocine, int id) {
		
		int opcion = 0;
		System.out.print("¿Quiere buscar pelicula por:\n" 
				+ " 1. Funciones.\n" 
				+ " 2. Pelicula.\n");
		Scanner entrada = new Scanner(System.in);
		opcion = entrada.nextInt();
		
		switch(opcion) {
		

		case 1: funcionesDia(autocine, id);
		break;
		
		case 2: funcionesPelicula(autocine, id);
		break;
		}
		
	}
	
	
	public static void funcionesPelicula(Autocine autocine, int id) {
		
		int opcion = 0;
		int dia, mes;
		String peliculaNombre;
		Scanner entrada = new Scanner(System.in);
		Scanner entrada1 = new Scanner(System.in);
		System.out.println("Ingrese el dia, mes y la pelicula de las funciones que desea ver: ");
		System.out.print("Dia: ");
		dia = entrada.nextInt();
		System.out.print("Mes: ");
		mes = entrada.nextInt();
		
		if(Autocine.verFuncion(dia, mes).size() == 0) {
			System.out.println("No hay funciones para esta fecha, escoja una fecha valida.");
			funcionesPelicula(autocine, id);	
		}
		else {
			ArrayList<Funcion> funciones = Autocine.verFuncion(dia, mes);
			List<Pelicula> peliculasMes = new ArrayList<Pelicula>();
			
			for(Funcion funcion: funciones) {
				peliculasMes.add(Funcion.getPelicula());
			}
			
			peliculasMes = peliculasMes.stream().distinct().collect(Collectors.toList());
			System.out.println("Peliculas en el cine: ");
			int i = 1;
			for(Pelicula p: peliculasMes) {
				System.out.println(i + ". " + p.getNombre());
				i++;
			}
			
			System.out.println("Digite el numero de la pelicula seleccionada: ");
			int peli = entrada.nextInt();
			Pelicula pelicula = peliculasMes.get(peli-1);
			System.out.println(formatearFunciones(Autocine.verFuncion(pelicula, dia, mes)));
			
			System.out.println("¿Que desea hacer?\n" 
					+ " 1. Comprar.\n" 
					+ " 2. Volver.\n");
			
			opcion = entrada.nextInt();
			
			switch(opcion) {
			case 1: comprar(autocine, id);
			break;
			
			case 2: if(Autocine.verificarCliente(id)) {
				buscarPorViejo(autocine, id);
			}
			else {
				buscarPorNuevo(autocine, id);
			}
			break;
			}
		}
	}
	
	
	public static void funcionesDia(Autocine autocine, int id) {
		
		int opcion = 0;
		int dia, mes;
		Scanner entrada = new Scanner(System.in);
		System.out.println("Ingrese el dia y mes de las funciones que desea ver: ");
		System.out.print("Dia: ");
		dia = entrada.nextInt();
		System.out.println("Mes: ");
		mes = entrada.nextInt();
		
		if(Autocine.verFuncion(dia, mes).size() == 0) {
			System.out.println("No hay funciones para esta fecha, escoja una fecha valida.");
			funcionesDia(autocine, id);
		}
		else {
			System.out.println(formatearFunciones(Autocine.verFuncion(dia, mes)));
			System.out.print("¿Que desea hacer\n" 
					+ " 1. Comprar.\n" 
					+ " 2. Volver.\n");
			
			opcion = entrada.nextInt();
			
			switch(opcion) {
			case 1: comprar(autocine, id);
			break;
			
			case 2: if(Autocine.verificarCliente(id)) {
				buscarPorViejo(autocine, id);
			}
			else {
				buscarPorNuevo(autocine, id);
			}
			break;
			}
		}
	}
	
	
	public static void recomendadas(Autocine autocine, int id) {
		
		int opcion = 0;
		System.out.println(formatearFunciones(autocine.verFuncion(Autocine.BuscadorCliente(id))));
		System.out.println("¿Que desea hacer?\n" 
				+ "1. Comprar.\n" 
				+ "2. Volver.\n");
		
		Scanner entrada = new Scanner(System.in);
		opcion = entrada.nextInt();
		
		switch(opcion) {
		case 1: comprar(autocine, id);
		break;
		
		case 2: buscarPorViejo(autocine, id);
		break;
		}
	}
	
	
	public static void comprar(Autocine autocine, int id) {
		
		int numeroFuncion;
		int numeroTicket;
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Ingrese el codigo de la funcion a la que desea asistir: ");
		numeroFuncion = entrada.nextInt();
		Funcion funcion = Autocine.BuscadorFuncion(numeroFuncion);
		System.out.println(funcion.verDisponiblidad());
		
		System.out.print("Ingrese el codigo del ticket que desea comprar: ");
		numeroTicket = entrada.nextInt();
		Ticket ticket = Autocine.BuscadorTicket(numeroTicket, funcion);
		
		if(funcion.ventaTicket(ticket, Autocine.BuscadorCliente(id))) {
			System.out.print("El precio de su ticket es: ");
			System.out.println(Ticket.calcularPrecio());	
		}
		else {
			System.out.println("El ticket no esta disponible o no cumple con la edad minima para la pelicula.");
		}
	}
	
	
	public static String formatearFunciones(ArrayList<Funcion> funciones) {
		
		String resultado = "\n\n";
		for (Funcion funcion: funciones) {
			String fecha = "Fecha: " + String.format("%02d/%02d", Funcion.getDia(), Funcion.getMes());
			resultado += "Pelicula: " + Funcion.getPelicula().getNombre() + " | " + "Edad: " + "+" + Funcion.getPelicula().getClasificacion() + "\n"
					+ fecha + " | " + "Hora: " + Funcion.getHorario() + "\n"
					+ "Sala: " + Funcion.getSala().getNumero() + " | " + "Tipo: " + Funcion.getSala().getTipo() + "\n"
					+ "Codigo: " + String.format("%03d", Funcion.getNumero());
			resultado += "\n\n";
		}
		return resultado;
	}
	
	
	public static String centerString(int width, String s) {
		return String.format("%-" + width + "s", String.format("%" + (s.length() + (width - s.length()) / 2) + "s", s));
	}
	
	
	static Scanner sc = new Scanner(System.in); 
	
	static int readInt() {
		return sc.nextInt();
	}
	
	static String readString() {
		return sc.nextLine();
	}
	
	static double readDouble() {
		return sc.nextDouble();
	}
	
	
	public static void Ejecucion(Autocine autocine) {
	
		int opcion;
			System.out.println("¿Que quiere hacer?\n"
					+ " 1. Agregar una pelicula.\n"
					+ " 2. Eliminar una pelicula.\n"
					+ " 3. Agregar una funcion.\n"
					+ " 4. Agregar una sala.\n"
					+ " 5. Atras.");
			
			opcion=readInt();
			
			switch (opcion) {
			case 1: agregarPelicula(autocine);
			break;
			
			case 2: eliminarPelicula(autocine);
			break;
			
			case 3: generarFuncion(autocine);
			break;
			
			case 4: agregarSala(autocine);
			break;
			
			case 5: break;
		}			
	}

		
	public static void agregarPelicula(Autocine autocine) {

		System.out.println("Ingrese el nombre de la pelicula: ");		
		Scanner entr = new Scanner(System.in);
		String nombre = entr.nextLine();
	
		System.out.println("Ingrese el numero del genero que desea: ");
		
		ArrayList<String> generos = new ArrayList<>(Arrays.asList("Animada", "Accion", "Clasica", "Terror", "Fantasia", "Drama"));
		for(int i = 0; i < 6; i++){
			System.out.println(String.valueOf(i + 1) + ". " + generos.get(i));
		}

		String genero = generos.get(readInt() - 1);		

		int duracion = 0;
		while (true) {
			System.out.println("Ingrese la duracion de la pelicula (1 o 2 horas): ");
			duracion = readInt();
			if(duracion == 1||duracion == 2) {
				break;
			}
			else {
				System.out.println("Ingrese una duracion valida.");
			}
		}
		
		System.out.println("Ingrese el idioma de la pelicula: ");
		
		Scanner entra = new Scanner(System.in);
		String idioma = entra.nextLine();
		
		System.out.println("Ingrese la edad minima para ver la pelicula: ");
		int edad = readInt();
		
		Pelicula pelicula = new Pelicula(nombre, genero, duracion, idioma, edad, autocine);
		
		System.out.println("¡La pelicula fue creada con exito!");
	}
	
	
	public static void eliminarPelicula(Autocine autocine) {
		System.out.println("Peliculas disponibles: ");
		
		List<String> peliculas= new ArrayList<String>();		
		for(Pelicula p: Autocine.getPeliculas()) {		
			System.out.println(p.getNombre());
			peliculas.add(p.getNombre());
		}
		
		System.out.println("Digite el nombre de la pelicula que desea eliminar: ");
		Scanner entr = new Scanner(System.in);
		String eliminar = entr.nextLine();
		
		if(peliculas.contains(eliminar)) {			
			int pos = peliculas.indexOf(eliminar);	
			Autocine.getPeliculas().remove(pos);		
			System.out.println("¡La pelicula fue eliminada con exito!");
		}
		else {
			System.out.println("Digite un nombre valido.");	
			eliminarPelicula(autocine);
		}
	}
	
	
	public static void generarFuncion(Autocine autocine) {
	
		System.out.println("Digite el dia que desea crear la funcion: ");
		int dia = readInt();
		
		System.out.println("Digite el mes que desea crear la funcion: ");
		int mes = readInt();
		
		ArrayList<Sala> estados = Autocine.salasDisponibles(mes,dia);
		
		int i = 1;
		System.out.println("Salas disponibles para el Dia/Mes: " + dia + "/" + mes);
		for(Sala d: estados) {
			System.out.println(i + ". " + "Sala " + d.getNumero() + ". Tipo: " + d.getTipo());	
			i++;
		}
		
		System.out.println("Seleccione el numero de la sala que desea: ");
		int sala = readInt();
		
		Sala Seleccionada = Autocine.buscarSala(sala);
		
		System.out.println("Horarios disponibles de la sala: ");
		
		System.out.println(Seleccionada.verHorarios(dia, mes));
		
		System.out.print("Ingrese el horario en el formato que se le presento arriba: ");
		Scanner entr = new Scanner(System.in);
		String hora = entr.nextLine();
		
		Horario horario = Horario.getHorario(hora);
		
		System.out.println("Peliculas en el cine:");
		
		int j = 1;
		
		for(Pelicula p: Autocine.getPeliculas()) {
			System.out.println(j + ". " + p.getNombre());
			j++;
		}
		
		System.out.println("Digite el numero de la pelicula seleccionada: ");
		int peli = readInt();
		
		Pelicula pelicula = Autocine.getPeliculas().get(peli - 1);
			
		Funcion.crearFuncion(dia, mes, horario, pelicula, Seleccionada.getNumero(), autocine);
		System.out.println("¡La funcion fue generada con exito!");
	}
	

	public static void agregarSala(Autocine autocine) {
		
		System.out.println("¿Que tipo de sala desea agregar?: \n" 
				+ " 1. Sala 3D.\n" 
				+ " 2. Sala 2D.\n");
		
		int opcion = readInt();
		
		switch(opcion) {
		case 1: agregarSala3D(autocine);
		break;
		
		case 2: agregarSala2D(autocine);
		break;
		}	
	}
	
	
	public static void agregarSala2D(Autocine autocine) {
		
		System.out.print("Ingresar cantidad de filas preferencial de la sala: ");
		int filasPreferencial = readInt();
		
		System.out.print("Ingresar cantidad de filas: ");
		int filas = readInt();
		
		System.out.print("Ingresar cantidad de columnas: ");
		int columnas = readInt();
		
		new Sala2D(filas, columnas, filasPreferencial, autocine);	 
		
		System.out.println("¡La nueva sala ha sido creada con Exito!");		
	}
	
	
	public static void agregarSala3D(Autocine autocine) {
		
		System.out.print("Ingresar cantidad de filas preferencial de la sala: ");
		int filasPreferencial = readInt();
		
		System.out.print("Ingresar cantidad de filas: ");
		int filas = readInt();
		
		System.out.print("Ingresar cantidad de columnas: ");
		int columnas = readInt();
		
		System.out.print("Ingresar cantidad de gafas disponibles de la sala, en caso de que se tengan suficientes ingrese \"0\": ");
		int gafas = readInt();
	
		if(gafas == 0) {
			new Sala3D(filas, columnas, autocine);		
		}
		else {
			new Sala3D(filas, columnas, gafas, autocine);	
		}
		System.out.println("¡La nueva sala ha sido creada con Exito!");		
	}

	
}