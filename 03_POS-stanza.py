# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import stanza

text = "Im Teich in unserem Viertel schwimmen oft viele Enten."

# Laden des Modells
nlp = stanza.Pipeline("de", processors=["tokenize", "pos"])

# Linguistische Analyse des Textes
doc = nlp(text)

# Ausgabe der Ergebnisse
for sentence in doc.sentences:
    for token in sentence.words:
        print(token.text, token.xpos)
