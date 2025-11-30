from __future__ import annotations

from .models import Person
from .validation import validiere_person

class Buergerregister:
    """Einfache In-Memory-Verwaltung von Personen."""

    def __init__(self):
        self._personen: list[Person] = []

    def add(self, p: Person) -> bool:
        """Fügt eine Person hinzu, sofern sie valide und kein Duplikat ist.

        Duplikatdefinition: gleicher Vorname + Nachname.
        """
        ok, errors = validiere_person(p.__dict__)
        if not ok:
            print("Fehler:", errors)
            return False
        if any(e.nachname == p.nachname and e.vorname == p.vorname for e in self._personen):
            print("Warnung: Duplikat gefunden.")
            return False
        self._personen.append(p)
        return True

    def list(self) -> list[Person]:
        """Gibt eine Liste aller Personen zurück."""
        return list(self._personen)

    def find(self, nachname: str) -> list[Person]:
        """Findet Personen anhand des Nachnamens."""
        return [p for p in self._personen if p.nachname == nachname]