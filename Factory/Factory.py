from Automoviles import AutomovilDeportivo, AutomocilFamiliar

class FactoryAutomovil:

    @staticmethod
    def get_automovil(tipo, marca):
        if tipo == "Deportivo":
            return AutomovilDeportivo(marca)
        elif tipo == "Familiar":
            return AutomocilFamiliar(marca)
        else:
            return "Tipo invalido"