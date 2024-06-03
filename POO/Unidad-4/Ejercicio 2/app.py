"""
Una empresa de venta de grandes equipos de aire acondicionado, necesita desarrollar una aplicación que le permita el 
cálculo del IVA (Impuesto al Valor Agregado), sobre el precio base (sin IVA), de cada uno de los aires acondicionados 
que vende. 
Regla de negocio: el cálculo del IVA se calcula de la siguiente forma:
Precio Base*10.5/100 para los artículos grabados con el 10.5%
Precio Base*21/100 para los artículos grabados con el 21%
El analista funcional de la empresa ha diseñado una interface para llevar a cabo la tarea solicitada, la que se le 
provee a usted para el desarrollo de la aplicación.
"""
import tkinter as tk
from tkinter import ttk

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculo de IVA")
        self.geometry("250x250")

        ttk.Label(self, text="Calculo de IVA", justify=tk.LEFT).grid(row=0, column=0, columnspan=2)
        ttk.Label(self, text="Precio Base").grid(row=1, column=0)
        self.cajaPrecioBase = ttk.Entry(self)
        self.cajaPrecioBase.grid(row=1, column=1,pady=20)

        self.valor=tk.IntVar()
        self.opciones = tk.Label(self,text='Opciones:')
        self.opciones.grid(row=2, column=0,padx=20,pady=20)
        tk.Radiobutton(self.opciones, text =' IVA 21%  ',value=0, variable=self.valor, command=self.calcularValor).grid(row=3,column=0)
        tk.Radiobutton(self.opciones, text =' IVA 10.5%',value=1, variable=self.valor, command=self.calcularValor).grid(row=4,column=0)

        self.labelIVA = ttk.Label(self, text="IVA")
        self.labelIVA.grid(row=5, column=0)
        self.labelPrecioIVA = ttk.Label(self, text="Precio con IVA")
        self.labelPrecioIVA.grid(row=6, column=0)

        self.resultadoIVA = ttk.Label(self, text="-")
        self.resultadoIVA.grid(row=5, column=1)
        self.resultadoPrecioIVA = ttk.Label(self, text="-")
        self.resultadoPrecioIVA.grid(row=6, column=1)

    def calcularValor(self):
        iva21 = float(self.cajaPrecioBase.get())*0.21
        iva105 = float(self.cajaPrecioBase.get())*0.105
        total = float(self.cajaPrecioBase.get())

        if self.valor.get()==0:
            total = total + iva21
            self.resultadoIVA.config(text=iva21)
            self.resultadoPrecioIVA.config(text=total)
        elif self.valor.get()==1:
            total = total + iva105
            self.resultadoIVA.config(text=iva105)
            self.resultadoPrecioIVA.config(text=total)

if __name__ == '__main__':
    ventana = app()
    ventana.mainloop()