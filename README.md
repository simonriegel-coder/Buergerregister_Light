# Bürgerregister Light – Persistenzmodul 1.0 – Bürgerregister speichern und laden

Dieses Repository bildet das Starterpaket für die Teilprüfung 2(Hausaufgabe: Bürgerregister speichern und laden).

## Ziele
1. das Prinzip von Persistenz (Datenübertragung) praktisch anwenden können,
2. JSON als leichtgewichtiges, plattformunabhängiges Datenformat verstehen,
3. eine saubere Schnittstelle für ein Persistenzmodul entwerfen können,
4. Randfälle (leere, Dateien, fehlende Dateien, fehlerhafte Datensätze) systematisch behandeln,
5. das Zusammenspiel von Modell (Person), Register (Buergerregister) und Persistenz (JsonPersistence) verstehen und
6. einfache Roundtrip-Tests („save à load à compare“) formulieren und ausführen können.

## Code testen
```bash
-CLI.py öffnen
-Code in CLI.py ausführen
-Neue Person anlegen (bei terminal) / Alle Personen anzeigen
-Sobald das CLI beendet wird, werden die eingegebenen Daten sofort gespeichert
-People.json öffnen (hier finden Sie die im System gespeicherten Daten)
```

## Tests ausführen
```bash
pytest -vv
```

## Beispiel
```python
from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister
from src.buergerregister.validation import validiere_person
from src.buergerregister.jsonpersistance import JsonPersistence

register = JsonPersistence.load("people.json")
print("\033[92mBürgerregister CLI gestartet.\033[0m")
print("\033[94mDaten aus people.json geladen.\033[0m")
```

## Dokumentation
- Microsoft Word als Schriftliche Dokumentation
