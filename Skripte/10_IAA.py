# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

from sklearn.metrics import cohen_kappa_score

# Erstellung des Datensatzes
person_1 = 60 * ["Ente"] + 15 * ["Ente"] + 10 * ["Gans"] + 15 * ["Gans"]
person_2 = 60 * ["Ente"] + 15 * ["Gans"] + 10 * ["Ente"] + 15 * ["Gans"]

# Berechnung und Ausgabe des Inter-Annotator-Agreements
iaa = cohen_kappa_score(person_1, person_2)
print(round(iaa, 3))
