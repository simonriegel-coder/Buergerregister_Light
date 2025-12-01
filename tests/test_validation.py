import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


import pytest
from src.buergerregister.validation import validiere_person


def test_valid_person():
    """Validasi lengkap harus lolos."""
    p = {
        "vorname": "Max",
        "nachname": "Mustermann",
        "geburtsjahr": 1990,
        "wohnort": "Bochum",
    }

    ok, errors = validiere_person(p)
    assert ok is True
    assert errors == []


def test_missing_firstname():
    p = {
        "vorname": "",
        "nachname": "Mustermann",
        "geburtsjahr": 1990,
        "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Vorname fehlt." in errors


def test_missing_lastname():
    p = {
        "vorname": "Max",
        "nachname": "",
        "geburtsjahr": 1990,
        "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Nachname fehlt." in errors


def test_missing_city():
    p = {
        "vorname": "Max",
        "nachname": "Mustermann",
        "geburtsjahr": 1990,
        "wohnort": "",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Wohnort fehlt." in errors


def test_firstname_contains_digits():
    p = {
        "vorname": "M4x",
        "nachname": "Mustermann",
        "geburtsjahr": 1990,
        "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Vorname darf keine Zahlen enthalten." in errors


def test_lastname_contains_digits():
    p = {
        "vorname": "Max",
        "nachname": "Must3rmann",
        "geburtsjahr": 1990,
               "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Nachname darf keine Zahlen enthalten." in errors


def test_birthyear_too_small():
    p = {
        "vorname": "Max",
        "nachname": "Mustermann",
        "geburtsjahr": 1800,
        "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Geburtsjahr unplausibel." in errors


def test_birthyear_too_large():
    p = {
        "vorname": "Max",
        "nachname": "Mustermann",
        "geburtsjahr": 2030,
        "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Geburtsjahr unplausibel." in errors


def test_birthyear_not_int():
    p = {
        "vorname": "Max",
        "nachname": "Mustermann",
        "geburtsjahr": "1990",  # string bukan int
        "wohnort": "Bochum",
    }
    ok, errors = validiere_person(p)
    assert ok is False
    assert "Geburtsjahr unplausibel." in errors
