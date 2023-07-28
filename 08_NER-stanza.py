# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import stanza

text = 'Frank Hansen kocht Nudeln in Stuttgart.'

# Laden des Modells
nlp = stanza.Pipeline('de')

# Linguistische Analyse des Textes
doc = nlp(text)

# Ausgabe der Ergebnisse
for entity in doc.ents:
    print(entity.text, entity.type, entity.start_char, entity.end_char)



