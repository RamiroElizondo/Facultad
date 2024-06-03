from tkinter import * #type: ignore
from ClasePaciente import Paciente
from DatosPaciente import DatosPaciente

class VentanaAgregar(Toplevel):
    __llamada = None

    def __init__(self, parent, llamada):
        super().__init__(parent)
        self.__llamada = llamada
        self.title("Agregar Paciente")
        self.geometry("400x300")
        self.datos = DatosPaciente(self)
        self.datos.pack()
        
        self.guardarBoton = Button(self.datos, text="Guardar", command=self.guardar)
        self.guardarBoton.pack(side=RIGHT, ipadx=5, padx=5, pady=5)

    def guardar(self):
        datos = self.datos.getDatos()
        if datos is not None:
            nom = datos['nombre']
            ape = datos['apellido']
            tel = datos['telefono']
            peso = datos['peso']
            altura = datos['altura']
            self.__llamada(Paciente(nom,ape,tel,peso,altura)) #type: ignore
            self.destroy()
        