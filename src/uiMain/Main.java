package uiMain;

import java.util.*;
import gestorAplicacion.Autocine.Autocine;
import baseDatos.Serializador;
import baseDatos.Deserializador;

public class Main {
	
	public static void main(String[] args) {
		
		System.out.println("BIENVENIDO AL AUTOCINE");
		int opcion;
		Autocine autocine = Deserializador.deserializador();
		do {
			System.out.println("¿Que desea hacer?\n" + "1. Vender\n" + "2. Administrar\n" + "3. Cerrar");
			
			Scanner entrada = new Scanner(System.in);
			opcion = entrada.nextInt();
			Serializador.serializar(autocine);
			switch(opcion) {
			case 1: Funciones.clienteNuevoOViejo(autocine);
			break;
			
			case 2: System.out.println("Administrar seleccionado\n");
			Administrar.Ejecucion(autocine);
			break;
			}
		}
		while (opcion != 3);
	}

}