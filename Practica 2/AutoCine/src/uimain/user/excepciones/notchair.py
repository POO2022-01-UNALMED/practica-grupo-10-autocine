# Clase de excepcion relacionada al funcionamiento del programa, centrada en la selección de botones disponibles.

from uimain.user.excepciones.funcionamiento import Funcionamiento
from tkinter import messagebox

class NotChair(Funcionamiento):
    def __init__(self):
        super().__init__()
        messagebox.showerror(title="Error de funcionamiento", message="No se ha seleccionado una opción con disponiblidad")