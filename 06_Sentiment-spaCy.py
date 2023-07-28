# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen
# HINWEIS: Das deutsche Modell muss vor der Ausführung heruntergeladen werden, siehe https://spacy.io/models/de.
# Außerdem muss der Ordner "resources" dieses Repositoriums am Ort der Skriptausführung gespeichert sein.
# Alternativ kann SentiWS hier heruntergeladen werden: https://wortschatz.uni-leipzig.de/en/download
# Am Ende von Zeile 15 ist ggf. der Pfad anzupassen, unter dem die SentiWS-Daten gespeichert wurden.

import spacy
import spacy_sentiws

text = 'Gemeinsam mit tollen Menschen kann auch die langweiligste Aufgabe Spaß machen.'

nlp = spacy.load('de_core_news_sm')
nlp.add_pipe('sentiws', config={'sentiws_path': 'resources/SentiWS_v2.0'})

doc = nlp(text)

for token in doc:
    print(token.text, token._.sentiws)

