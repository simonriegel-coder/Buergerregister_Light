from __future__ import annotations

import sys
from pathlib import Path

# ---------------------------------------------------------
# Projekt-Root und src/ zum Python-Pfad hinzufügen
# ---------------------------------------------------------

# Pfad:
# docs/demoproto/demo_validation.py
# parents[0] = demoproto
# parents[1] = docs
# parents[2] = Projekt-Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# ---------------------------------------------------------
# Zentrale Validierungsfunktion importieren
# ---------------------------------------------------------

from buergerregister.validation import validiere_person


def main() -> None:
    print("========================================")
    print("  Live-Demo: Validierung einer Person")
    print("========================================\n")

    
    # Eingaben abfragen
    vorname = input("Vorname: ").strip()
    nachname = input("Nachname: ").strip()
    geburtsjahr_input = input("Geburtsjahr (z. B. 1990): ").strip()
    wohnort = input("Wohnort: ").strip()

    # Geburtsjahr versuchen zu konvertieren
    try:
        geburtsjahr = int(geburtsjahr_input)
    except ValueError:
        geburtsjahr = None  # wird von validiere_person als unplausibel erkannt

    # Person als Dictionary (wie vom Validierer erwartet)
    person_dict = {
        "vorname": vorname,
        "nachname": nachname,
        "geburtsjahr": geburtsjahr,
        "wohnort": wohnort,
    }

    print("\n--> Aufruf: validiere_person(person_dict)")
    ok, fehler = validiere_person(person_dict)

    # Ergebnis ausgeben
    if ok:
        print("✅ Person ist gültig.")
    else:
        print("❌ Person ist ungültig.")
        print("Fehler:")
        for f in fehler:
            print(f" - {f}")


if __name__ == "__main__":
    main()
