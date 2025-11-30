from __future__ import annotations

from .models import Person
from .validation import validiere_person


class Buergerregister:
    """Einfache In-Memory-Verwaltung von Personen."""

    def __init__(self):
        self._personen: list[Person] = []

    def add(self, p: Person) -> bool:
        """Fügt eine Person hinzu, sofern sie valide und kein Duplikat ist."""

        # Sichere Validierung
        daten = {
            "vorname": p.vorname,
            "nachname": p.nachname,
            "geburtsjahr": p.geburtsjahr,
            "wohnort": p.wohnort,
        }

        ok, errors = validiere_person(daten)
        if not ok:
            print("Fehler:", errors)
            return False

        # Case-insensitive Duplikatprüfung
        vor = p.vorname.strip().lower()
        nach = p.nachname.strip().lower()

        if any(
            e.vorname.strip().lower() == vor and
            e.nachname.strip().lower() == nach
            for e in self._personen
        ):
            print("Warnung: Duplikat gefunden.")
            return False

        self._personen.append(p)
        return True

    def list(self) -> list[Person]:
        """Gibt eine Liste aller Personen zurück."""
        return list(self._personen)

    def find(self, nachname: str) -> list[Person]:
        """Findet Personen anhand des Nachnamens (case-insensitive)."""
        key = nachname.strip().lower()
        return [
            p for p in self._personen
            if p.nachname.strip().lower() == key
        ]

    def count(self) -> int:
        """Gibt die Gesamtanzahl der gespeicherten Personen zurück."""
        return len(self._personen)

    def clear_all(self):
        """Löscht alle Personen."""
        self._personen.clear()

    def delete(self, vorname: str, nachname: str) -> bool:
        """Löscht eine Person anhand von Vorname + Nachname (case-insensitive)."""

        vor = vorname.strip().lower()
        nach = nachname.strip().lower()

        for p in self._personen:
            if (
                p.vorname.strip().lower() == vor
                and p.nachname.strip().lower() == nach
            ):
                self._personen.remove(p)
                return True

        return False
