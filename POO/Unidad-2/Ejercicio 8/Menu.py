from Conjunto import Conjunto


A = Conjunto([1,2,3,4])
B = Conjunto([3,6,9])
print('A',A)
print('B',B)
class Menu:
    def mostrar(self):
        print('Menu Opciones'.center(30, '-'))
        print('1- Union de Conjuntos')
        print('2- Diferencia de Conjuntos')
        print('3- Verificar Igualdad')
        print('4- Salir') 

    def opcion1(self):
        print('A',A)
        print('Union: ', end=' ')
        print(A+B)

    def opcion2(self):
        print('Diferencia: ', end=' ')
        print(A-B)
        
    def opcion3(self):
        if(A==B):
            print('Conjuntos iguales'.center(30, '-'))
        else:
            print('Conjuntos no iguales'.center(30, '-'))
    def menuopciones(self, opcion):
        if opcion == 1:
            self.opcion1()
        elif opcion == 2:
            self.opcion2()
        elif opcion == 3:
            self.opcion3()
        elif opcion != 1 and opcion != 2 and opcion != 3:
            print('Opcion Invalida')