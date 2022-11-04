from abc import ABC, abstractclassmethod
from typing import Optional, Union

class Combatiente(ABC):
    @abstractclassmethod
    def pelear(self):
        pass

class Mago(ABC):
    @abstractclassmethod
    def sanar(self):
        pass

    @abstractclassmethod
    def invocar_hechizo(self):
        pass

class Paladin(Combatiente):
    def pelear(self):
        print("Paladin peleando con espada")

class Orco(Combatiente):
    def pelear(self):
        print("Orco lanzando piedras")

class Elfo(Mago):
    def sanar(self):
        print("Elfo sanando aliados")

    def invocar_hechizo(self):
        print("Elfo lazando hechizo")

class Nigromante(Mago):
    def sanar(self):
        pass
    def invocar_hechizo(self):
        print("Nigromante lanzando magia negra")