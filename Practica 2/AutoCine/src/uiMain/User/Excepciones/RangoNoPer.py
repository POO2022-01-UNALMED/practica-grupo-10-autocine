# Clase de excepcion relacionada a los datos ingresados.

from uiMain.User.Excepciones.IngresoDatos import IngresoDatos
from tkinter import messagebox

class RangoNoPer(IngresoDatos):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de ingreso", message="Los datos ingresados no son validos")