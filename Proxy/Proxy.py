from abc import ABCMeta, abstractstaticmethod

class Ipersona(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def persona_metodo():
        """Interfaz de metodo"""

class Persona(Ipersona):

    def persona_metodo(self):
        print("Yo soy una persona")

class ProxyPersona(Ipersona):
    def __init__(self):
        self.persona = Persona()

    def persona_metodo(self):
        print("Yo soy la funcionalidad de proxy")
        self.persona.persona_metodo()

p1 = Persona()
p1.persona_metodo()

p2 = ProxyPersona()
p2.persona_metodo() 