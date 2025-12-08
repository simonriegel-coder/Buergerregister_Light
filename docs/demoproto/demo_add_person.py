"""
Live-Demo für die Funktion Buergerregister.add(person).

Ablauf:
1) Bürgerregister anlegen.
2) Personendaten über die Konsole eingeben.
3) Person-Objekt erzeugen.
4) Buergerregister.add(person) aufrufen.
5) Rückgabewert und Ergebnis anzeigen.

Diese Datei liegt in docs/demoproto und greift auf den Code im src/-Ordner zu.
"""

from __future__ import annotations

import sys
from pathlib import Path

# ---------------------------------------------------------
# Projekt-Root und src/ zum Python-Pfad hinzufügen,
# damit wir das Paket aus src importieren können
# ---------------------------------------------------------

# docs/demoproto/demo_add_person.py
# -> parents[0] = demoproto
# -> parents[1] = docs
# -> parents[2] = Projekt-Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# ---------------------------------------------------------
# Hier das eigentliche Bürgerregister importieren
# WICHTIG: Der Paketname im src-Ordner heißt sehr
# wahrscheinlich "buergerregister".
# Falls er anders heißt, musst du den Namen unten anpassen.
# ---------------------------------------------------------

from buergerregister.models import Person  # ggf. Paketname anpassen
from buergerregister.register import Buergerregister  # dto.


def main() -> None:
    print("========================================")
    print("  Live-Demo: Buergerregister.add(person)")
    print("========================================\n")

    # 1) Leeres Register anlegen
    register = Buergerregister()

    # 2) Eingabe der Personendaten
    print("Bitte Personendaten eingeben:\n")
    vorname = input("Vorname: ").strip()
    nachname = input("Nachname: ").strip()
    geburtsjahr_str = input("Geburtsjahr (z. B. 1990): ").strip()
    wohnort = input("Wohnort: ").strip()

    # 3) Geburtsjahr nach int konvertieren (mit Fehlerbehandlung)
    try:
        geburtsjahr = int(geburtsjahr_str)
    except ValueError:
        print("\n❌ Ungültige Eingabe für Geburtsjahr (keine Zahl).")
        return

    # 4) Person-Objekt erzeugen
    try:
        person = Person(
            vorname=vorname,
            nachname=nachname,
            geburtsjahr=geburtsjahr,
            wohnort=wohnort,
        )
    except Exception as e:
        # Falls Person im Konstruktor / __post_init__ schon meckert
        print(f"\n❌ Fehler beim Erzeugen der Person: {e}")
        return

    # 5) Person mit add() ins Register aufnehmen
    print("\n--> Aufruf: register.add(person)")
    erfolg = register.add(person)

    # 6) Ergebnis anzeigen
    print(f"Rückgabewert von add(person): {erfolg}")
    if erfolg:
        print("✅ Die Person wurde erfolgreich zum Register hinzugefügt.")
    else:
        print("❌ Die Person konnte nicht hinzugefügt werden.")


if __name__ == "__main__":
    main()

