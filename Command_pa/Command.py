from abc import ABC, abstractclassmethod
from typing import Union
from personajes import *

class Comando(ABC):
    def ejecutar(self)-> None:
        pass

class AtacarEnemigo(Comando):
    def __init__(self, personaje: Union[Combatiente, Mago])-> None:
        self._personaje = personaje

    def ejecutar(self) -> None:
        if isinstance(self._personaje, Combatiente):
            self._personaje.pelear()
        elif isinstance(self._personaje, Mago):
            self._personaje.invocar_hechizo()

class SanarAliado(Comando):
    def __init__(self, mago: Mago) -> None:
        self._personaje = mago

    def ejecutar(self) -> None:
        self._personaje.sanar()