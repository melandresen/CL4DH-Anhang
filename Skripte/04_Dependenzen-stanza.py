# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import stanza

text = "Im Teich in unserem Viertel schwimmen oft viele Enten."

# Laden des Modells
nlp = stanza.Pipeline("de")

# Linguistische Analyse des Textes
doc = nlp(text)

# Ausgabe der Ergebnisse
for sent in doc.sentences:
    for token in sent.words:
        print(token.id, token.text, token.deprel, token.head)
