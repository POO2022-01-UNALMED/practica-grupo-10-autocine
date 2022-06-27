# Clase de excepcion relacionada a los datos ingresados, centrada en datos no encontrados.

from uiMain.User.Excepciones.IngresoDatos import IngresoDatos
from tkinter import messagebox

class NotIn(IngresoDatos):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de ingreso", message="Los datos ingresados no se encuentran en la base de datos")