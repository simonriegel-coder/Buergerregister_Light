from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister
from src.buergerregister.validation import validiere_person
from src.buergerregister.jsonpersistance import JsonPersistence

register = JsonPersistence.load("people.json")
print("\033[92mBürgerregister CLI gestartet.\033[0m")
print("\033[94mDaten aus people.json geladen.\033[0m")



# ---------------------------------------------------------
# Tabellenanzeige
# ---------------------------------------------------------
def drucke_tabelle(personen):
    if not personen:
        print("\033[91mKeine Personen vorhanden.\033[0m")
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
        print("6: Suche nach Wohnort")
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
                print("\033[91mFehler: Geburtsjahr muss eine Zahl sein.\033[0m")
                continue

            valid, errors = validiere_person(data)
            if not valid:
                print("\033[91mFehler in den Eingaben:\033[0m")
                for e in errors:
                    print(" -", e)
                continue

            person = Person(**data)

            if register.add(person):
                print("\033[92mPerson erfolgreich hinzugefügt.\033[0m")
            else:
                print("\033[91mPerson konnte nicht gespeichert werden.\033[0m")

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
                print("\033[93mAlle Daten wurden gelöscht.\033[0m")
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
        # 6: Nach Wohnort suchen
        # ---------------------------------------
        elif choice == "6":
            ort = input("Wohnort: ").strip()
            personen = register.find_by_wohnort(ort)
            drucke_tabelle(personen)

        # ---------------------------------------
        # 0: Beenden
        # ---------------------------------------
        elif choice == "0":
            JsonPersistence.save(register, "people.json")
            print("\033[92mDaten wurden gespeichert.\033[0m")
            print("Programm beendet.")
            break

        # ---------------------------------------
        # Ungültige Eingabe
        # ---------------------------------------
        else:
            print("\033[91mUngültige Eingabe. Bitte erneut versuchen.\033[0m")


# ---------------------------------------------------------
# Startpunkt
# ---------------------------------------------------------
if __name__ == "__main__":
    cli()
