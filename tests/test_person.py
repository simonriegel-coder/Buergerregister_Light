from src.buergerregister.models import Person
import pytest

def test_person_valid():
    p = Person("Max", "Mustermann", 1990, "Bochum")
    assert p.vorname == "Max"

def test_person_invalid_year():
    with pytest.raises(ValueError):
        Person("Max", "Mustermann", 1800, "Bochum")
