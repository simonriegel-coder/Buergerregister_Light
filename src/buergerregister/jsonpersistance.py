"""
Persistenzmodul 1.0 – Speicherung und Laden des Bürgerregisters
auf Basis von JSON.
"""

import json
from pathlib import Path

from .models import Person
from .register import Buergerregister


class JsonPersistence:
    """
    Persistenzklasse für das Bürgerregister.
    """

    @staticmethod
    def save(register: Buergerregister, filename: str) -> None:
        """
        Speichert den aktuellen Inhalt des Registers in einer JSON-Datei.
        """
        path = Path(filename)

        data = [
            {
                "vorname": p.vorname,
                "nachname": p.nachname,
                "geburtsjahr": p.geburtsjahr,
                "wohnort": p.wohnort,
            }
            for p in register.list()
        ]

        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def load(filename: str) -> Buergerregister:
        """
        Lädt ein Bürgerregister aus einer JSON-Datei.
        """
        path = Path(filename)
        register = Buergerregister()

        # Datei existiert nicht
        if not path.exists():
            return register

        # Datei ist leer
        if path.stat().st_size == 0:
            return register

        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            return register

        if not isinstance(data, list):
            return register

        for entry in data:
            try:
                person = Person(
                    entry["vorname"],
                    entry["nachname"],
                    int(entry["geburtsjahr"]),
                    entry["wohnort"],
                )
                register.add(person)
            except (KeyError, ValueError):
                # Ungültige Einträge überspringen
                continue

        return register
