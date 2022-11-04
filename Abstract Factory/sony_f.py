from Abstracy import Fabrica
from sony_t import SonyTelevisor
from sony_c import SonyCelular

class SonyFabrica(Fabrica):
    def crear_televisor(self):
        return SonyTelevisor()

    def crear_celular(self):
        return SonyCelular()