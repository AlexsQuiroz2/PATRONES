class SubClaseSistemaA:
    @staticmethod
    def metodo():
        return "A"

class SubClaseSistemaB:
    @staticmethod
    def metodo():
        return "B"

class SubClaseSistemaC:
    @staticmethod
    def metodo():
        return "C"

class Facade:
    def __init__(self):
        self.sub_sistema_clase_a = SubClaseSistemaA()
        self.sub_sistema_clase_b = SubClaseSistemaB()
        self.sub_sistema_clase_c = SubClaseSistemaC()

    def create(self):
        resultado = self.sub_sistema_clase_a.metodo()
        resultado += self.sub_sistema_clase_b.metodo()
        resultado += self.sub_sistema_clase_c.metodo()
        return resultado

FACADE = Facade()
RESULT = FACADE.create()
print("El resultado = %s" % RESULT)
