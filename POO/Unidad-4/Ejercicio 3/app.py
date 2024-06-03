"""
Un empresario que se dedica a la venta de productos importados, conoce el precio de compra y el precio de venta de sus
productos en moneda dólar. Diariamente, realiza sus ventas en pesos argentinos y necesita conocer el precio de venta 
actualizado según la cotización actual del dólar.

Se le solicita que diseñe y desarrolle una aplicación que permita convertir el precio en dólares de un producto al 
precio en pesos argentinos. Para conocer la cotización actual del dólar, usted deberá hacer uso de la API 
https://www.dolarsi.com/api/api.php?type=dolar. El valor del dólar que se toma como referencia es el Oficial para la 
venta. El empresario le ha dado a conocer un prototipo de la aplicación deseada:
"""
import requests
import tkinter as tk
from tkinter import DoubleVar, StringVar, ttk

class app(tk.Tk):
    __dolares = None
    def __init__(self):
        super().__init__()
        self.title("Conversión de Dólar a Pesos")
        self.geometry("250x100")
        self.__dolares =StringVar()
        ttk.Label(self, text="Conversión de Dólar a Pesos", justify=tk.CENTER).grid(row=0, column=0, columnspan=3)
        self.__dolares.trace("w", self.obtenerPrecioDolar)
        self.cajaPrecioDolar = ttk.Entry(self, textvariable=self.__dolares, width=10)
        self.cajaPrecioDolar.grid(row=1, column=1)

        self.labeldolares = ttk.Label(self, text="Dólares")
        self.labeldolares.grid(row=1, column=2)

        self.labelEq = ttk.Label(self, text="Es equivalente a:")
        self.labelEq.grid(row=2, column=0)

        self.labelResultado = ttk.Label(self, text="-")
        self.labelResultado.grid(row=2, column=1)

        self.labelPeso = ttk.Label(self, text="Pesos")
        self.labelPeso.grid(row=2, column=2)

        ttk.Button(self,text='Salir', command=self.destroy).grid(row=3, column=2)
        #self.cajaPrecioDolar.bind('<Return>',self.obtenerPrecioDolar)
        
    
    def obtenerPrecioDolar(self, *args):
        response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
        listaDict = response.json()
        precioDolar:float = 0.0

        for dict in listaDict:
            if dict['casa']['nombre'] == 'Oficial':
                precioDolar = float(dict['casa']['venta'].replace(',', '.'))

        if self.cajaPrecioDolar.get() != "":
            dolar = float(self.cajaPrecioDolar.get())
            pesos = dolar * precioDolar
            self.labelResultado.config(text=str(pesos))
        else:
            self.labelResultado.config(text="-")

if __name__ == '__main__':
    ventana = app()
    ventana.mainloop()
