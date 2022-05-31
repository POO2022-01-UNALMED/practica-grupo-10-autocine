package uiMain;

import java.util.*;
import gestorAplicacion.Taquilla.Funcion;
import gestorAplicacion.Taquilla.Funcion.Horario;
import gestorAplicacion.Taquilla.Pelicula;
import gestorAplicacion.Autocine.Autocine;
import gestorAplicacion.Salas.*;

public class Administrar {
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
			System.out.println("Â¿Que quiere hacer?\n"
					+ "1: Agregar una pelicula\n"
					+ "2: Eliminar una pelicula\n"
					+ "3: Agregar una funcion\n"
					+ "4: Eliminar una funcion\n"
					+ "5: Agregar una sala\n"
					+ "6: Eliminar una sala\n"
					+ "7: Atras");
			
			opcion=readInt();
			
			switch (opcion) {
			case 1: agregarPelicula(autocine);
			break;
			
			case 2: eliminarPelicula(autocine);
			break;
			
			case 3: generarFuncion(autocine);
			break;
			
			case 4: eliminarFuncion(autocine);
			break;
			
			case 5: agregarSala(autocine);
			break;
			
			case 6: eliminarSala(autocine);
			break;
			
			case 7: break;
		}			
	}

		
	
	public static void agregarPelicula(Autocine autocine) {

		System.out.println("Ingrese el nombre de la pelicula:");		
		Scanner entr = new Scanner(System.in);
		String nombre = entr.nextLine();
		
		System.out.println("Ingrese numero del genero que desea: ");
		
		ArrayList<String> generos = new ArrayList<>(Arrays.asList("Animada", "Accion", "Clasica", "Terror", "Fantasia", "Drama"));
		for(int i = 0; i < 6; i++){
			System.out.println(String.valueOf(i + 1) + " " + generos.get(i));
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
				System.out.println("Ingrese una duracion valida");
			}
		}
		
		System.out.println("Ingrese el idioma de la pelicula:");
		
		Scanner entra = new Scanner(System.in);
		String idioma = entra.nextLine();
		
		System.out.println("Ingrese la edad minima para ver la pelicula: ");
		int edad = readInt();
		
		Pelicula pelicula = new Pelicula(nombre, genero, duracion, idioma, edad, autocine);
		
		autocine.agregarPelicula(pelicula);
		
		System.out.println("La pelicula fue creada con exito");
	}
	
	
	
	public static void eliminarPelicula(Autocine autocine) {
		System.out.println("Peliculas disponibles: ");
		
		List<String> titulos= new ArrayList<String>();		
		for(Pelicula p: Autocine.getPeliculas()) {		
			System.out.println(p.getNombre());
			titulos.add(p.getNombre());
		}
		
		System.out.println("Digite el nombre de la pelicula que quiere eliminar:");
		String eliminar=readString();
		
		if(titulos.contains(eliminar)) {			
			int pos = titulos.indexOf(eliminar);	
			Autocine.getPeliculas().remove(pos);		
			System.out.println("La pelicula fue eliminada con exito");
		}
		else {
			System.out.println("Digite un nombre valido");	
			eliminarPelicula(autocine);
		}
	}
	
	
	
	public static void generarFuncion(Autocine autocine) {
	
		System.out.println("Digite el dia que quiere crear la funcion: ");
		int dia = readInt();
		
		System.out.println("Digite el mes que quiere crear la funcion: ");
		int mes = readInt();
		
		ArrayList<Sala> estados = Autocine.salasDisponibles(mes,dia);
		
		System.out.println("Salas disponibles para el dia/mes: " + dia + "/" + mes);
		for(Sala d: estados) {
			System.out.println("Sala " + d.getNumero());				
		}
		
		System.out.println("Seleccione el numero de la sala que quiere: ");
		int sala = readInt();
		
		Sala Seleccionada = Autocine.buscarSala(sala);
		
		System.out.println("Horarios disponibles de la sala: ");
		
		System.out.println(Seleccionada.verHorarios(dia, mes));
		
		System.out.print("Ingrese el horario en el formato que se le presento arriba: ");
		Scanner entr = new Scanner(System.in);
		String hora = entr.nextLine();
		
		Horario horario = Horario.getHorario(hora);
		
		System.out.println("Peliculas en el cine");
		
		int i = 1;
		
		for(Pelicula p: Autocine.getPeliculas()) {
			System.out.println(i + " : " + p.getNombre());
			i++;
		}
		
		System.out.println("Digite el numero de la pelicula seleccionada: ");
		int peli = readInt();
		
		Pelicula pelicula = Autocine.getPeliculas().get(peli - 1);
			
		Funcion.crearFuncion(dia, mes, horario, pelicula, Seleccionada.getNumero(), autocine);
		System.out.println("La funcion fue generada con exito");
	}
	

	public static void eliminarFuncion(Autocine autocine) {
		System.out.println("funciones disponibles: ");

		List<List<Funcion>> cartelera= new ArrayList<>();
		for(Funcion f: Funcion.getFunciones()) {
			System.out.println(f.getFunciones());
			cartelera.add(f.getFunciones());
		}

		System.out.println("Digite el numero de la funcion que quiere eliminar:");
		Scanner entr = new Scanner(System.in);
		String eliminar = entr.nextLine();

		if(cartelera.contains(eliminar)) {
			int pos = cartelera.indexOf(eliminar);
			Funcion.getFunciones().remove(pos);
			System.out.println("La funcion fue eliminada con exito");
		}
		else {
			System.out.println("Digite un nombre valido");
			eliminarFuncion(autocine);
		}
	}
		
		
	public static void agregarSala(Autocine autocine) {
		
		System.out.println("¿Que tipo de sala quiere agregar?: \n" + "1. Sala 3D\n" + "2. Sala 2D\n");
		
		int opcion = Administrar.readInt();
		
		switch(opcion) {
		case 1: agregarSala3D(autocine);
		break;
		
		case 2: agregarSala2D(autocine);
		break;
		}	
	}
	
	
	
	public static void agregarSala2D(Autocine autocine) {
		
		System.out.print("Ingresar cantidad de filas preferencial de la sala: ");
		int filasPreferencial = Administrar.readInt();
		
		System.out.print("En caso de que la sala sea de tamano normal (5x5) ingrese \"0\" para filas y columnas");
		System.out.print("Ingresar cantidad de filas: ");
		int filas = Administrar.readInt();
		
		System.out.print("Ingresar cantidad de columnas: ");
		int columnas = Administrar.readInt();
		
		if(filas == 0 && columnas == 0) {
			new Sala2D(filasPreferencial, autocine);		
		}
		else {
			new Sala2D(filas, columnas, filasPreferencial, autocine);	 
		}
		System.out.println("¡La nueva sala ha sido creada con Exito!");		
	}
	
	
	public static void agregarSala3D(Autocine autocine) {
		
		System.out.print("Ingresar cantidad de filas: ");
		int filas = Administrar.readInt();
		
		System.out.print("Ingresar cantidad de columnas: ");
		int columnas = Administrar.readInt();
		
		System.out.print("Ingresar cantidad de gafas disponibles de la sala, en caso de que se tengan suficientes ingrese \"0\": ");
		int gafas = Administrar.readInt();
		
		if(gafas == 0) {
			new Sala3D(filas, columnas, autocine);		
		}
		else {
			new Sala3D(filas, columnas, gafas, autocine);	
		}
		System.out.println("¡La nueva sala ha sido creada con Exito!");		
	}
	
	
	public static void eliminarSala(Autocine autocine) {
		
		
	}



}
