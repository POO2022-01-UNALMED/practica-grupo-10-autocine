# Clase de la excepcion relacionada al funcionamiento del programa, centrada en la selección de funciones y la no disponibilidad.

from uiMain.User.Excepciones.Funcionamiento import Funcionamiento
from tkinter import messagebox

class NoDisp(Funcionamiento):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de funcionamiento", message="No hay funciones disponibles")