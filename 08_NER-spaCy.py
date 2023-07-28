# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen
# HINWEIS: Das deutsche Modell muss vor der Ausführung heruntergeladen werden, siehe https://spacy.io/models/de.

import spacy

text = "Frank Hansen kocht Nudeln in Stuttgart."

# Laden des Modells
nlp = spacy.load('de_core_news_sm')

# Linguistische Analyse des Textes
doc = nlp(text)

# Ausgabe der Ergebnisse
for entity in doc.ents:
    print(entity.text, entity.label_, entity.start_char, entity.end_char)
