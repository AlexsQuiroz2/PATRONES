from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """El metodo de subscribe"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """El metodo unsubscribe"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """El metodo notify"""

class Subjuect(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.remove(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """Recibio notificaciones"""

class Observer(IObserver):
    def __init__(self, observable, name):
        observable.subscribe(self)
        self.name = name

    def notify(self, observable, *args, **kwargs):
        print("Observador", self.name, "recibido", args, kwargs)

SUBJECT = Subjuect()

OBSERVER_A = Observer(SUBJECT, "ObservadorA")   
OBSERVER_B = Observer(SUBJECT, "ObservadorB")

SUBJECT.notify("Hola Observador", [1,2,3], {"a": 1, "b": 2, "c": 3})


    