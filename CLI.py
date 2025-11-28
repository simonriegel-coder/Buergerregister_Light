from src.Bürgerregister.person import Person
from src.Bürgerregister.register import Buergerregister, validiere_person

register = Buergerregister()

def cli():
    while True:
        print("\n--- Bürgerregister CLI ---")
        print("1: Neue Person anlegen")
        print("2: Alle Personen anzeigen")
        print("3: Nach Nachname suchen")
        print("0: Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            data = {
                "vorname": input("Vorname: "),
                "nachname": input("Nachname: "),
                "geburtsjahr": int(input("Geburtsjahr: ")),
                "wohnort": input("Wohnort: ")
            }

            valid, msg = validiere_person(data)
            if not valid:
                print("Fehler:", msg)
                continue

            person = Person(**data)
            print(register.add(person))

        elif choice == "2":
            print(register.list())

        elif choice == "3":
            name = input("Nachname: ")
            print(register.find(name))

        elif choice == "0":
            break

        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    cli()