class Forma:
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio

def tipo(forma):
    valor = "Sin Tipo"
    if isinstance(forma,Rectangulo):
        valor = 'Rectangulo'
    elif isinstance(forma,Circulo):
        valor = 'Circulo'
    return valor

def main():
    Formas = [Rectangulo(10, 20),
              Circulo(5),
              Rectangulo(30, 40),
              Circulo(10)]

    for forma in Formas:
        print(f"El area del {tipo(forma)}: {forma.area()}")

if __name__ == '__main__':
    main()
