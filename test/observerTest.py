import unittest
import sys
import os
from io import StringIO
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.observer import Observer
from src.subject import Subject

class ObserverTest(unittest.TestCase):
    def test_notify1_should_be_true_when_subject1_notify_are_equals(self):
        #Esto se usa para capturar el print
        capture = StringIO()
        sys.stdout = capture
        #Se crea el subject y observer
        subject1 = Subject()
        observer1 = Observer(subject1)
        notify1 = "Observer id: {0} recibe ('Primera notificacion',)\n"
        subject1.notify("Primera notificacion")
        sys.stdout = sys.__stdout__
        self.assertEqual(notify1.format(observer1.index()), capture.getvalue())

    def test_lista_vacia_should_be_true_when_observers_are_equals(self):
        subject1 = Subject()
        self.assertEqual(0, len(subject1._observers))

    def test_suscribir_observador_should_be_true_when_number_of_observers_be_different_from_0(self):
        subject1 = Subject()
        observer1 = Observer(subject1)
        self.assertNotEqual(0, len(subject1._observers))

    def test_desuscribir_observador_should_be_true_when_number_of_observers_are_equals_to_one(self):
        subject1 = Subject()
        observer1 = Observer(subject1)
        observer2 = Observer(subject1)
        subject1.unsubscribe(observer2)
        self.assertEqual(1, len(subject1._observers))

if __name__ == '__main__': unittest.main()