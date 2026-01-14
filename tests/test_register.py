from __future__ import annotations

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


def test_add_valid_person():
    reg = Buergerregister()
    p = Person("Max", "Mustermann", 1990, "Bochum")

    assert reg.add(p) is True
    assert reg.count() == 1


def test_add_invalid_person():
    reg = Buergerregister()

    # Person ist nicht valid weil < 1900
    p = Person("Max", "Mustermann", 1800, "Bochum")

    # add() muss False zurückgeben
    assert reg.add(p) is False
    assert reg.count() == 0


def test_add_duplicate_person_case_insensitive():
    reg = Buergerregister()

    p1 = Person("Max", "Mustermann", 1990, "Bochum")
    p2 = Person("max", "MUSTERMANN", 1990, "Bochum")

    assert reg.add(p1) is True
    assert reg.add(p2) is False  # Duplikate mussen abgelehnt werden
    assert reg.count() == 1


def test_list_returns_copy():
    reg = Buergerregister()
    p = Person("Max", "Mustermann", 1990, "Bochum")

    reg.add(p)
    lst = reg.list()

    assert len(lst) == 1
    assert lst is not reg._personen   # muss copy
    assert lst[0] == p


def test_find_case_insensitive():
    reg = Buergerregister()

    p1 = Person("Max", "Mustermann", 1990, "Bochum")
    p2 = Person("Julia", "MUSTERMANN", 1995, "Essen")

    reg.add(p1)
    reg.add(p2)

    results = reg.find("mustermann")
    assert len(results) == 2

    results2 = reg.find("MUSTERMANN")
    assert len(results2) == 2


def test_delete_existing_person():
    reg = Buergerregister()

    p1 = Person("Max", "Mustermann", 1990, "Bochum")
    reg.add(p1)

    assert reg.delete("max", "mustermann") is True
    assert reg.count() == 0


def test_delete_non_existing_person():
    reg = Buergerregister()

    reg.add(Person("Max", "Mustermann", 1990, "Bochum"))

    assert reg.delete("Julia", "Musterfrau") is False
    assert reg.count() == 1


def test_clear_all():
    reg = Buergerregister()

    reg.add(Person("Max", "Mustermann", 1990, "Bochum"))
    reg.add(Person("Anna", "Schmidt", 2000, "Essen"))

    reg.clear_all()
    assert reg.count() == 0


