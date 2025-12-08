from dataclasses import dataclass
from typing import Dict


@dataclass
class Person:
    """Repräsentiert eine Bürgerin bzw. einen Bürger."""
    vorname: str
    nachname: str
    geburtsjahr: int
    wohnort: str

    def __post_init__(self):
        pass
        

    def to_dict(self) -> Dict:
        """
        Gibt eine dict-Repräsentation der Person zurück.
        Nützlich für Ausgabe- oder Serialisierungszwecke.
        """
        return {
            "vorname": self.vorname,
            "nachname": self.nachname,
            "geburtsjahr": self.geburtsjahr,
            "wohnort": self.wohnort,
        }

    def get_full_name(self) -> str:
        """Gibt den vollständigen Namen zurück."""
        return f"{self.vorname} {self.nachname}"
    
    def get_wohnort(self) -> str:
         """Gibt den Wohnort Zurück."""
         return self.wohnort
    
    def get_geburtsjahr(self) -> int:
            """Gibt das Geburtsjahr Zurück."""
            return self.geburtsjahr
        

  