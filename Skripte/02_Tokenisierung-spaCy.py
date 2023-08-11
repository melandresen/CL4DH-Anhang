# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen
# HINWEIS: Das deutsche Modell muss vor der Ausführung heruntergeladen werden, siehe https://spacy.io/models/de.

import spacy

text = """Ich habe gerade Frau Dr. Meier getroffen. Das Buch erscheint in dritter Aufl.
Am Mittwoch fliege ich nach New York. Ich mag z.B. Enten."""

# Laden des Modells
nlp = spacy.load("de_core_news_sm")

# Linguistische Analyse des Textes
doc = nlp(text)

# Ausgabe der Ergebnisse
for sentence in doc.sents:
    tokens = [i for i in sentence]
    print(tokens)
