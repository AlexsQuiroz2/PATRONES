from abc import abstractmethod
from cafe import Cafe


class Extra(Cafe):
    @abstractmethod
    def get_descripcion(self) -> str:
        raise NotADirectoryError

    @abstractmethod
    def calcular_costo(self) -> float:
        raise NotADirectoryError

class CremaBatida(Extra):
    def __init__(self, cafe: Cafe) -> None:
        self._cafe = cafe

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()}, con crema batida"  
    
    def calcular_costo(self) -> float:
        return self._cafe.calcular_costo() + 1.0

class Leche(Extra):
    def __init__(self, cafe: Cafe) -> None:
        self._cafe = cafe

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()}, con leche"  
    
    def calcular_costo(self) -> float:
        return self._cafe.calcular_costo() + .5

class Helado(Extra):
    def __init__(self, cafe: Cafe) -> None:
        self._cafe = cafe

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()}, con helado"  
    
    def calcular_costo(self) -> float:
        return self._cafe.calcular_costo() + 1.5

class Caramelo(Extra):
    def __init__(self, cafe: Cafe) -> None:
        self._cafe = cafe

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()}, con caramelo"  
    
    def calcular_costo(self) -> float:
        return self._cafe.calcular_costo() + .65