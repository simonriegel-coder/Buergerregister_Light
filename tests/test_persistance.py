import json
from pathlib import Path

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
# ---------------------------------------------------------
# Projekt-Root und src/ zum Python-Pfad hinzufügen,
# damit wir das Paket aus src importieren können
# ---------------------------------------------------------

# docs/demoproto/demo_add_person.py
# -> parents[0] = demoproto
# -> parents[1] = docs
# -> parents[2] = Projekt-Root

from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister
from src.buergerregister.jsonpersistance import JsonPersistence


def test_save_and_load_roundtrip(tmp_path):
    """
    Testet, ob ein Register korrekt gespeichert
    und wieder geladen werden kann (Roundtrip).
    """
    register = Buergerregister()
    register.add(Person("rifdah", "adilarifah", 2004, "Bandung"))
    register.add(Person("simon", "rigel", 1990, "bremen"))

    file_path = tmp_path / "people.json"

    JsonPersistence.save(register, file_path)
    loaded_register = JsonPersistence.load(file_path)

    personen = loaded_register.list()
    assert len(personen) == 2
    assert personen[0].nachname == "adilarifah"
    assert personen[1].wohnort == "bremen"


def test_load_non_existing_file(tmp_path):
    """
    Testet das Laden einer nicht existierenden Datei.
    Erwartet wird ein leeres Register.
    """
    file_path = tmp_path / "does_not_exist.json"

    register = JsonPersistence.load(file_path)
    assert register.count() == 0


def test_load_empty_file(tmp_path):
    """
    Testet das Laden einer leeren JSON-Datei.
    """
    file_path = tmp_path / "empty.json"
    file_path.write_text("")

    register = JsonPersistence.load(file_path)
    assert register.count() == 0


def test_load_invalid_json(tmp_path):
    """
    Testet das Laden einer ungültigen JSON-Datei.
    """
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{ invalid json }")

    register = JsonPersistence.load(file_path)
    assert register.count() == 0


def test_load_partial_invalid_entries(tmp_path):
    """
    Testet eine JSON-Datei mit gültigen und ungültigen Einträgen.
    Ungültige Einträge müssen übersprungen werden.
    """
    file_path = tmp_path / "mixed.json"

    data = [
        {
            "vorname": "rifdah",
            "nachname": "adilarifah",
            "geburtsjahr": 2004,
            "wohnort": "Bandung"
        },
        {
            "foo": "bar"  # ungültiger Datensatz
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    register = JsonPersistence.load(file_path)
    personen = register.list()

    assert len(personen) == 1
    assert personen[0].vorname == "rifdah"

def test_duplicate_entries_are_not_added_twice(tmp_path):
    """
    Testet, dass doppelte Personen beim Laden aus JSON
    nicht doppelt im Register gespeichert werden.
    """
    file_path = tmp_path / "duplicates.json"

    data = [
        {
            "vorname": "rifdah",
            "nachname": "adilarifah",
            "geburtsjahr": 2004,
            "wohnort": "Bandung"
        },
        {
            # Duplikat (gleiche Person)
            "vorname": "rifdah",
            "nachname": "adilarifah",
            "geburtsjahr": 2004,
            "wohnort": "Bandung"
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    register = JsonPersistence.load(file_path)
    personen = register.list()

    # Erwartung: nur EIN Eintrag
    assert len(personen) == 1



def test_save_empty_register(tmp_path):
    """
    Testet das Speichern eines leeren Registers.
    """
    register = Buergerregister()
    file_path = tmp_path / "empty_save.json"

    JsonPersistence.save(register, file_path)

    assert file_path.exists()
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data == []
