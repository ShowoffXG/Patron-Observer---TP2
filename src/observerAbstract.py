from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):     #Clase abstracta
    "A method for the Observer to implement"
    @staticmethod
    @abstractmethod

    def notify(observable, *args):      #Metodo abstracto
        "Receive notifications"