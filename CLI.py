from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister
from src.buergerregister.validation import validiere_person

register = Buergerregister()


# ---------------------------------------------------------
# Tabellenanzeige
# ---------------------------------------------------------
def drucke_tabelle(personen):
    if not personen:
        print("Keine Personen vorhanden.")
        return

    print("\n" + "-" * 70)
    print("{:<15} {:<15} {:<12} {:<20}".format(
        "Vorname", "Nachname", "Geburtsjahr", "Wohnort"
    ))
    print("-" * 70)

    for p in personen:
        print("{:<15} {:<15} {:<12} {:<20}".format(
            p.vorname, p.nachname, p.geburtsjahr, p.wohnort
        ))

    print("-" * 70)


# ---------------------------------------------------------
# CLI Hauptmenü
# ---------------------------------------------------------
def cli():
    while True:
        print("\n--- Bürgerregister CLI ---")
        print("1: Neue Person anlegen")
        print("2: Alle Personen anzeigen")
        print("3: Nach Nachname suchen")
        print("4: Alle Daten löschen")
        print("5: Person löschen")
        print("0: Beenden")

        choice = input("Auswahl: ").strip()

        # ---------------------------------------
        # 1: Neue Person anlegen
        # ---------------------------------------
        if choice == "1":
            data = {
                "vorname": input("Vorname: ").strip(),
                "nachname": input("Nachname: ").strip(),
                "geburtsjahr": input("Geburtsjahr: ").strip(),
                "wohnort": input("Wohnort: ").strip(),
            }

            # Geburtsjahr konvertieren
            try:
                data["geburtsjahr"] = int(data["geburtsjahr"])
            except ValueError:
                print("Fehler: Geburtsjahr muss eine Zahl sein.")
                continue

            valid, errors = validiere_person(data)
            if not valid:
                print("Fehler in den Eingaben:")
                for e in errors:
                    print(" -", e)
                continue

            person = Person(**data)

            if register.add(person):
                print("Person erfolgreich hinzugefügt.")
            else:
                print("Person konnte nicht gespeichert werden.")

        # ---------------------------------------
        # 2: Alle Personen anzeigen
        # ---------------------------------------
        elif choice == "2":
            personen = register.list()
            drucke_tabelle(personen)

         # 🔹 Tambahkan jumlah total data
            print(f"\nGesamtanzahl: {register.count()}")

        # ---------------------------------------
        # 3: Nachname suchen
        # ---------------------------------------
        elif choice == "3":
            name = input("Nachname: ").strip()
            personen = register.find(name)
            drucke_tabelle(personen)

        # ---------------------------------------
        # 4: Alle Daten löschen
        # ---------------------------------------
        elif choice == "4":
            confirm = input("Alle Daten löschen? (j/n): ").strip().lower()
            if confirm == "j":
                register.clear_all()
                print("Alle Daten wurden gelöscht.")
            else:
                print("Abgebrochen.")

        # ---------------------------------------
        # 5: Einzelne Person löschen
        # ---------------------------------------
        elif choice == "5":
            v = input("Vorname der zu löschenden Person: ").strip()
            n = input("Nachname der zu löschenden Person: ").strip()

            if register.delete(v, n):
                print("✅ Person erfolgreich gelöscht.")
            else:
                print("❌ Person wurde nicht gefunden.")

        # ---------------------------------------
        # 0: Beenden
        # ---------------------------------------
        elif choice == "0":
            print("Programm beendet.")
            break

        # ---------------------------------------
        # Ungültige Eingabe
        # ---------------------------------------
        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")


# ---------------------------------------------------------
# Startpunkt
# ---------------------------------------------------------
if __name__ == "__main__":
    cli()
