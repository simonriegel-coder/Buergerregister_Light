from typing import Tuple, List, Dict, Any

def validiere_person(p: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Prüft Pflichtfelder und Plausibilität.

    Args:
        p: Dictionary mit Schlüsseln vorname, nachname, geburtsjahr, wohnort
    Returns:
        Tuple[bool, List[str]]: (ist_valide, fehlerliste)
    """
    errors: List[str] = []
    if not p.get("vorname"):
        errors.append("Vorname fehlt.")
    if not p.get("nachname"):
        errors.append("Nachname fehlt.")
    jahr = p.get("geburtsjahr")
    if not isinstance(jahr, int) or not (1900 <= jahr <= 2025):
        errors.append("Geburtsjahr unplausibel.")
    if not p.get("wohnort"):
        errors.append("Wohnort fehlt.")
    return (len(errors) == 0, errors)
