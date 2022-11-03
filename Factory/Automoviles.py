class Automovil:

    def __init__(self, marca):
        self.marca = marca
        self.__estado = 0

    def arrancar(self): 
        if self.__estado == 0:
            print ("Arrancando el auto", self.marca)
            self.__estado = 1
        else:
            print("El auto", self.marca, "no se ha detenido")

    def detener(self): 
        if self.__estado == 1:
            print ("Deteneniendo el auto", self.marca)
            self.__estado = 0
        else:
            print ("El auto", self.marca, "no ha arrancado")

    def nitro(self):
        print ("Aplicando nitro a auto deportivo")


class AutomovilDeportivo(Automovil):

    def __init__(self, marca):
        super(AutomovilDeportivo, self).__init__(marca)
        print ("Has adquirido un automovil deportivo marca", self.marca)


class AutomocilFamiliar(Automovil):

    def __init__(self, marca):
        super(AutomocilFamiliar, self).__init__(marca)
        print ("Has adquirido un automovil familiar marca", self.marca)

    def nitro(self):
        print ("El auto familiar carece de nitro")

