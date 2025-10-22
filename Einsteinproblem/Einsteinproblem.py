# Importiere den Z3-Solver
from z3 import * # type: ignore
# Z3 ist ein SMT-Solver (Satisfiability Modulo Theories), der zur Lösung logischer Probleme verwendet wird

# Es gibt 5 Häuser, nummeriert von 0 bis 4
houses = range(5)


# Definiere die möglichen Werte für jede Eigenschaft
colors = ["rot", "grün", "weiß", "gelb", "blau"]
nationalities = ["brite", "schwede", "däne", "norweger", "deutscher"]
drinks = ["tee", "kaffee", "milch", "bier", "wasser"]
cigarettes = ["pallmall", "dunhill", "marlboro", "winfield", "rothmanns"]
pets = ["hund", "vogel", "katze", "pferd", "fisch"]

# Erstelle Variablen für jede Eigenschaft in jedem Haus
color_vars = [Int(f"color_{i}") for i in houses]
nation_vars = [Int(f"nation_{i}") for i in houses]
drink_vars = [Int(f"drink_{i}") for i in houses]
cigarette_vars = [Int(f"cigarette_{i}") for i in houses]
pet_vars = [Int(f"pet_{i}") for i in houses]

# Initialisiere den Z3-Solver
s = Solver()
# Der Solver wird verwendet, um alle Bedingungen zu prüfen und eine gültige Lösung zu finden

# Jede Eigenschaft muss eine Permutation von 0 bis 4 sein (jede Kombination ist einzigartig)
for var_list in [color_vars, nation_vars, drink_vars, cigarette_vars, pet_vars]:
    s.add(Distinct(var_list))  # Alle Werte müssen verschieden sein
    for var in var_list:
        s.add(var >= 0, var < 5)  # Wertebereich: 0 bis 4

##################################################### Füge die Regeln aus dem Rätsel hinzu#############################################################################

# Regel 11: Der Norweger wohnt im ersten Haus
s.add(nation_vars[0] == nationalities.index("norweger"))

# Regel 15: Der Mann im mittleren Haus trinkt Milch
s.add(drink_vars[2] == drinks.index("milch"))

# Regeln mit direkten Zuordnungen
for i in houses:
    s.add(Implies(nation_vars[i] == nationalities.index("brite"), color_vars[i] == colors.index("rot")))         # Regel 5
    s.add(Implies(nation_vars[i] == nationalities.index("schwede"), pet_vars[i] == pets.index("hund")))          # Regel 6
    s.add(Implies(nation_vars[i] == nationalities.index("däne"), drink_vars[i] == drinks.index("tee")))          # Regel 7
    s.add(Implies(nation_vars[i] == nationalities.index("deutscher"), cigarette_vars[i] == cigarettes.index("rothmanns")))  # Regel 8
    s.add(Implies(color_vars[i] == colors.index("grün"), drink_vars[i] == drinks.index("kaffee")))               # Regel 9
    s.add(Implies(cigarette_vars[i] == cigarettes.index("winfield"), drink_vars[i] == drinks.index("bier")))     # Regel 10
    s.add(Implies(color_vars[i] == colors.index("gelb"), cigarette_vars[i] == cigarettes.index("dunhill")))      # Regel 13
    s.add(Implies(cigarette_vars[i] == cigarettes.index("pallmall"), pet_vars[i] == pets.index("vogel")))        # Regel 14

# Regel 12: Der Norweger wohnt neben dem blauen Haus
s.add(Or(
    And(nation_vars[0] == nationalities.index("norweger"), color_vars[1] == colors.index("blau")),
    And(nation_vars[1] == nationalities.index("norweger"), color_vars[0] == colors.index("blau"))
))

# Regel 16: Das grüne Haus steht direkt links vom weißen Haus
for i in range(4):  # Nur bis Haus 3, damit i+1 nicht aus dem Bereich fällt
    s.add(Implies(color_vars[i] == colors.index("grün"), color_vars[i+1] == colors.index("weiß")))

# Regel 17: Marlboro-Raucher wohnt neben dem mit der Katze
for i in houses:
    neighbors = []
    if i > 0:
        neighbors.append(pet_vars[i-1] == pets.index("katze"))
    if i < 4:
        neighbors.append(pet_vars[i+1] == pets.index("katze"))
    s.add(Implies(cigarette_vars[i] == cigarettes.index("marlboro"), Or(neighbors)))

# Regel 18: Marlboro-Raucher hat einen Nachbarn, der Wasser trinkt
for i in houses:
    neighbors = []
    if i > 0:
        neighbors.append(drink_vars[i-1] == drinks.index("wasser"))
    if i < 4:
        neighbors.append(drink_vars[i+1] == drinks.index("wasser"))
    s.add(Implies(cigarette_vars[i] == cigarettes.index("marlboro"), Or(neighbors)))

# Regel 19: Der Mann mit dem Pferd wohnt neben dem Dunhill-Raucher
for i in houses:
    neighbors = []
    if i > 0:
        neighbors.append(cigarette_vars[i-1] == cigarettes.index("dunhill"))
    if i < 4:
        neighbors.append(cigarette_vars[i+1] == cigarettes.index("dunhill"))
    s.add(Implies(pet_vars[i] == pets.index("pferd"), Or(neighbors)))

# Berechne die Lösung
if s.check() == sat:
# Wenn das Problem lösbar ist, wird das Modell ausgegeben
    m = s.model()
    for i in houses:
        if m.evaluate(pet_vars[i]).as_long() == pets.index("fisch"):
            besitzer = nationalities[m.evaluate(nation_vars[i]).as_long()]
            print(f"Der {besitzer} hält den Fisch als Haustier.")
else:
    print("Keine Lösung gefunden.")
