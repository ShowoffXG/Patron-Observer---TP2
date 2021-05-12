from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):       #Clase abstracta
    "La interfaz de Subject"

    @staticmethod
    @abstractmethod
    def subscribe(observer):        #Metodo abstracto
        "El metodo de suscripcion"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):      #Metodo abstracto
        "El metodo de desuscripcion"

    @staticmethod
    @abstractmethod
    def notify(observer):       #Metodo abstracto
        "El metodo de notificacion"