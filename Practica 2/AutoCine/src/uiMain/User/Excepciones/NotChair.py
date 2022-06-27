# Clase de excepcion relacionada al funcionamiento, centrada en la selección de botones disponibles.

from uiMain.User.Excepciones.Funcionamiento import Funcionamiento
from tkinter import messagebox

class NotChair(Funcionamiento):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de funcionamiento", message="No se ha seleccionado una opcion con disponibilidad")