from abc import ABC, abstractmethod

class Cafe(ABC):
    def __init__(self) -> None:
        self._descripcion = "Cualquier cafe"

    def set_descripcion(self, valor: str)-> None:
        self._descripcion = valor

    def get_descripcion(self,)-> str:
        return self._descripcion

    @abstractmethod
    def calcular_costo(self)->float:
        raise NotImplementedError

class Frapuccino(Cafe):
    def __init__(self) -> None:
        self._descripcion = "Frapuccino"

    def calcular_costo(self) -> float:
        return 1.99

class Latte(Cafe):
    def __init__(self) -> None:
        self._descripcion = "Latte"

    def calcular_costo(self) -> float:
        return 1.85