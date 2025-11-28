from src.buergerregister.validation import validiere_person

def test_validiere_person_valid():
    person = {"vorname": "Anna", "nachname": "Schmidt", "geburtsjahr": 1990, "wohnort": "Essen"}
    ok, errors = validiere_person(person)
    assert ok is True
    assert errors == []

def test_validiere_person_invalid_multiple():
    person = {"vorname": "", "nachname": "", "geburtsjahr": 1800, "wohnort": ""}
    ok, errors = validiere_person(person)
    assert ok is False
    assert len(errors) >= 3
