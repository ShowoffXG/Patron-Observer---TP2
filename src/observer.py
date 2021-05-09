from src.observerAbstract import IObserver

class Observer(IObserver):      #Clase observer, encargada de visualizar cambios en eventos del sujeto observado y notificarlos, implementa la clase abstracta IObserver
    "The concrete observer"
    def __init__(self, observable):     #Constructor de la clase
        observable.subscribe(self)      #Agrega al nuevo constructor creado a la lista de suscriptores

    def index(self):
        return id(self)

    def notify(self, observable, *args):        #Metodo para, en base al sujeto observado, mostrar las notificaciones mandadas
        print(f"Observer id: {id(self)} recibe {args}")