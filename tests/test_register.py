from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

def test_add_person_success():
    reg = Buergerregister()
    p = Person("Max", "Mustermann", 1999, "Bochum")
    assert reg.add(p) is True
    assert len(reg.list()) == 1

def test_add_duplicate_person():
    reg = Buergerregister()
    p1 = Person("Max", "Mustermann", 1999, "Bochum")
    p2 = Person("Max", "Mustermann", 1999, "Bochum")
    reg.add(p1)
    assert reg.add(p2) is False
    assert len(reg.list()) == 1
