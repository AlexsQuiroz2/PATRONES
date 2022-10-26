
def singleton(cls):             #Creacion de Decorador para clases
    
    instances = dict()
    
    def wrap(*args, **kwards):          #Creacion de listado de argumentos y diccionario de argumentos  
        if cls not in instances:
            instances [cls] = cls(*args, **kwards)

        return instances[cls]

    return wrap

@singleton                  #Decorador
class sena(object):
    def __init__(self, username):
        self.username = username

if __name__ == '__main__':                 #Creador de objetos

    sena1 = sena('alexs')
    sena2 = sena('cesar')
    sena2 = sena('brandon')
    sena2 = sena('oscar')

    print(sena1 is sena2)       #Reconocer si los objetos son verdaderos 

        

        