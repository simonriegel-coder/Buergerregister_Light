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

from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

def test_add_person_success():
    reg = Buergerregister()
    p = Person("Max", "Mustermann", 1999, "Bochum")
    assert reg.add(p) is True
    assert len(reg.list()) == 1

def test_add_duplicate_person():
    reg = Buergerregister()
    p1 = Person("Max", "Mustermann", 1999, "Bochum")
    p2 = Person("Max", "Mustermann", 1999, "Bochum")
    reg.add(p1)
    assert reg.add(p2) is False
    assert len(reg.list()) == 1
