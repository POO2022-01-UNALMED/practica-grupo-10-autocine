# Clase de excepcion relacionada a los datos ingresados, centrada para cuando el tipo de datos no es esperado.

from uimain.user.excepciones.ingresodatos import IngresoDatos
from tkinter import messagebox

class NoTipo(IngresoDatos):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de ingreso", message="Los datos ingresados no concuerdan con el tipo esperado")