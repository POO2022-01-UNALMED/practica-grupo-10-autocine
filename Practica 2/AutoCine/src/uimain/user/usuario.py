#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: La clase Usuario es donde estará la ventana de usuario del programa.
#**

from tkinter import *
from uimain.user.zonaa import ZonaA
from uimain.user.zonab import ZonaB
    
class Usuario:
    def __init__(self,cine):
        self.cine=cine
        self.user = Toplevel()
        self.user.title("Ventana de Usuario")
        self.user.geometry("1000x600")  # Tamaño de la ventana .
        self.user.option_add("*tearOff",False)  # Quitar la raya de las opciones de los menus.

        self.frame = ZonaB(self.user,cine)
        self.zona1 = ZonaA(self.user, self.frame)

# Usuario().user.mainloop()