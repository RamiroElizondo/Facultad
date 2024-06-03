class Nodo:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getDato(self):
        return self.data

    def getSiguiente(self):
        return self.next

    def setDato(self, val):
        self.data = val

    def setSiguiente(self, val):
        self.next = val
