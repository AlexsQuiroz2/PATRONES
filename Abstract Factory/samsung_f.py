from Abstracy import Fabrica
from samsung_t import SamsungTelevisor
from samsung_c import SamsungCelular

class SamsungFabrica(Fabrica):
    def crear_televisor(self):
        return SamsungTelevisor()

    def crear_celular(self):
        return SamsungCelular()