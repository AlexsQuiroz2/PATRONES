from Command import *
from personajes import *
from typing import Iterable, Optional

class juego:
    def __init__(self) -> None:
        self._pelea: Optional[Iterable[Comando]]

    def set_pelea(self, comandos: Iterable[Comando])->None:
        self._pelea = comandos

    def ejecutar(self)->None:
        if self._pelea is not None:
            for comando in self._pelea:
                comando.ejecutar()

if __name__ == "__main__":
    juego = juego()

    Paladin = Paladin()
    elfo1 = Elfo()
    elfo2 = Elfo()
    enemigo1 = Nigromante()
    enemigo2 = Orco()
    enemigo3 = Orco()

    pelea = [
        AtacarEnemigo(enemigo1),
        AtacarEnemigo(enemigo2),
        AtacarEnemigo(Paladin),
        AtacarEnemigo(elfo1),
        AtacarEnemigo(enemigo3),
        AtacarEnemigo(elfo2)
    ]


    juego.set_pelea(pelea)
    juego.ejecutar()