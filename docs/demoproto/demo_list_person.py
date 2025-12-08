


from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

""""
Live-Demo: Liste im Bürgerregister

Ablauf:

1) Register anlegen
2) alle personen anzeigen
3) 
4) 

"""


if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
    
from tabulate import tabulate

from buergerregister.models import Person
from buergerregister.register import Buergerregister


def demo_list_person_table():
    # Register erstellen
    register = Buergerregister()

    # Beispielpersonen
    p1 = Person("Anna", "Schmidt", 1990, "Bremen")
    p2 = Person("Max", "Müller", 1985, "Hamburg")
    p3 = Person("Laura", "Becker", 2001, "Berlin")

    register.add(p1)
    register.add(p2)
    register.add(p3)

    # Liste abrufen
    personen = register.list()

    # Tabelle erstellen
    headers = ["Vorname", "Nachname", "Geburtsjahr", "Wohnort"]
    table = [
        [p.vorname, p.nachname, p.geburtsjahr, p.wohnort]
        for p in personen
    ]

    print("\n--- Personenliste als Tabelle ---\n")
    print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    demo_list_person_table()
