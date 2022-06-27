#**
#* @author: Jhon Ever Gallego Atehortua, Jimena Uribe Giraldo y Daniel Alejandro Giraldo Giraldo.
#* @param: Clase ZonaA.
#* @summary: FieldFrame será la clase en donde se generará el formulario para el ingreso de los datos de cada consulta o proceso.
#**

import tkinter  as tk 
from tkinter import * 
from tkinter import messagebox
from uiMain.User.Excepciones.NotFull import NotFull

class FieldFrame(Frame):
    def __init__(self, tituloCriterio, criterios, tituloValores, valores, habilitado, master):
        super().__init__(master)
        self.respuesta = {}
        self.criterios = criterios

        criteriosName = tk.Label(self, text= tituloCriterio, font=('Microsoft Himalaya', 17), width=20, anchor="c", bg = "#E0FFFF" )
        criteriosName.grid(row=1, column=1) 

        valuesName = tk.Label(self, text=tituloValores, font=('Microsoft Himalaya', 17), width=20, anchor="c", bg = "#E0FFFF" )
        valuesName.grid(row=1, column=2)  

        self.entries = [] 

        if(valores == None):
            valores = ["" for valor in range(len(criterios))]
        if(habilitado == None):
            habilitado = []

        for (row, ejemplo), valor in zip(enumerate(criterios), valores): 
            row += 2
            l1 = tk.Label(self, text=ejemplo + " :", width=15, anchor="c", bg = "white")
            l1.grid(row=row, column=1) 

            if((row - 2) not in habilitado):
                t1 = tk.Entry(self, width=15, bg='white') 
                t1.insert(END, valor)
                t1.grid(row=row, column=2)
                self.entries.append(t1)
            else:
                t1 = tk.Label(self, text=valor, font=('Microsoft Himalaya', 16), height=1, width=15, bg='white')
                t1.grid(row=row, column=2)
                self.entries.append(None)

        self.button = tk.Button(self, text='Aceptar', width=15)
        self.button.bind('<ButtonPress-1>', self.add_data)
        self.button.grid(row=7, column=2)
        self.button2 = tk.Button(self, text='Borrar', width=15)
        self.button2.bind('<ButtonPress-1>', self.clear)
        self.button2.grid(row=7, column=1)

    def clear(self, action):
        for i in self.entries:
            i.delete(0,'end')

    def press(self, holi):
        messagebox.showinfo("Hola","Hola")

    def add_data(self,valor):
        self.respuesta = {}

        for i, entry in enumerate(self.entries):
            if entry.get() == "":
                raise NotFull
            if(entry != None):
                self.respuesta[self.criterios[i]] = entry.get()

    def getValue(self, value):
        return self.respuesta[value]

if(__name__ == "__main__"):
    def cambiar(valor):
        frame.pack_forget()
        texto = Label(frame2, text="{}".format(frame.getValue("Hola")))
        texto.pack()
        frame2.pack()

    window = Tk()
    frame = FieldFrame("TituloCriterio", ["Hola", "Perro"],"Criterios" , None, None, window)
    frame.pack()
    frame.button.bind('<ButtonRelease>', cambiar)
    frame2 = Frame(window)

    window.mainloop()