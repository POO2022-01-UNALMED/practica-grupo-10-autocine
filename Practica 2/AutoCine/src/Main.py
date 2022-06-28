#** 
# @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
# @summary: Programa principal de la aplicacion.
#**

from baseDatos.deserializador import Deserializador
from uiMain.Principal.first import First

if __name__ == "__main__":
    Deserializador.deserializarTodo()
    ventana = First()
    ventana.mainloop()