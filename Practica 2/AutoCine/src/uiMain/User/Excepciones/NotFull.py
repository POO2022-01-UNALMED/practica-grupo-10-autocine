# Clase de excepcion relacionada al funcionamiento, centrado en completar todos los datos.

from uiMain.User.Excepciones.Funcionamiento import Funcionamiento
from tkinter import messagebox

class NotFull(Funcionamiento):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de funcionamiento", message="No se ha llenado todos los datos")