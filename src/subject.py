from src.subjectAbstract import IObservable

class Subject(IObservable):     #Clase del sujeto que sera observado, implementa la clase abstracta IObservable
    "The Subject (Observable)"
    def __init__(self):     #Constructor de la clase
        self._observers = []        #Lista con la cantidad de observadores

    def subscribe(self, observer):      #Metodo para añadir un observador a la lista
        self._observers.append(observer)

    def unsubscribe(self, observer):        #Metodo para eliminar un observador de la lista
        self._observers.remove(observer)

    def notify(self, *args):        #Metodo para notificar cambios en eventos
        for observer in self._observers:        #De la cantidad de observadores notifica de a uno
            observer.notify(self, *args)