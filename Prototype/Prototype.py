from abc import ABCMeta, abstractstaticmethod
import copy

class IprotoTipo(metaclass=ABCMeta):
    """Interfas con el metodo clone"""
    @abstractstaticmethod
    def clone():
        """El clone"""


class ClaseConcreta1(IprotoTipo):
    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d)
        )
        
    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"

class ClaseConcreta2(IprotoTipo):
    def __init__(self, i=0, s="", l=[], d={} ):

        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
            return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d)
        )
                
    def __str__(self):
        return f"i={self.i}\t\ts={self.s}\tl={self.l}\td={self.d}\n{id(self)}"


if __name__ == "__main__":
    Objeto1 = ClaseConcreta1(1, "Objeto1", [1,2,3], {"a": 1, "b": 2, "c": 3})
    print(Objeto1)
    Objeto2 = Objeto1.clone()
    Objeto2.s = "Objeto2"
    Objeto2.l[0] = 10
    print(Objeto2)
    print(Objeto1)