from __future__ import annotations

import sys
from pathlib import Path

# ---------------------------------------------------------
# Projekt-Root und src/ zum Python-Pfad hinzufügen
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# ---------------------------------------------------------
# Fachlogik importieren
# ---------------------------------------------------------

from buergerregister.models import Person
from buergerregister.register import Buergerregister


def eingabe_person() -> Person | None:
    """Fragt Personendaten ab und erzeugt ein Person-Objekt."""
    print("\nBitte Personendaten eingeben:\n")

    vorname = input("Vorname: ").strip()
    nachname = input("Nachname: ").strip()
    geburtsjahr_input = input("Geburtsjahr (z. B. 1990): ").strip()
    wohnort = input("Wohnort: ").strip()

    try:
        geburtsjahr = int(geburtsjahr_input)
    except ValueError:
        print("❌ Ungültige Eingabe für Geburtsjahr (keine Zahl).")
        return None

    try:
        return Person(
            vorname=vorname,
            nachname=nachname,
            geburtsjahr=geburtsjahr,
            wohnort=wohnort,
        )
    except Exception as e:
        print(f"❌ Fehler beim Erzeugen der Person: {e}")
        return None


def menu_loop() -> None:
    """Einfache CLI für einen End-to-End-Demo-Pfad."""
    register = Buergerregister()

    while True:
        print("\n========================================")
        print("  Bürgerregister Light – E2E-Demo")
        print("========================================")
        print("1) Neue Person anlegen")
        print("2) Alle Personen anzeigen")
        print("3) Personen nach Nachname suchen")
        print("0) Beenden")
        auswahl = input("\nAuswahl: ").strip()

        if auswahl == "0":
            print("Programm beendet.")
            break

        elif auswahl == "1":
            # End-to-End: Eingabe -> Validierung -> Speicherung
            person = eingabe_person()
            if person is None:
                continue

            print("\n--> Aufruf: register.add(person)")
            erfolg = register.add(person)

            if erfolg:
                print("✅ Person wurde erfolgreich gespeichert.")
            else:
                print("❌ Person konnte nicht gespeichert werden.")
                print("   (Details wurden von der Validierung/Logik ausgegeben.)")

        elif auswahl == "2":
            personen = register.list()
            if not personen:
                print("\n(Keine Personen im Register.)")
            else:
                print("\nAktuell gespeicherte Personen:")
                for p in personen:
                    print(f" - {p.vorname} {p.nachname} ({p.geburtsjahr}), {p.wohnort}")

        elif auswahl == "3":
            nachname = input("\nNachname für Suche: ").strip()
            treffer = register.find(nachname)
            if not treffer:
                print(f"\nKeine Personen mit Nachname '{nachname}' gefunden.")
            else:
                print(f"\nGefundene Personen mit Nachname '{nachname}':")
                for p in treffer:
                    print(f" - {p.vorname} {p.nachname} ({p.geburtsjahr}), {p.wohnort}")
        else:
            print("Ungültige Auswahl. Bitte 0, 1, 2 oder 3 eingeben.")


def main() -> None:
    menu_loop()


if __name__ == "__main__":
    main()
