# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import stanza

text = '''Ich habe gerade Frau Dr. Meier getroffen. Das Buch erscheint in dritter Aufl. 
Am Mittwoch fliege ich nach New York. Ich mag z.B. Enten.'''

nlp = stanza.Pipeline('de', processors='tokenize')

# Linguistische Analyse des Textes
doc = nlp(text)

# Ausgabe der Ergebnisse
for sentence in doc.sentences:
    tokens = [i.text for i in sentence.tokens]
    print(tokens)
