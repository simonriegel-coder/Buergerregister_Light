"""

Live-Demo: Suche im Bürgerregister

Ablauf:

1) Register anlegen
2) Suche mit Ergebnis (ein oder mehrere)
3) Suche ohne Ergebnis
4) Warnung bei zu vielen Fehlern

"""

MAX_FEHLER = 3  # Warnung nach 3 erfolglosen Versuchen

class Person:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

class Buergerregister:
    def __init__(self):
        self.eintraege = []

    def add(self, person):
        self.eintraege.append(person)

    def find(self, nachname):
    # Eingabe prüfen
        if not isinstance(nachname, str) or nachname.strip() == "":
            raise ValueError("Ungültige Eingabe!")
        # Suchlogik: Groß-/Kleinschreibung ignorieren
        nachname = nachname.strip().lower()
        return [p for p in self.eintraege if p.nachname.lower() == nachname]

def main():
# Register anlegen und Personen hinzufügen
    register = Buergerregister()
    register.add(Person("Anna", "Schmidt"))
    register.add(Person("Klaus", "Schmidt"))
    register.add(Person("Carla", "Meyer"))
    register.add(Person("Lisa", "Schmidt"))

    print("Suche im Bürgerregister (exit zum Beenden)")
    print("Groß-/Kleinschreibung wird ignoriert.")
    fehler = 0  # Zählt erfolglose Versuche

    while True:
        eingabe = input("Nachname: ").strip()
        if eingabe.lower() == "exit":
            print("Beende Demo.")
            break

        try:
            ergebnis = register.find(eingabe)
            if ergebnis:
                print(f"{len(ergebnis)} Treffer:")
                for p in ergebnis:
                    print(f"- {p.vorname} {p.nachname}")
                fehler = 0  # Reset bei Erfolg
            else:
                print("Keine Funde.")
                fehler += 1  # Zählt als erfolgloser Versuch
        except ValueError as e:
            print("Fehler:", e)
            fehler += 1

        # Warnung nach 3 erfolglosen Versuchen
        if fehler >= MAX_FEHLER:
            print("⚠ Achtung: Zu viele erfolglose Versuche! Bitte überprüfe deine Eingaben.")
            fehler = 0  # Zähler zurücksetzen

if __name__ == "__main__":
    main()

