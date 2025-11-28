# Bürgerregister Light – Starterpaket

Dieses Repository bildet das Starterpaket für die Teilprüfung 1 (Präsentation: Softwareentwurf & Prototyp).

## Ziele
- UML modellieren (Use-Case, Klassen, Sequenz)
- Python-Grundstruktur implementieren
- Live-Demo vorbereiten

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -U pip
pip install -e .[dev]
```

## Tests ausführen
```bash
pytest -q
```

## Beispiel
```python
from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

reg = Buergerregister()
reg.add(Person("Anna", "Schmidt", 1990, "Essen"))
print(reg.list())
```

## Dokumentation
- UML-Diagramme als Platzhalter unter `docs/uml/`
- Cheat-Sheets unter `docs/cheatsheets/`
