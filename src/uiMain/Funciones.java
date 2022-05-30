package uiMain;

import java.util.*;
import gestorAplicacion.Autocine.Autocine;
import gestorAplicacion.Persona.Cliente;
import gestorAplicacion.Taquilla.Ticket;
import gestorAplicacion.Taquilla.Funcion;
import gestorAplicacion.Taquilla.Pelicula;
import java.util.stream.Collectors;


public class Funciones {
	
	public static void clienteNuevoOViejo(Autocine autocine) {
		
		int id;
		int opcion;
		System.out.print("Digite la cedula del cliente: ");
		Scanner entrada = new Scanner(System.in);
		id = entrada.nextInt();
		if(autocine.verificarCliente(id)) {
			System.out.println(autocine.BuscadorCliente(id));
			Funciones.buscarPorViejo(autocine, id);
		}
		else {
			Funciones.datos(autocine, id);
			System.out.println("El cliente ha sido registrado con exito");
			System.out.println("");
			Funciones.buscarPorNuevo(autocine, id);
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
		Cliente cliente = new Cliente(nombre, edad, id, autocine);
	}
	
	
	public static void buscarPorViejo(Autocine autocine, int id) {
		
		int opcion = 0;
		System.out.print("Quiere buscar pelicula por:\n" + "1. Recomendadas\n" + "2. Funciones\n" + "3. Pelicula\n");
		Scanner entrada = new Scanner(System.in);
		opcion = entrada.nextInt();
		
		switch(opcion) {
		
		case 1: Funciones.recomendadas(autocine, id);
		break;
		
		case 2: Funciones.funcionesDia(autocine, id);
		break;
		
		case 3: Funciones.funcionesPelicula(autocine, id);
		break;	
		}
		
	}
	
		
	public static void buscarPorNuevo(Autocine autocine, int id) {
		
		int opcion = 0;
		System.out.print("¿Quiere buscar pelicula por:\n" + "1. Funciones\n" + "2. Pelicula\n");
		Scanner entrada = new Scanner(System.in);
		opcion = entrada.nextInt();
		
		switch(opcion) {
		

		case 1: Funciones.funcionesDia(autocine, id);
		break;
		
		case 2: Funciones.funcionesPelicula(autocine, id);
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
		
		if(autocine.verFuncion(dia, mes).size() == 0) {
			System.out.println("No hay funciones para esta fecha, escoja una fecha valida");
			funcionesPelicula(autocine, id);	
		}
		else {
			ArrayList<Funcion> funciones = autocine.verFuncion(dia, mes);
			List<Pelicula> peliculasMes = new ArrayList<Pelicula>();
			
			for(Funcion funcion: funciones) {
				peliculasMes.add(funcion.getPelicula());
			}
			
			peliculasMes = peliculasMes.stream().distinct().collect(Collectors.toList());
			System.out.println("Peliculas en el cine");
			int i = 1;
			for(Pelicula p: peliculasMes) {
				System.out.println(i + ": " + p.getNombre());
				i++;
			}
			
			System.out.println("Digite el numero de la pelicula seleccionada");
			int peli = entrada.nextInt();
			Pelicula pelicula = peliculasMes.get(peli-1);
			System.out.println(Funciones.formatearFunciones(autocine.verFuncion(pelicula, dia, mes)));
			
			System.out.println("¿Que desea hacer?\n" + "1. Comprar\n" + "2. Volver\n");
			opcion = entrada.nextInt();
			
			switch(opcion) {
			case 1: Funciones.comprar(autocine, id);
			break;
			
			case 2: if(autocine.verificarCliente(id)) {
				Funciones.buscarPorViejo(autocine, id);
			}
			else {
				Funciones.buscarPorNuevo(autocine, id);
			}
			break;
			}
		}
	}
	
	public static void funcionesDia(Autocine autocine, int id) {
		
		int opcion = 0;
		int dia, mes;
		Scanner entrada = new Scanner(System.in);
		System.out.println("Ingrese el dia y mes de las funciones que desea ver");
		System.out.print("Dia: ");
		dia = entrada.nextInt();
		System.out.println("Mes: ");
		mes = entrada.nextInt();
		
		if(autocine.verFuncion(dia, mes).size() == 0) {
			System.out.println("No hay funciones para esta fecha, escoja una fecha valida");
			funcionesDia(autocine, id);
		}
		else {
			System.out.println(Funciones.formatearFunciones(autocine.verFuncion(dia, mes)));
			System.out.print("¿Que desea hacer\n" + "1. Comprar\n" + "2. Volver\n");
			opcion = entrada.nextInt();
			
			switch(opcion) {
			case 1: Funciones.comprar(autocine, id);
			break;
			
			case 2: if(autocine.verificarCliente(id)) {
				Funciones.buscarPorViejo(autocine, id);
			}
			else {
				Funciones.buscarPorNuevo(autocine, id);
			}
			break;
			}
		}
	}
	
	
	public static void recomendadas(Autocine autocine, int id) {
		
		int opcion = 0;
		System.out.println(Funciones.formatearFunciones(autocine.verFuncion(autocine.BuscadorCliente(id))));
		System.out.println("¿Que desea hacer?\n" + "1. Comprar\n" + "2. Volver\n");
		Scanner entrada = new Scanner(System.in);
		opcion = entrada.nextInt();
		
		switch(opcion) {
		case 1: Funciones.comprar(autocine, id);
		break;
		
		case 2: Funciones.buscarPorViejo(autocine, id);
		break;
		}
	}
	
	
	public static void comprar(Autocine autocine, int id) {
		
		int numeroFuncion;
		int numeroTicket;
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Ingrese el codigo de la funcion a la que desea asistir: ");
		numeroFuncion = entrada.nextInt();
		Funcion funcion = autocine.BuscadorFuncion(numeroFuncion);
		System.out.println(funcion.verDisponiblidad());
		
		System.out.print("Ingrese el codigo del ticket que desea comprar: ");
		numeroTicket = entrada.nextInt();
		Ticket ticket = autocine.BuscadorTicket(numeroTicket, funcion);
		
		if(funcion.ventaTicket(ticket, autocine.BuscadorCliente(id))) {
			System.out.print("El precio de su boleto es: ");
			System.out.println(ticket.calcularPrecio());	
		}
		else {
			System.out.println("El boleto no esta disponible o no cumple con la edad minima para la pelicula");
		}
	}
	
	
	public static String formatearFunciones(ArrayList<Funcion> funciones) {
		
		String resultado = "\n\n";
		for (Funcion funcion: funciones) {
			String formato = "%s|%s|%s|%s";
			String fecha = "Fecha: " + String.format("%02d/%02d", funcion.getDia(), funcion.getMes());
			resultado += funcion.getPelicula().getNombre() + " " + funcion.getPelicula().getClasificacion() + "+" + "\n";
			resultado += String.format(
				formato,
				centerString(6, funcion.getHorario()),
				centerString(8, "Sala " + funcion.getSala().getNumero()),
				centerString(4, funcion.getSala().getTipo()),
				centerString(5, String.format("%03d", funcion.getNumero())));
			resultado += "\n" + fecha;
			resultado += "\n\n";
		}
		return resultado;
	}
	
	
	public static String centerString(int width, String s) {
		return String.format("%-" + width + "s", String.format("%" + (s.length() + (width - s.length()) / 2) + "s"));
	}
	
	
}