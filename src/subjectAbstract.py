from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):
    "The Subject Interface"
    @staticmethod
    @abstractmethod

    def subscribe(observer):
        "The subscribe method"

    @staticmethod
    @abstractmethod

    def unsubscribe(observer):
        "The unsubscribe method"

    @staticmethod
    @abstractmethod
    
    def notify(observer):
        "The notify method"