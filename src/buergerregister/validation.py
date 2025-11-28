from typing import Tuple, List, Dict, Any


def validiere_person(p: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validiert eine Person:
    - prüft Pflichtfelder (vorname, nachname, geburtsjahr, wohnort)
    - prüft, dass Vor- und Nachname keine Ziffern enthalten
    - prüft plausibles Geburtsjahr (1900–2025)
    """
    errors: List[str] = []

    # Vorname prüfen
    vorname = p.get("vorname")
    if not vorname:
        errors.append("Vorname fehlt.")
    elif any(ch.isdigit() for ch in vorname):
        errors.append("Vorname darf keine Zahlen enthalten.")

    # Nachname prüfen
    nachname = p.get("nachname")
    if not nachname:
        errors.append("Nachname fehlt.")
    elif any(ch.isdigit() for ch in nachname):
        errors.append("Nachname darf keine Zahlen enthalten.")

    # Wohnort prüfen
    wohnort = p.get("wohnort")
    if not wohnort:
        errors.append("Wohnort fehlt.")

    # Geburtsjahr prüfen
    jahr = p.get("geburtsjahr")
    if not isinstance(jahr, int) or not (1900 <= jahr <= 2025):
        errors.append("Geburtsjahr unplausibel.")

    return (len(errors) == 0, errors)
