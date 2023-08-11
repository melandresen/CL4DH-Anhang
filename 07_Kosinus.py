# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Erstellung des Datensatzes
df = pd.DataFrame(
    {
        "g": [0, 0, 93, 27],
        "und": [9, 13, 83, 31],
        "Minuten": [8, 50, 0, 0],
        "Salz": [1, 1, 45, 7],
        "Butter": [0, 0, 31, 6],
        "auf": [2, 3, 1, 3],
        "mit": [4, 7, 28, 14],
    },
    index=["kochen", "backen", "Zucker", "Mehl"],
)

print(df)

# Paarweise Berechnung der Kosinusähnlichkeit
print("kochen, backen: ", cosine_similarity([df.loc["kochen"]], [df.loc["backen"]]))
print("kochen, Zucker: ", cosine_similarity([df.loc["kochen"]], [df.loc["Zucker"]]))
print("kochen, Mehl: ", cosine_similarity([df.loc["kochen"]], [df.loc["Mehl"]]))
print("backen, Zucker: ", cosine_similarity([df.loc["backen"]], [df.loc["Zucker"]]))
print("backen, Mehl: ", cosine_similarity([df.loc["backen"]], [df.loc["Mehl"]]))
print("Zucker, Mehl: ", cosine_similarity([df.loc["Zucker"]], [df.loc["Mehl"]]))
