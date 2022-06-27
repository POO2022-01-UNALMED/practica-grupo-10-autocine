#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: La clase Usuario es donde estará la ventana de usuario del programa.
#**

from tkinter import *
from uiMain.User.ZonaA import ZonaA
from uiMain.User.ZonaB import ZonaB
    
class Usuario:
    def __init__(self, autocine):
        self.autocine = autocine
        self.user = Toplevel()
        self.user.title("Ventana de Usuario")
        self.user.geometry("1000x600")  
        self.user.option_add("*tearOff", False) 

        self.frame = ZonaB(self.user, autocine)
        self.zona1 = ZonaA(self.user, self.frame)

# Usuario().user.mainloop()