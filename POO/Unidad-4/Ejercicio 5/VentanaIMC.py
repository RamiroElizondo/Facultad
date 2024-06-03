from tkinter import * #type: ignore
from ClasePaciente import Paciente

class VentanaIMC(Toplevel):
    __paciente = None
    def __init__(self,parent,paciente:Paciente):
        super().__init__(parent)
        self.paciente = paciente
        self.title('IMC')
        self.geometry('300x200')
        
        self.frame = Frame(self)
        self.frame.pack()

        valores = paciente.calcularMCI()
        imcValor = StringVar(self,'{}'.format(float(valores[0])))
        tipoIMC = StringVar(self,valores[1])

        Label(self.frame,text='IMC:').grid(row=0,column=0)
        self.entryIMC = Entry(self.frame,textvariable=imcValor)
        self.entryIMC.grid(row=0,column=1)

        Label(self.frame,text='Tipo:').grid(row=1,column=0)
        self.entryTipo = Entry(self.frame,textvariable=tipoIMC)
        self.entryTipo.grid(row=1,column=1)

        Button(self.frame, text='Cerrar', command=self.destroy).grid(row=2, column=1, pady=5, padx=5, sticky='sew')