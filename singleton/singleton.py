
def singleton(cls):
    
    instances = dict()
    
    def wrap(*args, **kwards):
        if cls not in instances:
            instances [cls] = cls(*args, **kwards)

        return instances[cls]

    return wrap

@singleton
class sena(object):
    def __init__(self, username):
        self.username = username

if __name__ == '__main__':

    sena1 = sena('alexs')
    sena2 = sena('cesar')
    sena2 = sena('brandon')
    sena2 = sena('oscar')



    print(sena1 is sena2)

        

        