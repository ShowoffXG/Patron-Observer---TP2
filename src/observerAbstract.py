from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):     #Clase abstracta
    "Interfaz para que el Observer implemente"

    @staticmethod
    @abstractmethod
    def notify(observable, *args):      #Metodo abstracto
        "Recibe notificaciones"