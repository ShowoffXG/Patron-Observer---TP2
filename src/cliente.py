import sys
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.subject import Subject
from src.observer import Observer

# El cliente
SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT) 
OBSERVER_B = Observer(SUBJECT)
SUBJECT.notify("Primera notificación", [1, 2, 3])
SUBJECT.unsubscribe(OBSERVER_B) 
SUBJECT.notify("Segunda notificación", {"A": 1, "B": 2, "C": 3})