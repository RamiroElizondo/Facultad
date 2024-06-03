import json
from ClaseLista import ListaEnlazada
from ClaseDocente import Docente
from ClaseInvestigador import Investigacion
from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo

class ObjectEncoder:
    def leerJson(self,archivo):
        with open(archivo,'r',encoding='utf8') as docJson:
            datos = json.load(docJson)
        return datos
    
    def cargarObjetos(self,lista:ListaEnlazada):
        dicc = self.leerJson("personal.json")
        for elem in dicc:
            if "__class__" not in elem:
                raise Exception('No hay Objetos')
            else:
                class_name = elem["__class__"]
                if class_name == "Docente":
                    atributos = elem["__atributos__"]
                    docente = Docente(atributos)
                    lista.agregarElemento(docente)
                elif class_name == "Investigador":
                    atributos= elem["__atributos__"]
                    investigador = Investigacion(atributos)
                    lista.agregarElemento(investigador)
                elif class_name == "DocenteInvestigador":
                    atributos = elem["__atributos__"]
                    docenteInvestigador = DocenteInvestigador(atributos)
                    lista.agregarElemento(docenteInvestigador)
                elif class_name == "PersonalApoyo":
                    atributos = elem["__atributos__"]
                    personalApoyo = PersonalApoyo(atributos)
                    lista.agregarElemento(personalApoyo)
                else:
                    print('No valido')
    
    def guardarJson(self,lista:ListaEnlazada):
        ruta = "nuevoArchivo.json"
        actual = lista.getComienzo()
        listaN = []
        while actual != None:
            dato = actual.getDato()
            dicc = dato.toJson()
            listaN.append(dicc)
            actual = actual.getSiguiente()
        with open(ruta,'w') as archivo:
            json.dump(listaN,archivo,indent='\t')
        print('Agentes Guardados'.center(30,'-'))