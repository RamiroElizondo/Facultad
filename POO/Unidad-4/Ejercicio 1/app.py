"""
Una nutricionista hace un análisis rápido de sus pacientes para determinar el tratamiento a seguir utilizando el índice 
de masa corporal (IMC). El mismo se calcula con la siguiente fórmula:
IMC = peso [kg]/ estatura2 [m]
Una vez determinado el IMC, se puede averiguar la composición corporal utilizando la siguiente tabla: Composición corporal
Índice de masa corporal (IMC)
Peso inferior al normal Menos de 18.5
Normal 18.5 - 24.9 
Peso superior al normal 25.0 - 29.9
Obesidad Más de 30.0
Con esta información la nutricionista puede decidir el tipo de dieta, actividad física y demás tratamientos a recomendar.
Se le solicita a usted que desarrolle una aplicación que permita calcular el IMC e informar la composición corporal. 
Para ello, la nutricionista le ha proporcionado un prototipo de la aplicación que desea.
"""
import tkinter as tk
from tkinter import ttk

class app(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("IMC")
        self.geometry("300x150")
        
        self.labelTitulo = ttk.Label(self,text="Calculadora de IMC")
        self.labelTitulo.grid(row=0,column=0,columnspan=2)

        self.labelaltura = ttk.Label(self, text="Altura:")
        self.labelaltura.grid(row=1, column=0)
        self.cajaAltura = ttk.Entry(self,width=30) 
        self.cajaAltura.grid(row=1, column=1)

        self.labelPeso = ttk.Label(self, text="Peso:")
        self.labelPeso.grid(row=2, column=0)
        self.cajaPeso = ttk.Entry(self, width=30) 
        self.cajaPeso.grid(row=2, column=1)
        
        self.botonCm = ttk.Button(self,text="cm")
        self.botonCm.grid(row=1,column=3)
        self.botonKg = ttk.Button(self,text="kg")
        self.botonKg.grid(row=2,column=3)
        self.columnconfigure(3,weight=1)

        self.botonCalcular = ttk.Button(self, text="Calcular", command=self.calcular)#command=self.calcular
        self.botonCalcular.grid(row=3, column=0, sticky='NSWE')
        
        self.boton2 = ttk.Button(self, text="Limpiar", command=self.limpiar)
        self.boton2.grid(row=3, column=1, sticky='NSWE')

        self.Imclabel = ttk.Label(self, text="Su IMC es: ")
        self.Imclabel.grid(row=4, column=0)

        self.resultado = ttk.Label(self, text="-")
        self.resultado.grid(row=4, column=1)

        self.medidalabel = ttk.Label(self, text="Kg/m2")
        self.medidalabel.grid(row=4, column=2)

        self.conclusionlabel = ttk.Label(self, text="")
        self.conclusionlabel.grid(row=5, column=0, columnspan=2)
        
    def limpiar(self):
        self.cajaAltura.delete(0, tk.END)
        self.cajaPeso.delete(0, tk.END)
        self.botonCalcular.config(text="Calcular")
        self.resultado.config(text="Resultado: ")

    def calcular(self):
        altura = float(self.cajaAltura.get())
        peso = float(self.cajaPeso.get())
        imc = peso / ((altura/100) ** 2)
        imc = round(imc,2)
        self.resultado.config(text=str(imc))
        varMostrar = ""
        if imc < 18.5:
            varMostrar = "Peso inferior al normal"
        elif imc >= 18.5 and imc <= 24.9:
            varMostrar ="Normal"
        elif imc >= 25.0 and imc <= 29.9:
            varMostrar = "Peso superior al normal"
        elif imc >= 30.0:
            varMostrar = "Obesidad"
        else:
            varMostrar = "Valor no Estudiado"
        self.conclusionlabel.config(text=varMostrar)
if __name__ == "__main__":
    aplicacion = app()
    aplicacion.mainloop()

#Entry:
    #Width: cantidad de carectares, para alinear justify=tk.right/center/left
    #show: censura los caracteres
#Buttom:
#ipady ipadx se cambia el tamaño de la caja de texto interno
#pady padx se cambia el tamaño de la caja de texto externa
#columnspan se cambia la cantidad de columnas que ocupara
#rowspan se cambia la cantidad de filas que ocupara