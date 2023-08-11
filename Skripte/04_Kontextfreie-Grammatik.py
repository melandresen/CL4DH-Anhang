# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import numpy as np


def generate_sentence():
    """Funktion zur Kombination von Substantiven und Verben zu einfachen Sätzen"""

    nouns = ["Ente", "Welt", "Karotte"]
    verbs = ["quakt", "endet", "schmeckt"]
    sentence = "Die {} {}.".format(
        np.random.choice(nouns, 1)[0], np.random.choice(verbs, 1)[0]
    )
    return sentence


# Zufällige Generierung und Ausgabe von n Sätzen
n = 10

for i in range(n):
    print(generate_sentence())
