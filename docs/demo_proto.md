# 🧩 Bürgerregister Light – Demo-Skript (5 Schritte)

**Ziel:** Kurze, reproduzierbare Live-Demo der Kernfunktionen des Prototyps  
**Dauer:** ca. 5 – 7 Minuten  
**Voraussetzungen:**  
- Virtuelle Umgebung aktiv  
- Projekt installiert (`pip install -e .`)  
- Terminal geöffnet im Projektverzeichnis  

---

## **Schritt 1 – Start und Import**
**Ziel:** Zeigen, dass das Modul sauber importierbar ist.  
**Befehle:**
```python
from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

reg = Buergerregister()
print("Bürgerregister erfolgreich gestartet.")
```
**Erwartete Ausgabe:**
```
Bürgerregister erfolgreich gestartet.
```
**Erklärung:** Das System initialisiert ein leeres In-Memory-Register.  

---

## **Schritt 2 – Neue Person anlegen**
**Ziel:** Demonstration des erfolgreichen Hinzufügens einer validen Person.  
**Befehle:**
```python
p1 = Person("Anna", "Schmidt", 1990, "Essen")
reg.add(p1)
```
**Erwartete Ausgabe:**
```
True
```
**Erklärung:** Die Person wird korrekt hinzugefügt, da alle Pflichtfelder erfüllt sind.  

---

## **Schritt 3 – Liste aller Personen anzeigen**
**Ziel:** Zeigen, dass das Register Objekte korrekt speichert.  
**Befehle:**
```python
for person in reg.list():
    print(person)
```
**Erwartete Ausgabe:**
```
Person(vorname='Anna', nachname='Schmidt', geburtsjahr=1990, wohnort='Essen')
```
**Erklärung:** Das Register gibt die gespeicherten Objekte aus.  

---

## **Schritt 4 – Fehlerfall: Ungültige Eingabe**
**Ziel:** Präsentation der Validierung und Fehlermeldungen.  
**Befehle:**
```python
from src.buergerregister.validation import validiere_person

invalid = {"vorname": "", "nachname": "", "geburtsjahr": 1800, "wohnort": ""}
print(validiere_person(invalid))
```
**Erwartete Ausgabe (Beispiel):**
```
(False, ['Vorname fehlt.', 'Nachname fehlt.', 'Geburtsjahr unplausibel.', 'Wohnort fehlt.'])
```
**Erklärung:** Das System erkennt unplausible Eingaben.  

---

## **Schritt 5 – Duplikat prüfen**
**Ziel:** Zeigen, dass doppelte Personen abgefangen werden.  
**Befehle:**
```python
duplicate = Person("Anna", "Schmidt", 1990, "Essen")
reg.add(duplicate)
```
**Erwartete Ausgabe:**
```
Warnung: Duplikat gefunden.
False
```
**Erklärung:** Das System prüft Duplikate anhand von Vor- und Nachname.  

---

## 💡 **Zusatzempfehlung für die Präsentation**
| Tipp | Nutzen |
|------|--------|
| Verwenden Sie eine **vorkonfigurierte Python-Konsole oder Jupyter-Notebook**, um Kopierfehler zu vermeiden. | Flüssige Live-Demo |
| Halten Sie eine **zweite Konsole** bereit, falls ein Fehler auftritt. | Backup |
| Schließen Sie mit einem **kurzen Fazit**: „Wir haben ein sauberes, testbares Grundgerüst mit klaren Verantwortlichkeiten geschaffen.“ | Professioneller Abschluss |
