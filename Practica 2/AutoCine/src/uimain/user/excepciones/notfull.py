# Clase de excepcion relacionada al funcionamiento del programa, centrada en la completitud de formularios del programa.

from uimain.user.excepciones.funcionamiento import Funcionamiento
from tkinter import messagebox

class NotFull(Funcionamiento):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de funcionamiento", message="No se han llenado todos los formularios")