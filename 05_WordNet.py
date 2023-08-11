# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen
# HINWEIS: Beim ersten Durchlauf muss das Modell heruntergeladen werden.
# Dazu das Kommentarzeichen ('# ') am Beginn von Zeile 9 beim ersten Durchlauf entfernen.

import wn

# wn.download('ewn:2020')

wn_active = wn.Wordnet(lang="en")

# Auswahl und Ausgabe aller Synsets mit einem Eintrag für 'duck'
synsets = wn_active.synsets("duck")

print("\nSynsets:")
for i, synset in enumerate(synsets):
    print(i, synset.definition())

# Auswahl des Synsets mit der Bedeutung 'Wasservogel'
target = synsets[0]

# Ausgabe von Hyponymen und Hyperonymen zum ausgwählten Synset
print("\nHyponyme: ")
for h in target.hyponyms():
    print(h.lemmas())

print("\nHyperonym:")
for h in target.hypernyms():
    print(h.lemmas())
