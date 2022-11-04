from cafe import Cafe, Latte, Frapuccino
from Decorador import Helado, Leche, CremaBatida, Caramelo

def ver_detalle(cafe: Cafe):
    print(f"{cafe.get_descripcion()} cuesta {cafe.calcular_costo()}")

if __name__ == "__main__":
    cafe01 = Frapuccino()
    cafe01 = Helado(Leche(Helado(CremaBatida(cafe01))))
    
    
    ver_detalle(cafe01)