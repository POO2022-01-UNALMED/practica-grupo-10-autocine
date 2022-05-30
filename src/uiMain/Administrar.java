package uiMain;

import java.util.*;
import gestorAplicacion.Taquilla.Funcion;
import gestorAplicacion.Taquilla.Funcion.Horario;
import gestorAplicacion.Taquilla.Pelicula;
import gestorAplicacion.Autocine.Autocine;
import gestorAplicacion.Persona.Cliente;
import gestorAplicacion.Salas.*;
import gestorAplicacion.Taquilla.*;

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
/*	El proposito de este metodo es desarrollar la ejecucion de la clase, aca se define un switch que ejecuta el metodo	
correspondiente a la opcion seleccionada que debe corresponder con las mostradas en el print
*/		
		int opcion;
		
			System.out.println("Que quiere hacer?\n"
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
		/*
		 Recibe un parametro de tipo cine y no devuelve nada, su proposito es pedir los datos de la pelicula para
		 crearla e imprime un mensaje de creacion satisfactoria cuando termina el proceso
		 */
		System.out.println("Ingrese el nombre de la pelicula:");		//se piden los datos para crear la pelicula
		String nombre= readString();
		
		ArrayList<String> generos = new ArrayList<>(Arrays.asList("Animada","Accion","Clasica","Terror","Fantasia","Drama"));	//Se define una lista de generos disponibles con fines de organizacion

		for(int i = 0; i<6; i++){
			System.out.println(String.valueOf(i+1)+" "+generos.get(i));		//se imprimen en pantalla los generos disponibles
		}

		System.out.println("Ingrese numero del genero que desea");
		
		String genero=generos.get(readInt()-1);		//se establece el genero escogido segun el numero escogido por el usario

		int duracion=0;
		while (true) {
			System.out.println("Ingrese la duracion de la pelicula (1 o 2 horas):");	//se repite hasta que se digite un horario valido (1 o 2)
			duracion=readInt();
			if (duracion==1||duracion==2) {
				break;
			}
			else {
				System.out.println("Ingrese una duracion valida");
			}
		}
		
		System.out.println("Ingrese el idioma de la pelicula:");
		String idioma=readString();
		
		System.out.println("Ingrese la edad minima para ver la pelicula:");
		int edad=readInt();
		
		Pelicula pelicula= new Pelicula(nombre,genero,duracion,idioma,edad, autocine);	//se crea la pelicula y se anade a la lista de peliculas del cine
		
		autocine.agregarPelicula(pelicula);		//se agrega la pelicula a la lista de peliculas del cine
		
		System.out.println("La pelicula fue creada con exito");
	}
	
	
	public static void eliminarPelicula(Autocine autocine) {
		/*
		 Recibe un parametro de tipo cine y no devuelve nada, su proposito es mostrar las peliculas disponibles en el momento en el cine
		 que el usuario ingrese el nombre de la pelicula y si esta se encuentra en el cine, eliminarla
		 */
		System.out.println("Peliculas disponibles:");
		
		List<String> titulos= new ArrayList<String>();		
		for(Pelicula p:autocine.getPeliculas()) {		//se muestran las peliculas disponibles y se almacenan sus nombres en una lista
			System.out.println(p.getNombre());
			titulos.add(p.getNombre());
		}
		
		System.out.println("Digite el nombre de la pelicula que quiere eliminar:");
		String eliminar=readString();
		
		if(titulos.contains(eliminar)) {			//si el nombre ingresado esta en la lista de titulos entonces
			int pos = titulos.indexOf(eliminar);	//se coge el indice de lista correspondiente a ese titulo
			autocine.getPeliculas().remove(pos);		//se elimina la pelicula correspondiente al indice
			System.out.println("La pelicula fue eliminada con exito");
		}
		else {
			System.out.println("Digite un nombre valido");	//si no esta se vuelve a ejecturar la funcion
			eliminarPelicula(autocine);
		}
	}
	
	
	public static void generarFuncion(Autocine autocine) {
		/*
		Recibe un parametro de tipo cine, pide la fecha en la que se va a crear la funcion, se muestran las salas que tienen algun horario
		disponible para ese dia, de la sala que escoja el usuario se muestran los horarios disponibles, luego se imprimen las peliculas 
		disponibles y ya se pide el nombre de la pelicula para crear la funcion de la pelicula y sala indicadas en la fecha establecida
		 */
		System.out.println("Digite el dia que quiere crear la funcion:");
		int dia=readInt();
		
		System.out.println("Digite el mes que quiere crear la funcion:");
		int mes=readInt();
		
		ArrayList<Sala> estados=autocine.salasDisponibles(mes,dia);		//se agrega a una lista las salas disponibles del dia y mes requeridos
		
		System.out.println("Salas disponibles para el dia/mes: "+dia+"/"+mes);
		for(Sala d:estados) {
			System.out.println("Sala "+d.getNumero());				//se imprimen en pantalla las salas disponibles
		}
		
		System.out.println("Seleccione el numero de la sala que quiere: ");
		int sala=readInt();
		
		Sala seleccionada = autocine.buscarSala(sala);		//se busca la sala por su numero
		
		System.out.println("Horarios disponibles de la sala: ");
		
		System.out.println(seleccionada.verHorarios(dia, mes));		//se muestran los horarios disponibles de la sala seleccionada
		
		System.out.print("Ingrese el horario en el formato que se le presento arriba: ");
		String hora=readString();
		
		Horario h=Horario.getHorario(hora);
		
		System.out.println("Peliculas en el cine");
		
		int i=1;
		
		for(Pelicula p:autocine.getPeliculas()) {
			System.out.println(i+": "+p.getNombre());	//se muestra un numero y el nombre de las peliculas que hay en el cine
			i++;
		}
		
		System.out.println("Digite el numero de la pelicula seleccionada");
		int peli=readInt();
		
		Pelicula pelicula=autocine.getPeliculas().get(peli-1);
			
		Funcion.crearFuncion(dia, mes, h, pelicula, seleccionada.getNumero(), autocine); //se crea la pelicula en la fecha y horario seleccioado
		System.out.println("La funcion fue generada con exito");
	}
	

	public static void eliminarFuncion(Autocine autocine) {
		System.out.println("Funciones disponibles:");
		
		List<String> funciones = new ArrayList<String>();
		for(Funcion f: autocine.getFunciones()) {
			System.out.println(f.getNumero());
			funciones.add(f.getNumero());
		}
		
		System.out.println("Digite el numero de la funcion que desea eliminar:");
		int eliminar = readInt();
		
		if(funciones.contains(eliminar)) {
			int pos = funciones.indexOf(eliminar);
			autocine.getFunciones().remove(pos);
			System.out.println("La funcion fue eliminada con exito");
		}
		else {
			System.out.println("Digite un numero valido");
			eliminarPelicula(autocine);
		}
		
	}
		
	
	
	
	
	public static void agregarSala(Autocine autocine) {
		/*
		Recibe un parametro de tipo cine y no devuelve nada, su proposito es imprimir en pantalla las diferentes opciones de crear sala que hay
		y segun la opcion seleccionada ejecutar el metodo agregarSala3D o agregarSala2D
		 */
		System.out.println("Que tipo de sala quiere agregar?: \n"
				+ "1. Sala 3D\n"
				+ "2. Sala 2D\n");
		int opcion=Administrar.readInt();
		switch(opcion) {
		case 1: agregarSala3D(autocine);
		break;
		case 2: agregarSala2D(autocine);
		break;
		}

		
	}
	
	
	
	public static void agregarSala2D(Autocine autocine) {
		/*
		Recibe un parametro de tipo cine y no devuelve nada, su proposito es pedir los datos necesarios al usuario para crear una Sala2D
		y se da una opcion default para crear una sala de 8x5 que es cuando se da 0 y 0 para filas y columnas
		 */
		System.out.print("Ingresar cantidad de filas vip de la sala: ");
		int filasVip=Administrar.readInt();
		System.out.print("En caso de que la sala sea de tamano normal (8x5) ingrese \"0\" para filas y columnas");
		System.out.print("Ingresar cantidad de filas: ");
		int filas=Administrar.readInt();
		System.out.print("Ingresar cantidad de columnas: ");
		int columnas=Administrar.readInt();
		if(filas==0 && columnas==0) {
			new Sala2D(filasVip, autocine);			//se crea la sala solo pasando el parametro de filasVip (y cine) en el caso de ser una sala default
		}else {
			new Sala2D( filas,  columnas, filasPreferencial, autocine);	//se crea la sala pasando los parametros de filas, columnas y filasVip (y cine) si no es una sala default
		}
		System.out.println("La nueva sala ha sido creada con Exito!");		
	}
	
	public static void agregarSala3D(Autocine autocine) {
		/*
		Recibe un parametro de tipo cine y no devuelve nada, su proposito es pedir los datos necesarios al usuario para crear una Sala3D
		y se da una opcion default para crear una sala de con igual cantidad de gafas que de sillas que es cuando se ingresa 0 para la cantidad de gafas disponibles
		 */
	
		System.out.print("Ingresar cantidad de filas: ");
		int filas=Administrar.readInt();
		System.out.print("Ingresar cantidad de columnas: ");
		int columnas=Administrar.readInt();
		System.out.print("Ingresar cantidad de gafas disponibles de la sala, en caso de que se tengan suficientes ingrese \"0\": ");
		int gafas=Administrar.readInt();
		if(gafas==0) {
			new Sala3D( filas,  columnas,  autocine);		//se crea la sala solo pasando los parametros de filas, columnas y filasVip (y cine)
		}else {
			new Sala3D( filas,  columnas,  gafas, autocine);	//se crea pasando todos los parametros de filas, columnas y filasVip (y cine)
		}
		System.out.println("La nueva sala ha sido creada con Exito!");		
	}
	
	public static void eliminarSala(Autocine autocine) {
		/*
		Recibe un parametro de tipo cine y no devuelve nada, su proposito es imprimir en pantalla las diferentes opciones de crear sala que hay
		y segun la opcion seleccionada ejecutar el metodo agregarSala3D o agregarSala2D
		 */
		System.out.println("¿Que tipo de sala quiere eliminar?: \n"
				+ "1. Sala 3D\n"
				+ "2. Sala 2D\n");
		int opcion=Administrar.readInt();
		switch(opcion) {
		case 1: eliminarSala3D(autocine);
		break;
		case 2: eliminarSala2D(autocine);
		break;
		}
		
		public static void eliminarSala2D(Autocine autocine) {
			/*
			Recibe un parametro de tipo cine y no devuelve nada, su proposito es pedir los datos necesarios al usuario para crear una Sala2D
			y se da una opcion default para crear una sala de 8x5 que es cuando se da 0 y 0 para filas y columnas
			 */
			System.out.print("Ingresar cantidad de filas vip de la sala: ");
			int filasVip=Administrar.readInt();
			System.out.print("En caso de que la sala sea de tamano normal (8x5) ingrese \"0\" para filas y columnas");
			System.out.print("Ingresar cantidad de filas: ");
			int filas=Administrar.readInt();
			System.out.print("Ingresar cantidad de columnas: ");
			int columnas=Administrar.readInt();
			if(filas==0 && columnas==0) {
				new Sala2D(filasVip, autocine);			//se crea la sala solo pasando el parametro de filasVip (y cine) en el caso de ser una sala default
			}else {
				new Sala2D( filas,  columnas, filasPreferencial, autocine);	//se crea la sala pasando los parametros de filas, columnas y filasVip (y cine) si no es una sala default
			}
			System.out.println("La nueva sala ha sido creada con Exito!");		
		}
		
		public static void eliminarSala3D(Autocine autocine) {
			/*
			Recibe un parametro de tipo cine y no devuelve nada, su proposito es pedir los datos necesarios al usuario para crear una Sala3D
			y se da una opcion default para crear una sala de con igual cantidad de gafas que de sillas que es cuando se ingresa 0 para la cantidad de gafas disponibles
			 */
		
			System.out.print("Ingresar cantidad de filas: ");
			int filas=Administrar.readInt();
			System.out.print("Ingresar cantidad de columnas: ");
			int columnas=Administrar.readInt();
			System.out.print("Ingresar cantidad de gafas disponibles de la sala, en caso de que se tengan suficientes ingrese \"0\": ");
			int gafas=Administrar.readInt();
			if(gafas==0) {
				new Sala3D( filas,  columnas,  autocine);		//se crea la sala solo pasando los parametros de filas, columnas y filasVip (y cine)
			}else {
				new Sala3D( filas,  columnas,  gafas, autocine);	//se crea pasando todos los parametros de filas, columnas y filasVip (y cine)
			}
			System.out.println("La nueva sala ha sido creada con Exito!");		
		}


		
}

	
	
	
	
	

}