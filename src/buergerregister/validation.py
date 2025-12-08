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
        errors.append("\033[91mVorname fehlt.\033[0m")
    elif any(ch.isdigit() for ch in vorname):
        errors.append("\033[91mVorname darf keine Zahlen enthalten.\033[0m")

    # Nachname prüfen
    nachname = p.get("nachname")
    if not nachname:
        errors.append("\033[91mNachname fehlt.\033[0m")
    elif any(ch.isdigit() for ch in nachname):
        errors.append("\033[91mNachname darf keine Zahlen enthalten.\033[0m")

    # Wohnort prüfen
    wohnort = p.get("wohnort")
    if not wohnort:
        errors.append("\033[91mWohnort fehlt.\033[0m]")

    # Geburtsjahr prüfen
    jahr = p.get("geburtsjahr")
    if not isinstance(jahr, int) or not (1900 <= jahr <= 2025):
        errors.append("\033[91mGeburtsjahr unplausibel.\033[0m]")

    return (len(errors) == 0, errors)