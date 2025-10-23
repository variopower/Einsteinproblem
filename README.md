
# Einsteinproblem mit Z3

Dieses Skript löst das berühmte Einstein-Rätsel mithilfe des Z3-Solvers.
Ein Z3-Solver ist ein sogenannter SMT-Solver (Satisfiability Modulo Theories). Er dient dazu, logische Formeln zu lösen, die nicht nur boolesche Logik enthalten, sondern auch komplexere Theorien wie Arithmetik, Mengen oder Arrays. SMT-Solver sind besonders nützlich in Bereichen wie formaler Verifikation, Constraint-Programmierung und Modellprüfung.
Diese Lösung wurde gewählt, da im Wahlfach „Advanced Methods of Software Engineering“ bei Prof. Stefan Kugele genau diese Art des Beweisens von Formeln gezeigt wurde mit der Programmiersprache Python. Und da Python die gewählte Lieblingssprache war fand ich diesen Lösungsansatz als sinnvoll um an eine möglichst kurze Lösung zu gelangen. 

## Voraussetzungen
- Python 3.7 oder höher
- Z3-Python-Bibliothek
(falls noch nicht vorhanden über requirements.txt installieren)
## Installation
Führe die folgenden Schritte aus, um das Skript auf einem anderen Entwicklungsrechner auszuführen:

1. Python installieren: https://www.python.org/downloads/
2. Virtuelle Umgebung erstellen (optional aber empfohlen):
   ```bash
   python -m venv venv
   source venv/bin/activate  # oder venv\Scriptsactivate auf Windows
   ```
3. Z3 installieren:
   ```bash
   pip install z3-solver
   ```
oder alternativ
1. Python installieren: https://www.python.org/downloads/
2. VSC downloaden und installieren: https://code.visualstudio.com/download
3. Einsteinproblem.py in Entwicklungsumgebung öffnen und über internes Terminal starten


## Ausführung
Starte das Skript mit:
```bash
python Einsteinproblem.py
```

## Ausgabe
Das Programm gibt aus, welche Nationalität von Hausbesitzer das Haustier Fisch besitzt.
