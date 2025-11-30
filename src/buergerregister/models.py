from dataclasses import dataclass

@dataclass
class Person:
    """Repräsentiert eine Bürgerin bzw. einen Bürger."""
    vorname: str
    nachname: str
    geburtsjahr: int
    wohnort: str

    def __post_init__(self):
        if not (1900 <= self.geburtsjahr <= 2025):
            raise ValueError("Geburtsjahr unplausibel.")