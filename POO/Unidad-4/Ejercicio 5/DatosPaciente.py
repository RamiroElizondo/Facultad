from tkinter import LabelFrame,Label,Entry,Frame,messagebox,END
from ClasePaciente import Paciente

class DatosPaciente(LabelFrame):
    __entradas = {}

    def __init__(self, master, **kwargs):
        super().__init__(master,text='Paciente',padx=10,pady=10,**kwargs)
        self.frame = Frame(self)
        self.frame.pack()
        self.__entradas = {
            'nombre': self.hacerCampo(0, 'Nombre'),
            'apellido': self.hacerCampo(1, 'Apellido'),
            'telefono': self.hacerCampo(2, 'Teléfono'),
            'altura': self.hacerCampo(3, 'Altura'),
            'peso': self.hacerCampo(4, 'Peso')
        }

    def hacerCampo(self,indice, texto):
        Label(self.frame,text=texto).grid(row=indice,column=0,pady=10)
        entrada = Entry(self.frame, width=25)
        entrada.grid(row=indice,column=1,pady=10)
        return entrada
    
    def limpiar(self):
        for campo in self.__entradas:
            self.__entradas[campo].delete(0,END)
    
    def setPaciente(self, paciente:Paciente):
        self.limpiar()
        for campo in self.__entradas:
            self.__entradas[campo].config(state='normal')
        self.__entradas['nombre'].insert(0, paciente.getNombre())
        self.__entradas['apellido'].insert(0, paciente.getApellido())
        self.__entradas['telefono'].insert(0, paciente.getTelefono())
        self.__entradas['altura'].insert(0, "{}".format(paciente.getAltura()))
        self.__entradas['peso'].insert(0, "{}".format(paciente.getPeso()))

    def getDatos(self)->dict:
        datos = {}
        llaves = ['nombre', 'apellido', 'telefono', 'altura', 'peso']
        i:int=0
        bandera = False

        while i < len(llaves) and bandera == False:
            if self.__entradas[llaves[i]].get() == '':
                bandera = True
                messagebox.showerror('Error', 'Faltan datos')
            else:
                datos[llaves[i]] = self.__entradas[llaves[i]].get()
            i += 1

        valor:dict = {}
        if bandera == False:
            try:
                float(datos['altura'])
                float(datos['peso'])
            except:
                messagebox.showerror('Error', 'Altura y peso deben ser números')
            valor = datos 
        return valor