# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import nltk
from HanTa import HanoverTagger as ht

text = "Im Teich in unserem Viertel schwimmen oft viele Enten."

# Tagger mit deutschem Modell laden
tagger_de = ht.HanoverTagger("morphmodel_ger.pgz")

# Tokenisierung mit dem NLTK
tokens = nltk.word_tokenize(text)

# Annotation mit HanTa
annotation = tagger_de.tag_sent(tokens)

# Ausgabe der Ergebnisse
for tokens in annotation:
    print(tokens)
