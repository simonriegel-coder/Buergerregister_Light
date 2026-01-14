from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from typing import List


# ---------------------------------------------------------------------------
# Serviceschicht (Vorgegeben / zu verwenden)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PersonEntry:
    """Datenobjekt für einen Personeneintrag."""
    name: str
    birth_year: int

    def display_text(self) -> str:
        """Textdarstellung für die Listbox."""
        return f"{self.name} ({self.birth_year})"


class SimpleRegister:
    """Sehr einfache Serviceschicht zur Verwaltung von Personen."""

    def __init__(self) -> None:
        self._entries: List[PersonEntry] = []

    def add_person(self, name: str, birth_year: int) -> bool:
        """Fügt eine Person hinzu."""
        entry = PersonEntry(name=name, birth_year=birth_year)
        if entry in self._entries:
            return False
        self._entries.append(entry)
        return True

    def list_all(self) -> List[PersonEntry]:
        """Gibt alle Personen zurück (als Kopie)."""
        return list(self._entries)


# ---------------------------------------------------------------------------
# GUI-Schicht
# ---------------------------------------------------------------------------

class RegisterApp(tk.Tk):
    """Tkinter-App für das Bürgerregister Light."""

    def __init__(self, register: SimpleRegister | None = None) -> None:
        super().__init__()

        # TODO 1: Fenstertitel und Größe setzen
        self.title("Bürgerregister Light")
        self.geometry("820x620")
        self.resizable(False, False)

        # Serviceschicht
        self._register = register or SimpleRegister()

        # Tkinter-Variablen
        self.name_var = tk.StringVar()
        self.year_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Bereit.")

        # Widgets aufbauen
        self._build_widgets()

    def _build_widgets(self) -> None:
        """Erzeugt alle GUI-Elemente."""

        # TODO 2: Frame für Eingaben
        input_frame = tk.Frame(self, padx=10, pady=10)
        input_frame.pack(fill="x")

        # TODO 3: Labels + Entry
        tk.Label(input_frame, text="Vorname:").grid(row=0, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.name_var, width=30).grid(
            row=0, column=1, padx=5
        )

        tk.Label(input_frame, text="Nachname:").grid(row=0, column=2, sticky="w")
        tk.Entry(input_frame, width=30).grid(
            row=0, column=3, padx=5
        )

        tk.Label(input_frame, text="Geburtsjahr:").grid(row=1, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.year_var, width=30).grid(
            row=1, column=1, padx=5
        )

        tk.Label(input_frame, text="Wohnort:").grid(row=1, column=2, sticky="w")
        tk.Entry(input_frame, width=30).grid(
            row=1, column=3, padx=5
        )

        # TODO 4: Button
        tk.Button(
            input_frame,
            text="Person hinzufügen",
            command=self.on_add_person,
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # TODO 5: Listbox + Scrollbar
        list_frame = tk.Frame(self)
        list_frame.pack(fill="both", expand=True, padx=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.person_listbox = tk.Listbox(
            list_frame, height=8, yscrollcommand=scrollbar.set
        )
        self.person_listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.person_listbox.yview)

        # TODO 6: Status-Label
        self._status_label = tk.Label(
            self, textvariable=self.status_var, anchor="w", padx=10
        )
        self._status_label.pack(fill="x")

        # TODO 7: Initiale Anzeige
        self.refresh_person_list()

    def on_add_person(self) -> None:
        """Handler für den Button „Person hinzufügen“."""

        # TODO 8: Eingaben auslesen
        name = self.name_var.get().strip()
        year_str = self.year_var.get().strip()

        # TODO 9: Validierung
        if not name:
            self._set_status("Name darf nicht leer sein.", error=True)
            return

        try:
            birth_year = int(year_str)
        except ValueError:
            self._set_status("Geburtsjahr muss eine Zahl sein.", error=True)
            return

        if birth_year < 1800 or birth_year > 2100:
            self._set_status("Geburtsjahr außerhalb des gültigen Bereichs.", error=True)
            return

        # TODO 10: Service aufrufen
        added = self._register.add_person(name, birth_year)

        # TODO 11: Anzeige & Status
        if added:
            self.refresh_person_list()
            self._set_status("Person erfolgreich hinzugefügt.")
            self.name_var.set("")
            self.year_var.set("")
        else:
            self._set_status("Person existiert bereits.", error=True)

    def refresh_person_list(self) -> None:
        """Listbox mit allen Personen neu aufbauen."""
        # TODO 12
        self.person_listbox.delete(0, tk.END)
        for entry in self._register.list_all():
            self.person_listbox.insert(tk.END, entry.display_text())

    def _set_status(self, message: str, *, error: bool = False) -> None:
        """Statuszeile aktualisieren."""
        # TODO 13
        self.status_var.set(message)
        self._status_label.config(fg="red" if error else "blue")


def main() -> None:
    """Startet die Anwendung."""
    app = RegisterApp()
    app.mainloop()


if __name__ == "__main__":
    main()
