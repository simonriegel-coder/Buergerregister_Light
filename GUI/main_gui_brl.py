# gui/main_gui.py
"""
GUI für ein einfaches Personen-Register.

Anforderungen:
- Hauptfenster (Titel, Größe)
- Label + Entry: Name, Geburtsjahr
- Button: „Person hinzufügen“
- Anzeige aller Personen (Listbox)
- Label für Status-/Fehlermeldungen
- Verbindung zur Service-Schicht (SimpleRegister)
- Manuelle Tests: gültig/ungültig, Mehrfach-Eingaben

Hinweis zur Service-Schicht:
- Dieses GUI versucht SimpleRegister zu importieren.
- Falls Ihr Projektpfad anders ist, passen Sie bitte die IMPORTS unten an.
- Damit die Datei trotzdem "lauffähig" ist, gibt es einen kleinen Fallback-Register (nur für lokale GUI-Tests).
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from datetime import date
from dataclasses import dataclass
from typing import Any, Iterable, Optional


# ---------------------------------------------------------------------------
# 1) Service-Schicht importieren (BITTE an Ihr Projekt anpassen)
# ---------------------------------------------------------------------------
# Mögliche Importpfade (Beispiele):
# from service.simple_register import SimpleRegister
# from src.service.simple_register import SimpleRegister
# from register.service.simple_register import SimpleRegister
#
# Passen Sie GENAU EINE Zeile passend zu Ihrem Projekt an.
#
# Damit das Programm sofort lauffähig ist, nutzen wir try/except + Fallback.

try:
    # >>>>> HIER ggf. anpassen <<<<<
    from service.simple_register import SimpleRegister  # type: ignore
except Exception:
    SimpleRegister = None  # type: ignore


# ---------------------------------------------------------------------------
# 2) Fallback-Implementierung (nur für GUI-Standalone-Tests)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Person:
    name: str
    birth_year: int

class DuplicatePersonError(Exception):
    """Wird geworfen, wenn eine Person mehrfach hinzugefügt werden soll."""
    pass

class _FallbackSimpleRegister:
    """Minimaler Register-Service, falls der echte SimpleRegister nicht importierbar ist."""
    def __init__(self) -> None:
        self._people: list[Person] = []

    def add_person(self, name: str, birth_year: int) -> None:
        # Duplikat-Definition: gleicher Name + gleiches Geburtsjahr
        p = Person(name=name, birth_year=birth_year)
        if p in self._people:
            raise DuplicatePersonError("Diese Person ist bereits vorhanden.")
        self._people.append(p)

    def list_people(self) -> list[Person]:
        return list(self._people)


def _make_register() -> Any:
    """
    Erzeugt die Register-Instanz.

    Erwartete (typische) API der Service-Schicht:
      - add_person(name: str, birth_year: int) -> None
      - list_people() -> Iterable[...]
    """
    if SimpleRegister is not None:
        try:
            return SimpleRegister()
        except TypeError:
            # Falls SimpleRegister zwingend Parameter erwartet:
            # -> Hier müssten Sie die Initialisierung anpassen.
            # Wir weichen dann auf Fallback aus, damit die GUI weiterhin testbar ist.
            return _FallbackSimpleRegister()
    return _FallbackSimpleRegister()


# ---------------------------------------------------------------------------
# 3) GUI-Logik
# ---------------------------------------------------------------------------

class MainGUI:
    def __init__(self, root: tk.Tk, register: Any) -> None:
        self.root = root
        self.register = register

        # --- Hauptfenster ---
        self.root.title("Simple Register – Personenverwaltung")
        self.root.geometry("520x360")
        self.root.minsize(520, 360)

        # --- Layout-Container ---
        self.main = ttk.Frame(self.root, padding=12)
        self.main.pack(fill="both", expand=True)

        self._build_form()
        self._build_list()
        self._build_status()

        # Initiale Anzeige
        self.refresh_people()

    def _build_form(self) -> None:
        form = ttk.LabelFrame(self.main, text="Person erfassen", padding=12)
        form.pack(fill="x")

        # Name
        ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(form, textvariable=self.name_var, width=34)
        self.name_entry.grid(row=0, column=1, sticky="we", pady=(0, 8))
        self.name_entry.focus_set()

        # Geburtsjahr
        ttk.Label(form, text="Geburtsjahr:").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
        self.year_var = tk.StringVar()
        self.year_entry = ttk.Entry(form, textvariable=self.year_var, width=12)
        self.year_entry.grid(row=1, column=1, sticky="w", pady=(0, 8))

        # Button
        self.add_btn = ttk.Button(form, text="Person hinzufügen", command=self.on_add_person)
        self.add_btn.grid(row=2, column=1, sticky="w")

        # Enter-Shortcut: in beiden Feldern soll Enter hinzufügen
        self.name_entry.bind("<Return>", lambda _e: self.on_add_person())
        self.year_entry.bind("<Return>", lambda _e: self.on_add_person())

        form.columnconfigure(1, weight=1)

    def _build_list(self) -> None:
        list_frame = ttk.LabelFrame(self.main, text="Alle Personen", padding=12)
        list_frame.pack(fill="both", expand=True, pady=(12, 0))

        self.people_list = tk.Listbox(list_frame, height=8)
        self.people_list.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.people_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.people_list.configure(yscrollcommand=scrollbar.set)

    def _build_status(self) -> None:
        self.status_var = tk.StringVar(value="Bereit.")
        status = ttk.Label(self.main, textvariable=self.status_var)
        status.pack(fill="x", pady=(10, 0))

    # --- Validierung ---
    def _validate_inputs(self, name_raw: str, year_raw: str) -> tuple[str, int]:
        name = name_raw.strip()
        if not name:
            raise ValueError("Name darf nicht leer sein.")

        try:
            year = int(year_raw.strip())
        except ValueError:
            raise ValueError("Geburtsjahr muss eine ganze Zahl sein.")

        current_year = date.today().year
        # Plausibilitätsgrenzen: frei anpassbar
        if year < 1900 or year > current_year:
            raise ValueError(f"Geburtsjahr muss zwischen 1900 und {current_year} liegen.")

        return name, year

    # --- Event Handler ---
    def on_add_person(self) -> None:
        """
        Verhalten bei Eingaben:
        - gültig: Person hinzufügen, Liste aktualisieren, Status OK, Felder leeren
        - ungültig: Status mit Fehlermeldung, Fokus auf problematisches Feld
        - Mehrfach-Eingabe: je nach Service-Schicht -> Fehler (Duplicate) oder erneute Aufnahme.
          Dieses GUI fängt typische Fehler ab und zeigt sie im Status.
        """
        name_raw = self.name_var.get()
        year_raw = self.year_var.get()

        try:
            name, year = self._validate_inputs(name_raw, year_raw)

            # Service-Schicht aufrufen (typische Signatur)
            # Falls Ihr Service anders heißt, bitte hier anpassen.
            if hasattr(self.register, "add_person"):
                self.register.add_person(name, year)
            elif hasattr(self.register, "add"):
                # Alternative API
                self.register.add(name, year)
            else:
                raise RuntimeError("Register-Service hat keine bekannte add-Methode.")

            self.refresh_people()
            self.status_var.set(f"OK: '{name}' ({year}) hinzugefügt.")

            # Eingabefelder zurücksetzen
            self.name_var.set("")
            self.year_var.set("")
            self.name_entry.focus_set()

        except DuplicatePersonError as e:
            self.status_var.set(f"Fehler (Duplikat): {e}")
        except ValueError as e:
            self.status_var.set(f"Eingabefehler: {e}")
        except Exception as e:
            # Generischer Catch, damit GUI nicht abstürzt und Fehlersuche möglich bleibt
            self.status_var.set(f"Systemfehler: {type(e).__name__}: {e}")

    def refresh_people(self) -> None:
        """Liest alle Personen aus dem Service und aktualisiert die Listbox."""
        self.people_list.delete(0, tk.END)

        people: Optional[Iterable[Any]] = None
        if hasattr(self.register, "list_people"):
            people = self.register.list_people()
        elif hasattr(self.register, "get_all"):
            people = self.register.get_all()
        elif hasattr(self.register, "all"):
            people = self.register.all()

        if people is None:
            self.people_list.insert(tk.END, "(Keine Schnittstelle zum Auslesen gefunden)")
            return

        # Darstellung robust halten (egal ob Person-Objekte oder Dicts oder Tupel geliefert werden)
        count = 0
        for p in people:
            display = self._format_person(p)
            self.people_list.insert(tk.END, display)
            count += 1

        if count == 0:
            self.people_list.insert(tk.END, "(Noch keine Personen)")

    def _format_person(self, p: Any) -> str:
        # Person dataclass / Objekt mit Attributen
        if hasattr(p, "name") and hasattr(p, "birth_year"):
            return f"{p.name} – {p.birth_year}"

        # Dict
        if isinstance(p, dict):
            n = p.get("name", "?")
            y = p.get("birth_year", p.get("year", "?"))
            return f"{n} – {y}"

        # Tuple/List (name, year)
        if isinstance(p, (tuple, list)) and len(p) >= 2:
            return f"{p[0]} – {p[1]}"

        # Fallback
        return str(p)


def main() -> None:
    register = _make_register()
    root = tk.Tk()
    # ttk Theme (optional)
    try:
        style = ttk.Style()
        # "clam" ist oft hübscher als default; falls nicht verfügbar, ignorieren.
        style.theme_use("clam")
    except Exception:
        pass

    MainGUI(root, register)
    root.mainloop()


if __name__ == "__main__":
    main()
# Ende von gui/main_gui.py