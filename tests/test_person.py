import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


from src.buergerregister.models import Person


def test_person_valid():
    """wenn Data Valid ist, dann wird das Objek "person" etabliert."""
    p = Person("Max", "Mustermann", 1990, "Bochum")
    assert p.vorname == "Max"
    assert p.nachname == "Mustermann" 
    assert p.geburtsjahr == 1990
    assert p.wohnort == "Bochum"


def test_person_to_dict():
    """Methode to_dict muss das richtige Dict zurückgeben."""
    p = Person("Max", "Mustermann", 1990, "Bochum")
    d = p.to_dict()

    assert d == {
        "vorname": "Max",
        "nachname": "Mustermann",
        "geburtsjahr": 1990,
        "wohnort": "Bochum",
    }


def test_person_get_full_name():
    """Methode get_full_name muss volständige Name zurückgeben."""
    p = Person("Max", "Mustermann", 1990, "Bochum")
    assert p.get_full_name() == "Max Mustermann"

def test_person_whitespace_preserved():
    """."""
    p = Person("  Max", "Mustermann  ", 1990, "Bochum")
    assert p.vorname == "  Max"
    assert p.nachname == "Mustermann  "



print(Person)
print("Alle Tests in test_person.py erfolgreich ausgeführt.")