"""
Usar la narrativa del Ejercicio Nº 1
Se han agregado nuevos requerimientos al sistema, y usted como programador, debe darles solución:
La nutricionista cuenta con un archivo llamado “pacientes.json” donde tiene almacenados los datos de cada paciente que 
atiende. De cada paciente se almacena: nombre, apellido, teléfono, altura(cm) y peso(kg). 
Se necesita que la aplicación muestre los datos almacenados de los pacientes junto con el IMC y la composición corporal
resultantes. Además, se debe permitir modificar los datos del paciente, lo que implica que se actualice tanto el IMC 
como la composición corporal.
Para facilitar el desarrollo, la nutricionista le proporciona la estructura que debería tener el sistema y le solicita 
que se encargue del diseño del mismo.
"""
from tkinter import Tk,messagebox,Scrollbar,Button,Listbox,StringVar,Frame,LEFT,RIGHT,BOTH,N,S,E,W,END,Y,BOTTOM
from ObjectEncoder import ObjectEnconder
from ClasePaciente import Paciente
from VentanaAgregar import VentanaAgregar
from DatosPaciente import DatosPaciente
from VentanaIMC import VentanaIMC

class app(Tk):
    __objeto: ObjectEnconder
    __seleccionados: tuple[int,Paciente]  | None

    def __init__(self,manejador):
        super().__init__()
        self.__objeto = manejador
        self.title("Lista Pacientes")
        self.geometry("600x400")
    
        self.frame = Frame(self)
        self.frame.pack(side=LEFT, padx=10, pady=10)
        self.listB = Listbox(self.frame, height=15, width=20)
        self.listB.pack(side=LEFT, fill=BOTH,expand=1)
        self.listB.bind("<Double-Button-1>", self.mostrarPaciente) #type:ignore
        self.listB.bind("<<ListboxSelect>>", self.mostrarPaciente) #type:ignore

        scroll = Scrollbar(self.frame,command=self.listB.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.listB.config(yscrollcommand=scroll.set)

        self.datos = DatosPaciente(self)
        self.datos.pack(side=RIGHT, padx=10, pady=10)
        Button(self.datos, text="Guardar", command=self.guardar).pack(side=RIGHT, ipadx=5, padx=5, pady=5)
        Button(self.datos, text="Borrar", command=self.borrar).pack(side=RIGHT, ipadx=5, padx=5, pady=5)
        Button(self.datos, text="Ver IMC", command=self.verIMC).pack(side=RIGHT, ipadx=5, padx=5, pady=5)
        Button(self, text="Agregar Paciente", command=self.añadirPaciente).pack(side=BOTTOM, pady=5)

        for paciente in self.__objeto.getLista():
            self.cargarLista(paciente)
    #Muestra los datos del paciente seleccionado
    def mostrarPaciente(self,*args):
        eleccion = self.listB.curselection() # Devuelve una tupla de indices de los elementos seleccionados
        if len(eleccion) !=0:
            indice = int(eleccion[0])
            self.mostrarDatos(indice)
    
    def mostrarDatos(self,indice):
        paciente = self.__objeto.getPaciente(indice)

        if paciente is None:
            self.__seleccionados = None
            self.datos.limpiar()
        else:
            self.__seleccionados = (indice,paciente)
            self.datos.setPaciente(paciente)

    def guardar(self):
        if self.__seleccionados is  None:
            messagebox.showerror("Error", "No hay paciente seleccionado")
        else:
            datos = self.datos.getDatos()
            pos = self.__seleccionados[0]
            nom = datos['nombre']
            ape = datos['apellido']
            tel = datos['telefono']
            alt = datos['altura']
            pes = datos['peso']
            paciente = Paciente(nom,ape,tel,alt,pes)
            self.__objeto.renovar(pos,paciente)
    
    def borrar(self):
        if self.__seleccionados is  None:
            messagebox.showerror("Error", "No hay paciente seleccionado")
        else:
            pos = self.__seleccionados[0]
            self.__objeto.borrar(pos)
            self.listB.delete(pos)
            self.datos.limpiar()

    def verIMC(self):
        if self.__seleccionados is  None:
            messagebox.showerror("Error", "No hay paciente seleccionado")
        else:
            ventanaIMC = VentanaIMC(self,self.__seleccionados[1])
            ventanaIMC.wait_window()
    

    def cargarLista(self,paciente:Paciente):
        mostrar = paciente.getNombre() + " " + paciente.getApellido()
        self.listB.insert(END, mostrar)
    
    def añadirPaciente(self):
        def callback(paciente):
            self.__objeto.addPaciente(paciente)
            self.cargarLista(paciente)
        
        ventanaAgregar = VentanaAgregar(self,callback)
        ventanaAgregar.wait_window()

if __name__ == '__main__':
    manejador = ObjectEnconder()
    ventana = app(manejador)
    ventana.mainloop()







